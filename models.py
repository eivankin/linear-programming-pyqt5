import sqlite3
from collections import defaultdict

"""В этом файле содержится подключение к базе данных sqlite3 и объекты моделей,
связывающие таблицы в БД с объектами в коде (простой вариант ORM). 
Все модели наследуются от базового класса AbstractModel."""

DATABASE = 'examples.db'
CONNECTION = sqlite3.connect(DATABASE)
CURSOR = CONNECTION.cursor()


class AbstractModel:
    """Базовый класс модели для наследования"""
    TABLE = None
    VERBOSE_ATTRS = {}
    VERBOSE_VALS = defaultdict(dict)

    def __init__(self):
        self.ATTRS = [] if not self.TABLE else [
            d[0] for d in
            CURSOR.execute('SELECT * FROM ' + self.TABLE).description
        ]

    def get_title(self):
        """Возвращает человекочитаемый список атрибутов"""
        return [self.VERBOSE_ATTRS.get(a, a) for a in self.ATTRS]

    class __ModelObject:
        def __init__(self, model, saved=False, **kwargs):
            """Инициализирует объект модели 'model' с заданными аттрибутами.
            Если хотя бы одного аттрибута нет в списке аттрибутов модели - поднимает исключение."""
            for key, value in kwargs.items():
                if key in model.ATTRS:
                    self.__dict__[key] = value
                else:
                    raise AttributeError(f'"{type(model).__name__}" has no attribute "{key}"')
            self._model = model
            self._saved = saved

        def __setattr__(self, key, value):
            """Присваивает значение 'value' аттрибуту 'key',
            если 'key' есть в списке аттрибутов модели,
            иначе - поднимает исключение."""
            if key.startswith('_') or key in self._model.ATTRS:
                self.__dict__[key] = value
            else:
                raise AttributeError(f'"{type(self._model).__name__}" has no attribute "{key}"')

        def save(self):
            """Сохраняет объект в базе данных и помечает его как сохранённый.
            Если объект уже сохранён, то ничего не происходит."""
            if not self._saved:
                filtered = {}
                for key in self.__dict__.keys():
                    if not key.startswith('_'):
                        filtered[key] = self.__dict__[key]
                keys = filtered.keys()
                values = filtered.values()
                CURSOR.execute(f'''INSERT INTO {self._model.TABLE}
                                ({", ".join(keys)}) 
                                VALUES ({", ".join("?" * len(values))})''',
                               tuple(values))
                CONNECTION.commit()
                self._saved = True
                if 'id' in self._model.ATTRS:
                    self.id = CURSOR.lastrowid

        def delete(self):
            """Удаляет объект из базы данных, если он есть в ней.
            Если объект не сохранён в базе данных, ничего не происходит."""
            if self._saved:
                CURSOR.execute(f'''DELETE FROM {self._model.TABLE} WHERE id=?''', (self.id,))
                CONNECTION.commit()
                self._saved = False
                del self.id

    def update(self, pk, **kwargs):
        """Обновляет объект в базе данных по id.
        :param pk: id объекта в БД.
        :param kwargs: словарь, ключи которого являются атрибутами для обновления."""
        CURSOR.execute(f'''UPDATE {self.TABLE}
            SET {", ".join(map(lambda x: f'{x}=?', kwargs.keys()))}
            WHERE id=?''', (*kwargs.values(), pk))
        CONNECTION.commit()

    def new(self, **kwargs):
        """Создаёт и возвращает объект модели с заданными аттрибутами."""
        obj = self.__ModelObject(self, **kwargs)
        return obj

    def all(self):
        """Возвращает список всех объектов модели."""
        return [self.__ModelObject(self, True, **dict(zip(self.ATTRS, x)))
                for x in CURSOR.execute('SELECT * FROM ' + self.TABLE).fetchall()]

    def __get_filter_cursor(self, mode='=', **kwargs):
        if not kwargs:
            raise ValueError('''empty constraints (set it in method call). 
            Use method "all" to get full list of objects.''')
        values = kwargs.values() if mode == '=' else map(lambda x: f'%{x}%', kwargs.values())
        q = f'''SELECT * FROM {self.TABLE} WHERE '''
        q += ' AND '.join(map(lambda x: f'{x} {mode} ?', kwargs.keys()))
        return CURSOR.execute(q, tuple(values))

    def row_to_obj(self, row):
        """Преобразует строку таблицы в объект модели.
        :param row: строка таблицы.
        :return ModelObject: созданный объект."""
        if len(row) == len(self.ATTRS) - 1:
            return self.__ModelObject(self, False, **dict(zip(self.ATTRS[1:], row)))
        return self.__ModelObject(self, True, **dict(zip(self.ATTRS, row)))

    def get(self, **kwargs):
        """Возвращает один объект по заданным ограничениям типа 'аттрибут=значение'.
        Если объектов, удовлетворяющих ограничениям, несколько, то возвращает первый.
        Если объект не найден, возвращает None"""
        result = self.__get_filter_cursor(**kwargs).fetchone()
        return None if not result else self.row_to_obj(result)

    def filter(self, **kwargs):
        """Возвращает список строк с атрибутами объектов по заданным ограничениям типа 'аттрибут=значение'.
        Список может быть пустым."""
        result = self.__get_filter_cursor(**kwargs).fetchall()
        if not result:
            result = self.__get_filter_cursor(mode='LIKE', **kwargs).fetchall()
        return [self.row_to_obj(row) for row in result]


class TaskModel(AbstractModel):
    TABLE = 'Task'
    LIM_INF = -1
    LIM_ZERO = 1
    VERBOSE_ATTRS = {
        'problem_situation': 'Условие задачи',
        'target_func_lim': 'Оптимальное значение ЦФ',
        'target_func_coefs': 'Коэффициенты ЦФ',
        'inequalities_coefs': 'Коэффициенты линейных ограничений',
        'inequalities_consts': 'Значения линейных ограничений',
        'axis_coefs': 'Коэффициенты осевых ограничений',
        'axis_consts': 'Значения осевых ограничений',
        'settings_id': 'Настройки стилей',
    }
    VERBOSE_VALS = defaultdict(
        dict, {'target_func_lim': {LIM_INF: 'Максимум', LIM_ZERO: 'Минимум'}}
    )


class TagModel(AbstractModel):
    TABLE = 'Tag'
    VERBOSE_ATTRS = {'name': 'Название тега'}


class TaskTagModel(AbstractModel):
    TABLE = 'TaskTag'
