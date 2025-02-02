# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '定容积放气公式.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QMessageBox
import numpy as np
from sympy import *
from PyQt5.QtGui import *
import sqlite3
import datetime
from sqlite3 import Error

#连接数据库
def sql_connection():
    try:
        # con = sqlite3.connect("定容放气计算数据库.db")
        con = sqlite3.connect("公式集合数据库.db")
        return con
    except Error:
        print(Error)
#创建表
def sql_table(con):
    try:
        # 创建游标
        cursor = con.cursor()
        cursor.execute("create table 定容放气 (日期,气体类型,孔直径D,孔面积S,容器容积V,等熵指数κ,气源温度Ts,容器内气体的初始压力P1,放气临界压力P,放气至压力P2,充气时间t)")
        # 提交事务
        con.commit()
    except Error:
        print(Error)
con = sql_connection()
sql_table(con)

class Ui_dingrongfangqi(QMainWindow):
    def setupUi(self, dingrongfangqi):
        dingrongfangqi.setObjectName("dingrongfangqi")
        dingrongfangqi.setWindowModality(QtCore.Qt.NonModal)
        dingrongfangqi.setEnabled(True)
        dingrongfangqi.resize(740, 650)
        dingrongfangqi.setMaximumSize(QtCore.QSize(740, 650))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        dingrongfangqi.setFont(font)
        dingrongfangqi.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/PNG/chengliang.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dingrongfangqi.setWindowIcon(icon)
        dingrongfangqi.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(dingrongfangqi)
        self.label.setGeometry(QtCore.QRect(0, 20, 740, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(dingrongfangqi)
        self.pushButton.setGeometry(QtCore.QRect(650, 580, 60, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_9 = QtWidgets.QLabel(dingrongfangqi)
        self.label_9.setGeometry(QtCore.QRect(21, 460, 350, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(dingrongfangqi)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 210, 330, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.radioButton = QtWidgets.QRadioButton(dingrongfangqi)
        self.radioButton.setGeometry(QtCore.QRect(330, 75, 120, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(dingrongfangqi)
        self.radioButton_2.setGeometry(QtCore.QRect(470, 75, 100, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(dingrongfangqi)
        self.radioButton_3.setGeometry(QtCore.QRect(590, 75, 120, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(dingrongfangqi)
        self.radioButton_4.setGeometry(QtCore.QRect(390, 115, 120, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(dingrongfangqi)
        self.radioButton_5.setGeometry(QtCore.QRect(540, 115, 140, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.label_10 = QtWidgets.QLabel(dingrongfangqi)
        self.label_10.setGeometry(QtCore.QRect(20, 510, 350, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.lineEdit_8 = QtWidgets.QLineEdit(dingrongfangqi)
        self.lineEdit_8.setEnabled(True)
        self.lineEdit_8.setGeometry(QtCore.QRect(379, 510, 330, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_8.setClearButtonEnabled(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_2 = QtWidgets.QLabel(dingrongfangqi)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 140, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(dingrongfangqi)
        self.comboBox.setGeometry(QtCore.QRect(180, 100, 130, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_7 = QtWidgets.QLineEdit(dingrongfangqi)
        self.lineEdit_7.setEnabled(True)
        self.lineEdit_7.setGeometry(QtCore.QRect(380, 460, 330, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_7.setClearButtonEnabled(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(dingrongfangqi)
        self.lineEdit_4.setGeometry(QtCore.QRect(380, 310, 330, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(dingrongfangqi)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_5.setGeometry(QtCore.QRect(380, 360, 330, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(dingrongfangqi)
        self.lineEdit_6.setGeometry(QtCore.QRect(380, 410, 330, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_6.setClearButtonEnabled(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setEnabled(False)
        self.lineEdit = QtWidgets.QLineEdit(dingrongfangqi)
        self.lineEdit.setGeometry(QtCore.QRect(380, 160, 330, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(dingrongfangqi)
        self.lineEdit_3.setGeometry(QtCore.QRect(380, 260, 330, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setKerning(True)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText("1.666")
        self.label_8 = QtWidgets.QLabel(dingrongfangqi)
        self.label_8.setGeometry(QtCore.QRect(21, 405, 350, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(dingrongfangqi)
        self.label_4.setGeometry(QtCore.QRect(21, 205, 350, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(dingrongfangqi)
        self.label_5.setGeometry(QtCore.QRect(21, 260, 350, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(dingrongfangqi)
        self.label_6.setGeometry(QtCore.QRect(21, 310, 350, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(dingrongfangqi)
        self.label_7.setGeometry(QtCore.QRect(21, 360, 350, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(dingrongfangqi)
        self.label_3.setGeometry(QtCore.QRect(21, 160, 350, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_11 = QtWidgets.QLabel(dingrongfangqi)
        self.label_11.setGeometry(QtCore.QRect(10, 560, 630, 80))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setKerning(True)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.label_11.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")

        self.retranslateUi(dingrongfangqi)
        QtCore.QMetaObject.connectSlotsByName(dingrongfangqi)

        self.radioButton.setChecked(True)
        self.lineEdit_5.setClearButtonEnabled(True)

        self.lineEdit.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.lineEdit_2.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.lineEdit_3.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.lineEdit_4.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.lineEdit_5.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.lineEdit_7.setStyleSheet("background-color: rgb(85, 255, 255);")

        # 设置信号
        self.pushButton.clicked.connect(self.jisuan)
        self.radioButton.toggled.connect(self.cleck)
        self.radioButton_2.toggled.connect(self.cleck)
        self.radioButton_3.toggled.connect(self.cleck)
        self.radioButton_4.toggled.connect(self.cleck)
        self.radioButton_5.toggled.connect(self.cleck)
        self.comboBox.currentIndexChanged.connect(self.box)

        # 只允许输入数字
        self.lineEdit.setValidator(QDoubleValidator())
        self.lineEdit_2.setValidator(QDoubleValidator())
        self.lineEdit_3.setValidator(QDoubleValidator())
        self.lineEdit_4.setValidator(QDoubleValidator())
        self.lineEdit_5.setValidator(QDoubleValidator())
        self.lineEdit_6.setValidator(QDoubleValidator())
        self.lineEdit_7.setValidator(QDoubleValidator())
        self.lineEdit_8.setValidator(QDoubleValidator())

    def retranslateUi(self, dingrongfangqi):
        _translate = QtCore.QCoreApplication.translate
        dingrongfangqi.setWindowTitle(_translate("dingrongfangqi", "定容放气计算V1.2 By ChengLiang"))
        self.label.setText(_translate("dingrongfangqi", "定容放气计算"))
        self.pushButton.setText(_translate("dingrongfangqi", "计算"))
        self.label_9.setText(_translate("dingrongfangqi", "放气至压力P2（MPa）"))
        self.radioButton.setText(_translate("dingrongfangqi", "求放气时间"))
        self.radioButton_2.setText(_translate("dingrongfangqi", "求孔直径"))
        self.radioButton_3.setText(_translate("dingrongfangqi", "求容器容积"))
        self.radioButton_4.setText(_translate("dingrongfangqi", "求初始压力"))
        self.radioButton_5.setText(_translate("dingrongfangqi", "求放气至压力"))
        self.label_10.setText(_translate("dingrongfangqi", "放气时间t（s）"))
        self.label_2.setText(_translate("dingrongfangqi", "气体等熵指数"))
        self.comboBox.setItemText(0, _translate("dingrongfangqi", "氦气"))
        self.comboBox.setItemText(1, _translate("dingrongfangqi", "氩气"))
        self.comboBox.setItemText(2, _translate("dingrongfangqi", "氢气"))
        self.comboBox.setItemText(3, _translate("dingrongfangqi", "氧气"))
        self.comboBox.setItemText(4, _translate("dingrongfangqi", "氮气"))
        self.comboBox.setItemText(5, _translate("dingrongfangqi", "空气"))
        self.comboBox.setItemText(6, _translate("dingrongfangqi", "二氧化碳"))
        self.label_8.setText(_translate("dingrongfangqi", "放气临界压力P*（MPa）"))
        self.label_4.setText(_translate("dingrongfangqi", "容器容积V（L）"))
        self.label_5.setText(_translate("dingrongfangqi", "等熵指数κ"))
        self.label_6.setText(_translate("dingrongfangqi", "气源温度Ts（℃）"))
        self.label_7.setText(_translate("dingrongfangqi", "容器内气体的初始压力P1（MPa）"))
        self.label_3.setText(_translate("dingrongfangqi", "孔直径D（mm）"))
        self.label_11.setText(
            _translate("dingrongchongqi", "时间t=(5.217*V/(κ*S)*(273.16/(273+Ts))^0.5)*(2*κ*((P1/Ps)^""<br>""((κ-1)/(2*κ))-1)/(κ-1)+0.945*(P1/P2)^((κ-1)/(2*κ)))"))

    # 创建选择
    def cleck(self):
        self.lineEdit_6.clear()
        if self.radioButton.isChecked():
            self.lineEdit.setStyleSheet("background-color: rgb(85, 255, 255);")
            self.lineEdit_2.setStyleSheet("background-color: rgb(85, 255, 255);")
            self.lineEdit_5.setStyleSheet("background-color: rgb(85, 255, 255);")
            self.lineEdit_7.setStyleSheet("background-color: rgb(85, 255, 255) ;")
            self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255) ;")
            self.lineEdit_8.clear()
        elif self.radioButton_2.isChecked():
            self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.lineEdit_2.setStyleSheet("background-color: rgb(85, 255, 255);")
            self.lineEdit_5.setStyleSheet("background-color: rgb(85, 255, 255);")
            self.lineEdit_7.setStyleSheet("background-color: rgb(85, 255, 255);")
            self.lineEdit_8.setStyleSheet("background-color: rgb(85, 255, 255) ;")
            self.lineEdit.clear()
        elif self.radioButton_3.isChecked():
            self.lineEdit.setStyleSheet("background-color: rgb(85, 255, 255);")
            self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.lineEdit_5.setStyleSheet("background-color: rgb(85, 255, 255);")
            self.lineEdit_7.setStyleSheet("background-color: rgb(85, 255, 255);")
            self.lineEdit_8.setStyleSheet("background-color: rgb(85, 255, 255) ;")
            self.lineEdit_2.clear()
        elif self.radioButton_4.isChecked():
            self.lineEdit.setStyleSheet("background-color: rgb(85, 255, 255);")
            self.lineEdit_2.setStyleSheet("background-color: rgb(85, 255, 255);")
            self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.lineEdit_7.setStyleSheet("background-color: rgb(85, 255, 255);")
            self.lineEdit_8.setStyleSheet("background-color: rgb(85, 255, 255) ;")
            self.lineEdit_5.clear()
        elif self.radioButton_5.isChecked():
            self.lineEdit.setStyleSheet("background-color: rgb(85, 255, 255);")
            self.lineEdit_2.setStyleSheet("background-color: rgb(85, 255, 255);")
            self.lineEdit_5.setStyleSheet("background-color: rgb(85, 255, 255);")
            self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.lineEdit_8.setStyleSheet("background-color: rgb(85, 255, 255) ;")
            self.lineEdit_7.clear()

    # 气体选择
    def qiti(self):
        A = self.comboBox.currentText()
        if A == "氦气":
                self.lineEdit_3.setText("1.666")
        if A == "氩气":
                self.lineEdit_3.setText("1.665")
        if A == "氢气":
                self.lineEdit_3.setText("1.405")
        if A == "氧气":
                self.lineEdit_3.setText("1.396")
        if A == "氮气":
                self.lineEdit_3.setText("1.400")
        if A == "空气":
                self.lineEdit_3.setText("1.400")
        if A == "二氧化碳":
                self.lineEdit_3.setText("1.399")

    def box(self):
        self.qiti()
        self.jisuan()


#创建计算
    def jisuan(self):
        global S, D, V, κ, Ts, P1, Ps, t, τ, P2
        D = self.lineEdit.text()
        V = self.lineEdit_2.text()
        κ = self.lineEdit_3.text()
        Ts = self.lineEdit_4.text()
        P1 = self.lineEdit_5.text()
        P2 = self.lineEdit_7.text()
        t = self.lineEdit_8.text()
        if self.radioButton.isChecked():
            if D==None or V==None or κ==None or Ts==None or P1==None or P2==None or \
                    D=="" or V=="" or κ=="" or Ts=="" or P1=="" or P2=="" or \
                    float(D)<=0 or float(V)<=0 or float(κ)<=0 or float(P1)<0 or float(P2)<0 or float(P2)>=float(P1)/1.893:
                QMessageBox.information(None, "使用提示", "输入不完整或错误，P2必须<P1/1.892,请检查后重新输入！", QMessageBox.Ok)
                self.qiti()
            else:
                V = float(V)
                κ = float(κ)
                Ts = float(Ts)
                P1 = float(P1)
                P2 = float(P2)
                D=float(D)
                Ps = round(1.893 * P2, 12)
                self.lineEdit_6.setText(str(Ps))
                S = np.pi * np.power(D / 2, 2)
                τ = 5.217 * V / (κ * S) * np.power(273.16 / (273 + Ts), 0.5)
                t = round(τ * (2 * κ * (np.power(P1 / Ps, (κ - 1) / (2 * κ)) - 1) / (κ - 1) + 0.945 * np.power(P1 / P2,((κ - 1) / (2 * κ)))),6)
                if t<=0 or t==None:
                    QMessageBox.information(None, "使用提示", "计算错误，t为负值,请检查后重新输入！", QMessageBox.Ok)
                else:
                    self.lineEdit_8.setText(str(t))
                    self.shuju()
        elif self.radioButton_2.isChecked():
            if t==None or V==None or κ==None or Ts==None or P1==None or P2==None or \
                    t=="" or V=="" or κ=="" or Ts=="" or P1=="" or P2=="" or \
                    float(t)<=0 or float(V)<=0 or float(κ)<=0 or float(P1)<0 or float(P2)<0 or float(P2)>=float(P1)/1.893:
                QMessageBox.information(None, "使用提示", "计算错误，P2必须<P1/1.892,请检查后重新输入！", QMessageBox.Ok)
                self.qiti()
            else:
                V = float(V)
                κ = float(κ)
                Ts = float(Ts)
                P1 = float(P1)
                P2 = float(P2)
                t=float(t)
                Ps = round(1.893 * P2, 12)
                self.lineEdit_6.setText(str(Ps))
                τ = t / (2 * κ * (np.power(P1 / Ps, (κ - 1) / (2 * κ)) - 1) / (κ - 1) + 0.945 * np.power(P1 / P2, ((κ - 1) / (2 * κ))))
                S = 5.217 * V / (κ * τ) * np.power(273.16 / (273 + Ts), 0.5)
                D = round(2 * np.power(S / np.pi, 0.5), 6)
                if D<=0 or D==None:
                    QMessageBox.information(None, "使用提示", "计算错误，D为负值,请检查后重新输入！", QMessageBox.Ok)
                else:
                    self.lineEdit.setText(str(D))
                    self.shuju()
        elif self.radioButton_3.isChecked():
            if D==None or t==None or κ==None or Ts==None or P1==None or P2==None or \
                    D=="" or t=="" or κ=="" or Ts=="" or P1=="" or P2=="" or \
                    float(D)<=0 or float(t)<=0 or float(κ)<=0 or float(P1)<0 or float(P2)<0 or float(P2)>=float(P1)/1.893:
                QMessageBox.information(None, "使用提示", "计算错误，P2必须<P1/1.892,请检查后重新输入！", QMessageBox.Ok)
                self.qiti()
            else:
                t = float(t)
                κ = float(κ)
                Ts = float(Ts)
                P1 = float(P1)
                P2 = float(P2)
                D=float(D)
                Ps = round(1.893 * P2, 12)
                self.lineEdit_6.setText(str(Ps))
                S = np.pi * np.power(D / 2, 2)
                τ = t / (2 * κ * (np.power(P1 / Ps, (κ - 1) / (2 * κ)) - 1) / (κ - 1) + 0.945 * np.power(P1 / P2,((κ - 1) / (2 * κ))))
                V =round(τ*(κ * S) /(np.power(273.16 / (273 + Ts), 0.5)*5.217),6)
                if V <= 0 or V == None:
                    QMessageBox.information(None, "使用提示", "计算错误，V为负值,请检查后重新计算！", QMessageBox.Ok)
                else:
                    self.lineEdit_2.setText(str(V))
                    self.shuju()
        elif self.radioButton_4.isChecked():
            if D==None or t==None or κ==None or Ts==None or V==None or P2==None or \
                    D=="" or t=="" or κ=="" or Ts=="" or V=="" or P2=="" or \
                    float(D)<=0 or float(t)<=0 or float(κ)<=0 or float(V)<0 or float(P2)<0:
                QMessageBox.information(None, "使用提示", "输入不完整或错误，请检查后重新输入！", QMessageBox.Ok)
                self.qiti()
            else:
                P1 = symbols('P1',real=True,nonzero=True)
                t = float(t)
                κ = float(κ)
                Ts = float(Ts)
                V = float(V)
                P2 = float(P2)
                D=float(D)
                Ps = round(1.893 * P2, 12)
                print(Ps)
                S = np.pi * np.power(D / 2, 2)
                τ = 5.217 * V / (κ * S) * np.power(273.16 / (273 + Ts), 0.5)
                P1 = solveset((t-τ * (2 * κ * (np.power(P1 / Ps, (κ - 1) / (2 * κ)) - 1) / (κ - 1) + 0.945 * np.power(P1 / P2,((κ - 1) / (2 * κ))))),(P1))
                self.lineEdit_5.setText(str(P1))
                print(P1)
                # P1=P1 = ' '.join(str(i) for i in P1[0])
                print(P1)
                self.lineEdit_6.setText(str(Ps))
                # P1 = ','.join(str(i) for i in P1)  # 取结果的数值
                # if P1 <= 0 or P1 == None:
                #     QMessageBox.information(None, "使用提示", "计算错误，请检查后重新计算！", QMessageBox.Ok)
                # else:
                #     self.lineEdit_5.setText(str(P1))
                # self.shuju()
        elif self.radioButton_5.isChecked():
            if D==None or t==None or κ==None or Ts==None or V==None or P1==None or \
                    D=="" or t=="" or κ=="" or Ts=="" or V=="" or P1=="" or \
                    float(D)<=0 or float(t)<=0 or float(κ)<=0 or float(V)<0 or float(P1)<0:
                QMessageBox.information(None, "使用提示", "输入不完整或错误，请检查后重新输入！", QMessageBox.Ok)
                self.qiti()
            else:
                P2 = symbols('P2')
                t = float(t)
                κ = float(κ)
                Ts = float(Ts)
                V = float(V)
                P1 = float(P1)
                D=float(D)

                S = np.pi * np.power(D / 2, 2)
                τ = 5.217 * V / (κ * S) * np.power(273.16 / (273 + Ts), 0.5)
                P2 = solveset(τ * (2 * κ * (np.power(P1 / (1.893 * P2), (κ - 1) / (2 * κ)) - 1) / (κ - 1) + 0.945 * np.power(P1 / P2,((κ - 1) / (2 * κ))))-t, P2)
                print(P2)
                # Ps = round(1.893 * P2, 12)
                # self.lineEdit_6.setText(str(Ps))
                # P1 = ','.join(str(i) for i in P1)  # 取结果的数值
                # if P1 <= 0 or P1 == None:
                #     QMessageBox.information(None, "使用提示", "计算错误，请检查后重新计算！", QMessageBox.Ok)
                # else:
                #     self.lineEdit_5.setText(str(P1))
                # self.shuju()











    def datetime(self):
        global now_time
        now_time= datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")

    def shuju(self):
        A = self.comboBox.currentText()
        self.datetime()
        def sql_insert(con, data):
            cursor = con.cursor()
            cursor.execute("insert into 定容放气 (日期,气体类型,孔直径D,孔面积S,容器容积V,等熵指数κ,气源温度Ts,容器内气体的初始压力P1,放气临界压力P,放气至压力P2,充气时间t) values(?,?,?,?,?,?,?,?,?,?,?)",
                           data)
            con.commit()
        data = (now_time,A, D, S, V, κ, Ts, P1, Ps,P2, t)
        sql_insert(con, data)

import img_rc
import sys
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Mainwidow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_dingrongfangqi()  # 创建QT设计的窗体
    ui.setupUi(Mainwidow)  # 初始化设置
    Mainwidow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程