# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '热力学能焓等熵指数计算.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from PyQt5.QtGui import *
import sqlite3
import datetime
from sqlite3 import Error

#连接数据库
def sql_connection():
    try:
        # con = sqlite3.connect("热力学能焓等熵指数计算数据库.db")
        con = sqlite3.connect("公式集合数据库.db")
        return con
    except Error:
        print(Error)
#创建表
def sql_table(con):
    try:
        # 创建游标
        cursor = con.cursor()
        cursor.execute("create table 热力学能焓等熵指数 (日期,比热力学能u,温度T,比定容热容Cv,比焓h,比定压热容Cp,等熵指数k)")
        # 提交事务
        con.commit()
    except Error:
        print(Error)
con = sql_connection()
sql_table(con)

class Ui_relixuenenghanshang(QMainWindow):
    def setupUi(self, relixuenenghanshang):
        relixuenenghanshang.setObjectName("relixuenenghanshang")
        relixuenenghanshang.setWindowModality(QtCore.Qt.NonModal)
        relixuenenghanshang.setEnabled(True)
        relixuenenghanshang.resize(620, 500)
        relixuenenghanshang.setMaximumSize(QtCore.QSize(620, 500))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        relixuenenghanshang.setFont(font)
        relixuenenghanshang.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/PNG/chengliang.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        relixuenenghanshang.setWindowIcon(icon)
        relixuenenghanshang.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(relixuenenghanshang)
        self.label.setGeometry(QtCore.QRect(0, 20, 620, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(relixuenenghanshang)
        self.pushButton.setGeometry(QtCore.QRect(380, 440, 100, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(relixuenenghanshang)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 180, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_2.setAccessibleName("")
        self.lineEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_2.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(relixuenenghanshang)
        self.lineEdit_4.setGeometry(QtCore.QRect(320, 280, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_4.setAccessibleName("")
        self.lineEdit_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit = QtWidgets.QLineEdit(relixuenenghanshang)
        self.lineEdit.setGeometry(QtCore.QRect(320, 130, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit.setAccessibleName("")
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(relixuenenghanshang)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 230, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_3.setAccessibleName("")
        self.lineEdit_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_3.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(relixuenenghanshang)
        self.label_4.setGeometry(QtCore.QRect(40, 175, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(relixuenenghanshang)
        self.label_5.setGeometry(QtCore.QRect(40, 230, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(relixuenenghanshang)
        self.label_6.setGeometry(QtCore.QRect(40, 280, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(relixuenenghanshang)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(relixuenenghanshang)
        self.label_10.setGeometry(QtCore.QRect(40, 440, 250, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.checkBox = QtWidgets.QCheckBox(relixuenenghanshang)
        self.checkBox.setGeometry(QtCore.QRect(90, 75, 150, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(relixuenenghanshang)
        self.checkBox_2.setGeometry(QtCore.QRect(270, 75, 80, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(relixuenenghanshang)
        self.lineEdit_5.setGeometry(QtCore.QRect(320, 330, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_5.setAccessibleName("")
        self.lineEdit_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_5.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_5.setReadOnly(False)
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setClearButtonEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(relixuenenghanshang)
        self.label_7.setGeometry(QtCore.QRect(40, 330, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(relixuenenghanshang)
        self.lineEdit_6.setGeometry(QtCore.QRect(320, 380, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_6.setAccessibleName("")
        self.lineEdit_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_6.setReadOnly(False)
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setClearButtonEnabled(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(relixuenenghanshang)
        self.label_8.setGeometry(QtCore.QRect(40, 380, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.checkBox_3 = QtWidgets.QCheckBox(relixuenenghanshang)
        self.checkBox_3.setGeometry(QtCore.QRect(390, 75, 130, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")

        self.retranslateUi(relixuenenghanshang)
        QtCore.QMetaObject.connectSlotsByName(relixuenenghanshang)

        # 只允许输入数字
        self.lineEdit.setValidator(QDoubleValidator())
        self.lineEdit_2.setValidator(QDoubleValidator())
        self.lineEdit_3.setValidator(QDoubleValidator())
        self.lineEdit_4.setValidator(QDoubleValidator())
        self.lineEdit_5.setValidator(QDoubleValidator())
        self.lineEdit_6.setValidator(QDoubleValidator())

        self.pushButton.clicked.connect(self.jisuan)
        self.checkBox.clicked.connect(self.xuanze)
        self.checkBox_2.clicked.connect(self.xuanze)
        self.checkBox_3.clicked.connect(self.xuanze)

    def xuanze(self):
        if self.checkBox.isChecked() == False:
            self.lineEdit.clear()
        if self.checkBox_2.isChecked()== False:
            self.lineEdit_4.clear()
        if self.checkBox_3.isChecked()== False:
            self.lineEdit_6.clear()
        if self.checkBox.isChecked() == False and self.checkBox_2.isChecked() == False and self.checkBox_3.isChecked() == False:
            QMessageBox.information(None, "使用提示", "必须选择一项！", QMessageBox.Ok)


    def jisuan(self):
        T0 = 273.15
        T=self.lineEdit_2.text()
        Cv=self.lineEdit_3.text()
        Cp = self.lineEdit_5.text()
        if self.checkBox.isChecked()==True:
            if T==None or Cv==None or T =="" or Cv =="" or  float(T)<0 or float(Cv)<0:
                QMessageBox.information(None, "提示说明", "请输入正确的温度T和比定容热容Cv！", QMessageBox.Ok)
            else:
                T=T0+float(T)
                u=float(Cv)*T
                self.lineEdit.setText(str(u))
        if self.checkBox_2.isChecked()==True:
                if T == None or Cp == None or T == "" or Cp == "" or float(T) < 0 or float(Cp) < 0:
                    QMessageBox.information(None, "提示说明", "请输入正确的温度T和比定压热容Cp！", QMessageBox.Ok)
                else:
                    T = T0 + float(T)
                    h = float(Cp) * T
                    self.lineEdit_4.setText(str(h))
        if self.checkBox_3.isChecked()==True:
            if Cv==None or Cp==None or Cv =="" or Cp =="" or  float(Cv)<0 or float(Cp)<0:
                QMessageBox.information(None, "提示说明", "请输入正确的比定容热容Cv和比定压热容Cp！", QMessageBox.Ok)
            else:
                k=float(Cp)/float(Cv)
                self.lineEdit_6.setText(str(k))
        self.shuju()

    def datetime(self):
        global now_time
        now_time= datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")

    def shuju(self):
        self.datetime()
        u=self.lineEdit.text()
        T = self.lineEdit_2.text()
        Cv = self.lineEdit_3.text()
        h= self.lineEdit_4.text()
        Cp = self.lineEdit_5.text()
        k=self.lineEdit_6.text()
        def sql_insert(con, data):
            cursor = con.cursor()
            cursor.execute("insert into 热力学能焓等熵指数 (日期,比热力学能u,温度T,比定容热容Cv,比焓h,比定压热容Cp,等熵指数k) values(?,?,?,?,?,?,?)",
                           data)
            con.commit()
        data = (now_time,u,T,Cv,h,Cp,k)
        sql_insert(con, data)


    def retranslateUi(self, relixuenenghanshang):
        _translate = QtCore.QCoreApplication.translate
        relixuenenghanshang.setWindowTitle(_translate("relixuenenghanshang", "热力学能、焓、等熵指数计算V1.1 By ChengLiang"))
        self.label.setText(_translate("relixuenenghanshang", "热力学能、焓、等熵指数计算"))
        self.pushButton.setText(_translate("relixuenenghanshang", "计算"))
        self.label_4.setText(_translate("relixuenenghanshang", "温度T（℃）"))
        self.label_5.setText(_translate("relixuenenghanshang", "比定容热容Cv（J/kgK）"))
        self.label_6.setText(_translate("relixuenenghanshang", "比焓h（J/kg）"))
        self.label_3.setText(_translate("relixuenenghanshang", "比热力学能u（J/kg）"))
        self.label_10.setText(_translate("relixuenenghanshang", "<html><head/><body><p align=\"center\">u=C<span style=\" vertical-align:sub;\">v</span>T h=C<span style=\" vertical-align:sub;\">p</span>T k=C<span style=\" vertical-align:sub;\">p</span>/C<span style=\" vertical-align:sub;\">v</span></p></body></html>"))
        self.checkBox.setText(_translate("relixuenenghanshang", "求比热力学能"))
        self.checkBox_2.setText(_translate("relixuenenghanshang", "求比焓"))
        self.label_7.setText(_translate("relixuenenghanshang", "比定压热容Cp（J/kgK）"))
        self.label_8.setText(_translate("relixuenenghanshang", "等熵指数k"))
        self.checkBox_3.setText(_translate("relixuenenghanshang", "求等熵指数"))
import img_rc
import sys
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Mainwidow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_relixuenenghanshang()  # 创建QT设计的窗体
    ui.setupUi(Mainwidow)  # 初始化设置
    Mainwidow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程