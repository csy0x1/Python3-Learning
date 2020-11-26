from Ui_untitled import *
from Ui_create import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
import sys

class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_Main_Menu()
        self.main_ui.setupUi(self)

class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog()
        self.child.setupUi(self)


if __name__=='__main__':

    app=QApplication(sys.argv)
    window=parentWindow()
    child=childWindow()

    #通过toolButton将两个窗体关联
    btn=window.main_ui.pushButton_2
    btn.clicked.connect(child.show)

    # 显示
    window.show()
    sys.exit(app.exec_())