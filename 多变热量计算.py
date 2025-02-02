# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '多变热量计算.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from PyQt5.QtGui import *
import numpy as np
import sqlite3
import datetime
from sqlite3 import Error

#连接数据库
def sql_connection():
    try:
        # con = sqlite3.connect("多变过程热量计算数据库.db")
        con = sqlite3.connect("公式集合数据库.db")
        return con
    except Error:
        print(Error)
#创建表
def sql_table(con):
    try:
        # 创建游标
        cursor = con.cursor()
        cursor.execute("create table 多变过程热量 (日期,多变过程热量Q,多变指数n,比定压热容Cp,比定容热容Cv,温度T1,温度T2) ")
        # 提交事务
        con.commit()
    except Error:
        print(Error)
con = sql_connection()
sql_table(con)

class Ui_duobianreliang(QMainWindow):
    def setupUi(self, duobianreliang):
        duobianreliang.setObjectName("duobianreliang")
        duobianreliang.setWindowModality(QtCore.Qt.NonModal)
        duobianreliang.setEnabled(True)
        duobianreliang.resize(620, 520)
        duobianreliang.setMaximumSize(QtCore.QSize(620, 520))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        duobianreliang.setFont(font)
        duobianreliang.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/PNG/chengliang.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        duobianreliang.setWindowIcon(icon)
        duobianreliang.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(duobianreliang)
        self.label.setGeometry(QtCore.QRect(0, 20, 620, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(duobianreliang)
        self.pushButton.setGeometry(QtCore.QRect(450, 420, 100, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(duobianreliang)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 120, 260, 40))
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
        self.lineEdit_4 = QtWidgets.QLineEdit(duobianreliang)
        self.lineEdit_4.setGeometry(QtCore.QRect(310, 220, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_4.setAccessibleName("")
        self.lineEdit_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_4.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit = QtWidgets.QLineEdit(duobianreliang)
        self.lineEdit.setGeometry(QtCore.QRect(310, 70, 260, 40))
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
        self.lineEdit_3 = QtWidgets.QLineEdit(duobianreliang)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 170, 260, 40))
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
        self.label_4 = QtWidgets.QLabel(duobianreliang)
        self.label_4.setGeometry(QtCore.QRect(35, 115, 265, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(duobianreliang)
        self.label_5.setGeometry(QtCore.QRect(40, 170, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(duobianreliang)
        self.label_6.setGeometry(QtCore.QRect(40, 220, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(duobianreliang)
        self.label_3.setGeometry(QtCore.QRect(35, 70, 265, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(duobianreliang)
        self.label_10.setGeometry(QtCore.QRect(30, 370, 391, 131))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setKerning(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.lineEdit_5 = QtWidgets.QLineEdit(duobianreliang)
        self.lineEdit_5.setGeometry(QtCore.QRect(310, 270, 260, 40))
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
        self.label_7 = QtWidgets.QLabel(duobianreliang)
        self.label_7.setGeometry(QtCore.QRect(40, 270, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(duobianreliang)
        self.lineEdit_6.setGeometry(QtCore.QRect(310, 320, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_6.setAccessibleName("")
        self.lineEdit_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_6.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_6.setReadOnly(False)
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setClearButtonEnabled(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(duobianreliang)
        self.label_8.setGeometry(QtCore.QRect(40, 320, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(duobianreliang)
        QtCore.QMetaObject.connectSlotsByName(duobianreliang)

        self.pushButton.clicked.connect(self.jisuan)

        # 只允许输入数字
        self.lineEdit.setValidator(QDoubleValidator())
        self.lineEdit_2.setValidator(QDoubleValidator())
        self.lineEdit_3.setValidator(QDoubleValidator())
        self.lineEdit_4.setValidator(QDoubleValidator())
        self.lineEdit_5.setValidator(QDoubleValidator())
        self.lineEdit_6.setValidator(QDoubleValidator())

    def jisuan(self):
        global Q,n,Cp,Cv,T1,T2
        T0 = 273.15
        n = self.lineEdit_2.text()
        Cp = self.lineEdit_3.text()
        Cv = self.lineEdit_4.text()
        T1 = self.lineEdit_5.text()
        T2 = self.lineEdit_6.text()
        if n==None or Cp==None or Cv==None or T1==None or T2==None or \
                n == "" or Cp == "" or Cv == "" or T1 == "" or T2 == "":
            QMessageBox.information(None, "提示说明", "输入不完整或错误，请检查后重新输入！", QMessageBox.Ok)
        else:
            n=float(self.lineEdit_2.text())
            Cp = float(self.lineEdit_3.text())
            Cv = float(self.lineEdit_4.text())
            T1 = float(self.lineEdit_5.text()) + T0
            T2 = float(self.lineEdit_6.text()) + T0
            Q = round((Cv - Cp) * (T2 - T1) / (n - 1), 5)
            self.lineEdit.setText(str(Q))
            self.shuju()

    def datetime(self):
        global now_time
        now_time= datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")

    def shuju(self):
        self.datetime()
        def sql_insert(con, data):
            cursor = con.cursor()
            cursor.execute("insert into 多变过程热量 (日期,多变过程热量Q,多变指数n,比定压热容Cp,比定容热容Cv,温度T1,温度T2) values(?,?,?,?,?,?,?)",
                           data)
            con.commit()
        data = (now_time,Q,n,Cp,Cv,T1,T2)
        sql_insert(con, data)

    def retranslateUi(self, duobianreliang):
        _translate = QtCore.QCoreApplication.translate
        duobianreliang.setWindowTitle(_translate("duobianreliang", "多变过程热量计算V1.1 By ChengLiang"))
        self.label.setText(_translate("duobianreliang", "多变过程热量计算"))
        self.pushButton.setText(_translate("duobianreliang", "计算"))
        self.label_4.setText(_translate("duobianreliang", "多变指数n "))
        self.label_5.setText(_translate("duobianreliang", "比定压热容Cp（J/kgK）"))
        self.label_6.setText(_translate("duobianreliang", "比定容热容Cv（J/kgK）"))
        self.label_3.setText(_translate("duobianreliang", "多变过程热量Q（J/kg）"))
        self.label_10.setText(_translate("duobianreliang", "<html><head/><body><p align=\"center\">Q=(C<span style=\" vertical-align:sub;\">v</span>-C<span style=\" vertical-align:sub;\">p)</span>(T<span style=\" vertical-align:sub;\">2</span>-T<span style=\" vertical-align:sub;\">1</span>)/(n-1)</p><p align=\"center\">n=±∞：定容过程 n=0：定压过程</p><p align=\"center\">n=k：定熵过程 n=1：定温过程</p><p align=\"center\">n=其他数值：多变过程</p></body></html>"))
        self.label_7.setText(_translate("duobianreliang", "温度T1（℃）"))
        self.label_8.setText(_translate("duobianreliang", "温度T2（℃）"))
import img_rc
import sys
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Mainwidow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_duobianreliang()  # 创建QT设计的窗体
    ui.setupUi(Mainwidow)  # 初始化设置
    Mainwidow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程