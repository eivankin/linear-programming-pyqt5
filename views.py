from PyQt5 import QtCore, QtGui, QtWidgets
from utility import Plotter


"""В этом файле хранятся классы интерфейсов, созданные в QtDesigner"""


class Ui_SolveViewer:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.plotter = Plotter(MainWindow)
        self.plotter.setObjectName("plot")
        MainWindow.setCentralWidget(self.plotter)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Решение задачи"))


class Ui_TaskViewer:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.searchLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.searchLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tagLabel = QtWidgets.QLabel(self.centralwidget)
        self.tagLabel.setFont(font)
        self.tagLabel.resize(self.label.size())
        self.tagSelector = QtWidgets.QComboBox(self.centralwidget)
        self.tagSelector.addItem("")
        self.searchLayout.addWidget(self.tagLabel, 1, 0, 1, 1)
        self.searchLayout.addWidget(self.tagSelector, 1, 1, 1, 1)
        self.searchLine = QtWidgets.QLineEdit(self.centralwidget)
        self.searchLine.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.searchLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.searchLayout.addWidget(self.searchLine, 0, 2, 1, 1)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchLayout.addWidget(self.searchButton, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.searchLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("horizontalLayout_2")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("pushButton_2")
        self.solveButton = QtWidgets.QPushButton(self.centralwidget)
        self.solveButton.setObjectName("pushButton_2")
        self.exportButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportButton.setObjectName("pushButton_3")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setObjectName("pushButton_4")
        self.buttonLayout.addWidget(self.solveButton)
        self.buttonLayout.addWidget(self.deleteButton)
        self.buttonLayout.addWidget(self.exportButton)
        self.buttonLayout.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.buttonLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.loadMenu = QtWidgets.QMenu(self.menubar)
        self.loadMenu.setObjectName("menu")
        self.newTaskMenu = QtWidgets.QMenu(self.menubar)
        self.newTaskMenu.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.loadDBAction = QtWidgets.QAction(MainWindow)
        self.loadDBAction.setObjectName("load_db_action")
        self.loadFileAction = QtWidgets.QAction(MainWindow)
        self.loadFileAction.setObjectName("action_2")
        self.loadMenu.addAction(self.loadDBAction)
        self.loadMenu.addAction(self.loadFileAction)
        self.addNewTaskAction = QtWidgets.QAction(MainWindow)
        self.addNewTaskAction.setObjectName("action_3")
        self.solveNewTaskAcion = QtWidgets.QAction(MainWindow)
        self.newTaskMenu.addAction(self.addNewTaskAction)
        self.newTaskMenu.addAction(self.solveNewTaskAcion)
        self.solveNewTaskAcion.setObjectName("action_4")
        self.menubar.addAction(self.loadMenu.menuAction())
        self.menubar.addAction(self.newTaskMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Просмотр списка задач"))
        self.label.setText(_translate("MainWindow", "Поиск:"))
        self.tagLabel.setText(_translate("MainWindow", "Тег:"))
        self.tagSelector.setItemText(0, _translate("MainWindow", "Любой"))
        self.comboBox.setItemText(0, _translate("MainWindow", "По всем параметрам"))
        self.searchButton.setText(_translate("MainWindow", "Поиск"))
        self.solveButton.setText(_translate("MainWindow", "Решить"))
        self.deleteButton.setText(_translate("MainWindow", "Удалить"))
        self.exportButton.setText(_translate("MainWindow", "Экспортировать"))
        self.saveButton.setText(_translate("MainWindow", "Сохранить изменения"))
        self.loadMenu.setTitle(_translate("MainWindow", "Открыть"))
        self.newTaskMenu.setTitle(_translate("MainWindow", "Новая задача"))
        self.loadDBAction.setText(_translate("MainWindow", "Базу примеров"))
        self.loadFileAction.setText(_translate("MainWindow", "Файл..."))
        self.addNewTaskAction.setText(_translate("MainWindow", "Добавить к текущей таблице"))
        self.solveNewTaskAcion.setText(_translate("MainWindow", "Ввести данные и решить"))


class Ui_NewTaskDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 417)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.problemSituation = QtWidgets.QPlainTextEdit(Dialog)
        self.problemSituation.setObjectName("problemSituation")
        self.verticalLayout.addWidget(self.problemSituation)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.required = QtWidgets.QLabel(Dialog)
        self.required.setMaximumSize(QtCore.QSize(16, 16777215))
        self.required.setStyleSheet("color: red")
        self.required.setObjectName("required")
        self.horizontalLayout.addWidget(self.required)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.optimalValue = QtWidgets.QComboBox(Dialog)
        self.optimalValue.setObjectName("optimalValue")
        self.optimalValue.addItem("")
        self.optimalValue.addItem("")
        self.horizontalLayout.addWidget(self.optimalValue)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.required_2 = QtWidgets.QLabel(Dialog)
        self.required_2.setMaximumSize(QtCore.QSize(16, 16777215))
        self.required_2.setStyleSheet("color: red")
        self.required_2.setObjectName("required_2")
        self.horizontalLayout_2.addWidget(self.required_2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.a1Coef = QtWidgets.QDoubleSpinBox(Dialog)
        self.a1Coef.setObjectName("a1Coef")
        self.a1Coef.setMaximum(1e4)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.a1Coef)
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.a2Coef = QtWidgets.QDoubleSpinBox(Dialog)
        self.a2Coef.setMaximum(1e4)
        self.a2Coef.setObjectName("a2Coef")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.a2Coef)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.required_3 = QtWidgets.QLabel(Dialog)
        self.required_3.setMaximumSize(QtCore.QSize(12, 16777215))
        self.required_3.setStyleSheet("color: red")
        self.required_3.setObjectName("required_3")
        self.horizontalLayout_3.addWidget(self.required_3)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton_2 = QtWidgets.QToolButton(Dialog)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout.addWidget(self.toolButton_2, 1, 1, 1, 1)
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 0, 1, 1, 1)
        self.constraintsList = QtWidgets.QListWidget(Dialog)
        self.constraintsList.setObjectName("costraints")
        self.gridLayout.addWidget(self.constraintsList, 0, 0, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.required_4 = QtWidgets.QLabel(Dialog)
        self.required_4.setMaximumSize(QtCore.QSize(12, 16777215))
        self.required_4.setStyleSheet("color: red")
        self.required_4.setObjectName("required_4")
        self.horizontalLayout_4.addWidget(self.required_4)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setItalic(False)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.x1Gte = QtWidgets.QDoubleSpinBox(Dialog)
        self.x1Gte.setObjectName("x1Gte")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.x1Gte)
        self.label_9 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setItalic(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.x2Gte = QtWidgets.QDoubleSpinBox(Dialog)
        self.x2Gte.setObjectName("x2Gte")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.x2Gte)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Новая задача"))
        self.label.setText(_translate("Dialog", "Условие задачи:"))
        self.required.setText(_translate("Dialog", "*"))
        self.label_2.setText(_translate("Dialog", "Оптмальное значение целевой функции:"))
        self.optimalValue.setItemText(0, _translate("Dialog", "Минимум"))
        self.optimalValue.setItemText(1, _translate("Dialog", "Максимум"))
        self.required_2.setText(_translate("Dialog", "*"))
        self.label_3.setText(_translate("Dialog", "Коэффициенты целевой функции:"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>a<span style=\" "
                                                  "vertical-align:sub;\">1</span> = </p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p>a<span style=\" "
                                                  "vertical-align:sub;\">2</span> = </p></body></html>"))
        self.required_3.setText(_translate("Dialog", "*"))
        self.label_6.setText(_translate("Dialog", "Линейные ограничения:"))
        self.toolButton_2.setText(_translate("Dialog", "-"))
        self.toolButton.setText(_translate("Dialog", "+"))
        self.required_4.setText(_translate("Dialog", "*"))
        self.label_7.setText(_translate("Dialog", "Осевые ограничения:"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p>x<span style=\" "
                                                  "vertical-align:sub;\">1</span> &ge; </p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p>x<span style=\" "
                                                  "vertical-align:sub;\">2</span> &ge; </p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "ОК"))


class Ui_NewConstraintDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(316, 135)
        Dialog.setMaximumSize(QtCore.QSize(316, 135))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.a1Coef = QtWidgets.QDoubleSpinBox(Dialog)
        self.a1Coef.setMaximum(1e4)
        self.a1Coef.setObjectName("a1Coef")
        self.horizontalLayout.addWidget(self.a1Coef)
        self.label_9 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.a2Coef = QtWidgets.QDoubleSpinBox(Dialog)
        self.a2Coef.setObjectName("a2Coef")
        self.a2Coef.setMaximum(1e4)
        self.horizontalLayout.addWidget(self.a2Coef)
        self.label_10 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.typeSelector = QtWidgets.QComboBox(Dialog)
        self.typeSelector.setObjectName("typeSelector")
        self.typeSelector.addItem("")
        self.typeSelector.addItem("")
        self.horizontalLayout.addWidget(self.typeSelector)
        self.constant = QtWidgets.QDoubleSpinBox(Dialog)
        self.constant.setMaximum(1e4)
        self.constant.setObjectName("constant")
        self.horizontalLayout.addWidget(self.constant)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Новое линейное ограничение"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p> &times; x<span style=\" "
                                                  "vertical-align:sub;\">1</span> + </p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p> &times; x<span style=\" "
                                                   "vertical-align:sub;\">2</span></p></body></html>"))
        self.typeSelector.setItemText(0, _translate("Dialog", ">="))
        self.typeSelector.setItemText(1, _translate("Dialog", "<="))
        self.pushButton.setText(_translate("Dialog", "ОК"))


class Ui_ExportDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 260)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setChecked(True)
        self.verticalLayout.addWidget(self.radioButton_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Экспорт задач"))
        self.label.setText(_translate("Dialog", "Путь к файлу:"))
        self.lineEdit.setText(_translate("Dialog", "tasks.csv"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.label_2.setText(_translate("Dialog", "Разделитель:"))
        self.lineEdit_2.setText(_translate("Dialog", ";"))
        self.label_3.setText(_translate("Dialog", "Опции:"))
        self.checkBox.setText(_translate("Dialog", "Первая строка таблицы - заголовок"))
        self.radioButton.setText(_translate("Dialog", "Экспортировать все задачи"))
        self.radioButton_2.setText(_translate("Dialog", "Экспортировать только выбранные"))


class Ui_AboutDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(458, 398)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.imageLabel = QtWidgets.QLabel(Dialog)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("label_8")
        self.verticalLayout.addWidget(self.imageLabel)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_13 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_15 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_6.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_17 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_7.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_7.addWidget(self.label_18)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_19 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_8.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_8.addWidget(self.label_20)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_21 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_9.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_9.addWidget(self.label_22)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "О программе"))
        self.label_3.setText(_translate("Dialog", "Графический метод решения задач линейного программирования для экономических задач"))
        self.label_2.setText(_translate("Dialog", "Список горячих клавиш:"))
        self.label_4.setText(_translate("Dialog", "Ctrl+O"))
        self.label_5.setText(_translate("Dialog", "Открыть файл"))
        self.label_6.setText(_translate("Dialog", "Ctrl+B"))
        self.label_7.setText(_translate("Dialog", "Загрузить базу примеров"))
        self.label_9.setText(_translate("Dialog", "Ctrl+N"))
        self.label_10.setText(_translate("Dialog", "Добавить задачу к текущей таблице"))
        self.label_11.setText(_translate("Dialog", "Alt+N"))
        self.label_12.setText(_translate("Dialog", "Ввести данные новой задачи и решить её"))
        self.label_13.setText(_translate("Dialog", "Ctrl+S"))
        self.label_14.setText(_translate("Dialog", "Сохранить изменения"))
        self.label_15.setText(_translate("Dialog", "Alt+S"))
        self.label_16.setText(_translate("Dialog", "Решить выбранную задачу"))
        self.label_17.setText(_translate("Dialog", "Delete"))
        self.label_18.setText(_translate("Dialog", "Удалить выбранные задачи"))
        self.label_19.setText(_translate("Dialog", "Ctrl+E"))
        self.label_20.setText(_translate("Dialog", "Экспорт задач в CSV"))
        self.label_21.setText(_translate("Dialog", "F1"))
        self.label_22.setText(_translate("Dialog", "Показать это окно"))
        self.label.setText(_translate("Dialog", "v0.1.0"))
