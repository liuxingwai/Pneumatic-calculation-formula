# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '打开数据库.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog,QMessageBox
import pandas as pd
import pandas.io.sql as sql
import sqlite3
import os


class Ui_opensqlite(QMainWindow):
    def setupUi(self, opensqlite):
        opensqlite.setObjectName("opensqlite")
        opensqlite.resize(940, 940)
        opensqlite.setMaximumSize(QtCore.QSize(940, 940))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        opensqlite.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/PNG/chengliang.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        opensqlite.setWindowIcon(icon)
        opensqlite.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_2 = QtWidgets.QLabel(opensqlite)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 100, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(opensqlite)
        self.lineEdit.setGeometry(QtCore.QRect(130, 20, 740, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(opensqlite)
        self.pushButton_2.setGeometry(QtCore.QRect(880, 20, 30, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(opensqlite)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 100, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(opensqlite)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 70, 740, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(opensqlite)
        self.pushButton_3.setGeometry(QtCore.QRect(880, 70, 30, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser = QtWidgets.QTextBrowser(opensqlite)
        self.textBrowser.setGeometry(QtCore.QRect(20, 110, 890, 200))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(opensqlite)
        self.textEdit.setGeometry(QtCore.QRect(20, 320, 890, 600))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(opensqlite)
        QtCore.QMetaObject.connectSlotsByName(opensqlite)

        self.pushButton_2.clicked.connect(self.filename)
        self.pushButton_3.clicked.connect(self.cun)
        self.lineEdit.textChanged.connect(self.sqlite)
        self.lineEdit_2.textEdited.connect(self.tables)

    def filename(self):
        global FileName,tables,con
        FileName=QFileDialog.getOpenFileName(None,"选择数据库文件",".","*.db")#选取文件名
        FileName = ''.join(str(i) for i in FileName[0]) #获取文件名
        self.lineEdit.clear()
        self.lineEdit.setText(str(FileName))

    def sqlite(self):
        global FileName,tables,con
        con = sqlite3.connect(FileName)
        # 列出所有表
        cursorObj = con.cursor()
        cursorObj.execute('SELECT name from sqlite_master where type= "table"')
        tables = cursorObj.fetchall()
        l = len(tables)
        tables = ','.join(str(i) for i in tables)
        self.textBrowser.setText("共有"+ str(l) +"个数据表"+"\n" + str(tables))

    def tables(self):
        # 查询数据表的数据
        global FileName,tables,con,rows,table_name
        table_name = self.lineEdit_2.text()
        if table_name=="" or table_name==None:
           QMessageBox.information(None, "使用提示", "请输入数据表！", QMessageBox.Ok)
        if table_name in tables:
            rows = sql.read_sql('select * from ' + table_name + ';', con)
            # pd.set_option('display.unicode.ambiguous_as_wide', True) #设置DataFrame输出对齐
            pd.set_option('display.unicode.east_asian_width', True)#设置DataFrame输出对齐
            rows=pd.DataFrame(rows)
            self.textEdit.setPlainText(str(rows))
        else:
            QMessageBox.information(None, "使用提示", "输入的数据表不存在，请重新输入！", QMessageBox.Ok)

    def cun(self):
        if self.lineEdit_2.text():
            A=self.lineEdit_2.text()
            QMessageBox.information(None, "使用提示", "请选择数据要保存的文件夹地址，不能直接放在盘符下！", QMessageBox.Ok)
            folderpath=QFileDialog.getExistingDirectory() #选取文件夹
            B= folderpath+"/" + A + ".xls"
            rows.to_excel(B)
            os.startfile(B)#打开文件
        else:
            QMessageBox.information(None, "使用提示", "请选择数据表！", QMessageBox.Ok)

    def retranslateUi(self, opensqlite):
        _translate = QtCore.QCoreApplication.translate
        opensqlite.setWindowTitle(_translate("opensqlite", "查看计算数据V1.0.1 By ChengLiang"))
        self.label_2.setText(_translate("opensqlite", "数据库"))
        self.lineEdit.setPlaceholderText(_translate("opensqlite", "请选择数据库"))
        self.pushButton_2.setText(_translate("opensqlite", "…"))
        self.label_3.setText(_translate("opensqlite", "数据表"))
        self.lineEdit_2.setPlaceholderText(_translate("opensqlite", "请填写数据表"))
        self.pushButton_3.setText(_translate("opensqlite", "存"))
        self.textBrowser.setHtml(_translate("opensqlite", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'楷体\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit.setHtml(_translate("opensqlite", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'楷体\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p></body></html>"))
import img_rc
import sys
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Mainwidow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_opensqlite()  # 创建QT设计的窗体
    ui.setupUi(Mainwidow)  # 初始化设置
    Mainwidow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程