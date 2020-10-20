from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from views import Ui_SolveViewer
import numpy as np
import sys


class SolveViewer(QMainWindow, Ui_SolveViewer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.plotter.plot(
            y=3 + np.random.normal(size=50), brush=self.plotter.brush, fillLevel=0,
            name='<p style="font-size: 12pt; font-family:Georgia, \'Times New Roman\', Times, serif">x &ge; y</p>'
        )
        self.plotter.plotItem.vb.setLimits(xMin=-1, xMax=51, yMin=-1, yMax=10)
        self.action_4.triggered.connect(self.saveImage)

    def saveImage(self):
        file_name, ok = QFileDialog.getSaveFileName(self, 'Сохранить отчёт',
                                                    'Решение.png', 'Images (*.png *.jpg *.tiff)')
        if ok:
            self.plotter.save(file_name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SolveViewer()
    ex.show()
    sys.exit(app.exec())