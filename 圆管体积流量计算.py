# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '圆管体积流量计算.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QMessageBox
import numpy as np
from PyQt5.QtGui import *
import sqlite3
import datetime
from sqlite3 import Error

#连接数据库
def sql_connection():
    try:
        # con = sqlite3.connect("圆管体积流量计算数据库.db")
        con = sqlite3.connect("公式集合数据库.db")
        return con
    except Error:
        print(Error)
#创建表
def sql_table(con):
    try:
        # 创建游标
        cursor = con.cursor()
        cursor.execute("create table 圆管体积流量 (日期,气体类型,气体动力粘度,圆管长度,压力差,圆管直径,圆管体积流量)")
        # 提交事务
        con.commit()
    except Error:
        print(Error)
con = sql_connection()
sql_table(con)

class Ui_yuanguantijiliuliang(QMainWindow):
    def setupUi(self, yuanguantijiliuliang):
        yuanguantijiliuliang.setObjectName("yuanguantijiliuliang")
        yuanguantijiliuliang.setWindowModality(QtCore.Qt.NonModal)
        yuanguantijiliuliang.setEnabled(True)
        yuanguantijiliuliang.resize(740, 500)
        yuanguantijiliuliang.setMaximumSize(QtCore.QSize(740, 500))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        yuanguantijiliuliang.setFont(font)
        yuanguantijiliuliang.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/PNG/chengliang.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        yuanguantijiliuliang.setWindowIcon(icon)
        yuanguantijiliuliang.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(yuanguantijiliuliang)
        self.label.setGeometry(QtCore.QRect(0, 20, 740, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(yuanguantijiliuliang)
        self.pushButton.setGeometry(QtCore.QRect(600, 430, 110, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(yuanguantijiliuliang)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 200, 330, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_2.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(yuanguantijiliuliang)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QtCore.QRect(340, 300, 330, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_4.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(yuanguantijiliuliang)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_5.setGeometry(QtCore.QRect(340, 350, 330, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_5.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_5.setClearButtonEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit = QtWidgets.QLineEdit(yuanguantijiliuliang)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(340, 150, 330, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(yuanguantijiliuliang)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 250, 330, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_3.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(yuanguantijiliuliang)
        self.label_4.setGeometry(QtCore.QRect(70, 195, 250, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(yuanguantijiliuliang)
        self.label_5.setGeometry(QtCore.QRect(70, 250, 250, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(yuanguantijiliuliang)
        self.label_6.setGeometry(QtCore.QRect(70, 300, 250, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(yuanguantijiliuliang)
        self.label_7.setGeometry(QtCore.QRect(70, 350, 250, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(yuanguantijiliuliang)
        self.label_3.setGeometry(QtCore.QRect(70, 150, 250, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(yuanguantijiliuliang)
        self.label_8.setGeometry(QtCore.QRect(20, 420, 561, 61))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        font.setKerning(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(yuanguantijiliuliang)
        self.label_9.setGeometry(QtCore.QRect(100, 90, 50, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.comboBox = QtWidgets.QComboBox(yuanguantijiliuliang)
        self.comboBox.setGeometry(QtCore.QRect(160, 90, 130, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox_2")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(yuanguantijiliuliang)
        QtCore.QMetaObject.connectSlotsByName(yuanguantijiliuliang)

        self.lineEdit_2.setText("0.019845")

        # 设置信号
        self.pushButton.clicked.connect(self.jisuan)
        self.comboBox.currentIndexChanged.connect(self.box)


        # 只允许输入数字
        self.lineEdit.setValidator(QDoubleValidator())
        self.lineEdit_2.setValidator(QDoubleValidator())
        self.lineEdit_3.setValidator(QDoubleValidator())
        self.lineEdit_4.setValidator(QDoubleValidator())
        self.lineEdit_5.setValidator(QDoubleValidator())

    def retranslateUi(self, yuanguantijiliuliang):
        _translate = QtCore.QCoreApplication.translate
        yuanguantijiliuliang.setWindowTitle(_translate("yuanguantijiliuliang", "圆管体积流量计算V1.1 By ChengLiang"))
        self.label.setText(_translate("yuanguantijiliuliang", "圆管体积流量计算"))
        self.pushButton.setText(_translate("yuanguantijiliuliang", "计算"))
        self.label_4.setText(_translate("yuanguantijiliuliang", "气体动力粘度μ（Pas）"))
        self.label_5.setText(_translate("yuanguantijiliuliang", "圆管长度l（m）"))
        self.label_6.setText(_translate("yuanguantijiliuliang", "压力差的△P（MPa）"))
        self.label_7.setText(_translate("yuanguantijiliuliang", "圆管直径d（mm）"))
        self.label_3.setText(_translate("yuanguantijiliuliang", "圆管体积流量Qv（L/s）"))
        self.label_8.setText(_translate("yuanguantijiliuliang", "Qv=d^4*Π△P/（128μl)"))
        self.label_9.setText(_translate("yuanguantijiliuliang", "气体"))
        self.comboBox.setItemText(0, _translate("yuanguantijiliuliang", "氦气"))
        self.comboBox.setItemText(1, _translate("yuanguantijiliuliang", "氩气"))
        self.comboBox.setItemText(2, _translate("yuanguantijiliuliang", "氢气"))
        self.comboBox.setItemText(3, _translate("yuanguantijiliuliang", "氧气"))
        self.comboBox.setItemText(4, _translate("yuanguantijiliuliang", "氮气"))
        self.comboBox.setItemText(5, _translate("yuanguantijiliuliang", "空气"))
        self.comboBox.setItemText(6, _translate("yuanguantijiliuliang", "二氧化碳"))

    #设置参数
    def canshu(self):
        global A, μ, l, P, d, Qv
        A = self.comboBox.currentText()
        μ = self.lineEdit_2.text()
        l = self.lineEdit_3.text()
        P = self.lineEdit_4.text()
        d = self.lineEdit_5.text()
        Qv=self.lineEdit.text()


    #气体选择
    def qitiniandu(self):
        self.canshu()
        if A == "氦气":
            self.lineEdit_2.setText("0.019845")
        if A == "氩气":
            self.lineEdit_2.setText("0.022624")
        if A == "氢气":
            self.lineEdit_2.setText("0.008915")
        if A == "氧气":
            self.lineEdit_2.setText("0.02055")
        if A == "氮气":
            self.lineEdit_2.setText("0.017825")
        if A == "空气":
            self.lineEdit_2.setText("0.018448")
        if A == "二氧化碳":
            self.lineEdit_2.setText("0.014932")

    def box(self):
        self.qitiniandu()
        self.jisuan()


    #创建计算
    def jisuan(self):
        self.canshu()
        global A, μ, l, P, d, Qv
        if μ==None or l==None or P==None or d==None or μ=="" or l=="" or P=="" or d=="" or \
                float(μ)<0 or float(l)<0 or float(P)<0 or float(d)<0:
            QMessageBox.information(None, "使用提示", "输入不完整或错误，请检查后重新输入！", QMessageBox.Ok)
            self.qitiniandu()
        else:
            μ = float(self.lineEdit_2.text())
            l = float(self.lineEdit_3.text())
            P = float(self.lineEdit_4.text())
            d = float(self.lineEdit_5.text())
            Qv = round((P * np.power(d, 4) * np.pi) / (128 * 1000 * μ * l), 10)
            self.lineEdit.setText(str(Qv))
            self.shuju()

    def datetime(self):
        global now_time
        now_time= datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")

    def shuju(self):
        self.datetime()
        def sql_insert(con, data):
                cursor = con.cursor()
                cursor.execute("insert into 圆管体积流量 (日期,气体类型,气体动力粘度,圆管长度,压力差,圆管直径,圆管体积流量) values(?,?,?,?,?,?,?)", data)
                con.commit()
        data = (now_time,A,μ,l,P,d,Qv)
        sql_insert(con, data)

import img_rc
import sys
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Mainwidow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_yuanguantijiliuliang()  # 创建QT设计的窗体
    ui.setupUi(Mainwidow)  # 初始化设置
    Mainwidow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程