from Ui_modify2 import Ui_Modify2_Form
from Ui_modify1 import Ui_Modify1
from Ui_search import Ui_Search, Ui_Search
from database import Insert_Info, Modify, Search_All, Search_Info
from Ui_menu import *
from Ui_create import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog, QMessageBox, QTableWidgetItem, QWidget
import sys
import prettytable

class MainWindow(QMainWindow):  #主窗口
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui= Ui_Main_Menu()
        self.main_ui.setupUi(self)
        #btn=self.main_ui.pushButton_2
        self.main_ui.pushButton_2.clicked.connect(self.CreateForm) #录入信息按钮
        self.main_ui.pushButton_3.clicked.connect(self.SearchForm) #搜索信息按钮
        self.main_ui.pushButton.clicked.connect(self.Modify1Form)  #修改信息按钮

    def CreateForm(self):    #跳转到创建窗口，隐藏主窗口
        self.crea=CreateWindow()
        self.crea.show()
        self.close()
    
    def SearchForm(self):
        self.search=SearchWindow()
        self.search.show()
        self.close()

    def Modify1Form(self):
        self.modify1=ModifyWindow1()
        self.modify1.show()
        self.close()

class CreateWindow(QDialog):    #录入信息窗口
    def __init__(self):
        QDialog.__init__(self)
        self.create_ui=Ui_Dialog()
        self.create_ui.setupUi(self)
        self.create_ui.pushButton.clicked.connect(self.MainW)
        self.create_ui.pushButton_2.clicked.connect(self.submit)
        self.Teacher={}

    def MainW(self):    #返回主界面
        self.main=MainWindow()
        self.main.show()
        self.close()

    def submit(self):   #提交
        self.Teacher['工号']=self.create_ui.lineEdit.text()
        self.Teacher['姓名']=self.create_ui.lineEdit_2.text()
        self.Teacher['年龄']=self.create_ui.lineEdit_3.text()
        self.Teacher['职称']=self.create_ui.lineEdit_4.text()
        self.Teacher['系名']=self.create_ui.lineEdit_5.text()
        self.Teacher['手机号码']=self.create_ui.lineEdit_6.text()
        self.Teacher['联系地址']=self.create_ui.lineEdit_7.text()
        table=prettytable.PrettyTable()     #创建表格
        table.field_names=['信息','\t内容']   #设置表头
        table.border=False
        for key,value in self.Teacher.items():
            table.add_row([key,"\t"+value])
        info=table.get_string(title='\t教师信息\t')
        code=QMessageBox.question(self,"确认","请确认信息输入正确\n"+info,QMessageBox.Yes | QMessageBox.No)
        if code == 65536:   #选否
            pass
        else:   #选是
            if(Insert_Info(self.Teacher)!=False):
                code=QMessageBox.information(self, '成功','操作成功',QMessageBox.Yes)
                self.MainW()
            else:
                code=QMessageBox.critical(self,"错误","操作失败",QMessageBox.Yes)
                self.MainW()

class SearchWindow(QWidget):    #搜索信息窗口
    def __init__(self):
        QWidget.__init__(self)
        self.search_ui=Ui_Search()
        self.search_ui.setupUi(self)
        self.search_ui.pushButton.clicked.connect(self.MainW)
        self.row,self.table=Search_All()
        self.search_ui.tableWidget.setColumnCount(9)
        self.search_ui.tableWidget.setRowCount(self.row)
        self.data()


    def MainW(self):    #返回主界面
        self.main=MainWindow()
        self.main.show()
        self.close()

    def data(self):   #填充数据
        for i in range(self.row):
            for j in range(9):
                temp_data=self.table[i][j]
                data=QTableWidgetItem(str(temp_data))
                self.search_ui.tableWidget.setItem(i,j,data)

class ModifyWindow1(QWidget):   #展示可供修改的信息窗口
    def __init__(self):
        QWidget.__init__(self)
        self.modify1_ui=Ui_Modify1()
        self.modify1_ui.setupUi(self)
        self.modify1_ui.pushButton_2.clicked.connect(self.modify_data)  #确认按钮
        self.modify1_ui.pushButton.clicked.connect(self.MainW)  #返回按钮
        self.row,self.table=Search_All()
        self.modify1_ui.tableWidget.setColumnCount(9)
        self.modify1_ui.tableWidget.setRowCount(self.row)
        self.data()

    def modify_data(self):
        if(self.modify1_ui.tableWidget.selectedItems):
            row_index=self.modify1_ui.tableWidget.currentIndex().row()
            id=self.modify1_ui.tableWidget.item(row_index,0).text()
            #QMessageBox.information(self,"test",id,QMessageBox.Yes)
            rows=Search_Info('ID',id)
            self.Modify2(rows)

    def data(self):   #填充数据
        for i in range(self.row):
            for j in range(9):
                temp_data=self.table[i][j]
                data=QTableWidgetItem(str(temp_data))
                self.modify1_ui.tableWidget.setItem(i,j,data)

    def MainW(self):    #返回主界面
        self.main=MainWindow()
        self.main.show()
        self.close()

    def Modify2(self,rows): #进入编辑窗口
        self.modify2_ui=ModifyWindow2(rows)
        self.modify2_ui.show()
        self.close()

class ModifyWindow2(QWidget):   #信息编辑窗口
    def __init__(self,rows):
        QWidget.__init__(self)
        self.modify2_ui=Ui_Modify2_Form()
        self.modify2_ui.setupUi(self)
        self.get_data(rows)
        self.modify2_ui.pushButton.clicked.connect(self.Modify1)    #返回
        self.modify2_ui.pushButton_2.clicked.connect(self.store_data)

    def get_data(self,rows):    #将获取的信息预写入文本编辑框
        self.modify2_ui.lineEdit.setText(rows[0][0])    #工号
        self.modify2_ui.lineEdit_2.setText(rows[0][1])  #姓名
        self.modify2_ui.lineEdit_3.setText(str(rows[0][2])) #年龄
        self.modify2_ui.lineEdit_4.setText(rows[0][3])  #职称
        self.modify2_ui.lineEdit_5.setText(rows[0][4])  #所在系
        self.modify2_ui.lineEdit_6.setText(rows[0][6])  #手机号码
        self.modify2_ui.lineEdit_7.setText(rows[0][7])  #联系地址

    def Modify1(self):
        self.modify1_ui=ModifyWindow1()
        self.modify1_ui.show()
        self.close()

    def MainW(self):    #返回主界面
        self.main=MainWindow()
        self.main.show()
        self.close()
        
    def store_data(self):
        data=[]
        lineedit=self.modify2_ui.__dict__
        for i in range(7):  #动态设置变量名，获取所有输入框内的数据
            if(i == 0):
                data.append(lineedit['lineEdit'].text())
                continue
            data.append(lineedit['lineEdit_'+str(i+1)].text())
        if(Modify(data)):
            code=QMessageBox.information(self,'成功','操作成功',QMessageBox.Ok)
            if(code):
                self.MainW()
        else:
            QMessageBox.critical(self,'失败','操作失败',QMessageBox.Ok)

        #print(data)

if __name__ == '__main__':   
    app=QApplication(sys.argv)
    mainW=MainWindow()
    mainW.show()
    sys.exit(app.exec_())
