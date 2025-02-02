# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '比体积和密度计算.ui'
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
        # con = sqlite3.connect("比体积和密度计算数据库.db")
        con = sqlite3.connect("公式集合数据库.db")
        return con
    except Error:
        print(Error)
#创建表
def sql_table(con):
    try:
        # 创建游标
        cursor = con.cursor()
        cursor.execute("create table 比体积和密度 (日期,气体比体积Vm,气体体积V,气体质量m,气体密度ρ)")
        # 提交事务
        con.commit()
    except Error:
        print(Error)
con = sql_connection()
sql_table(con)

class Ui_bitijimidu(QMainWindow):
    def setupUi(self, bitijimidu):
        bitijimidu.setObjectName("bitijimidu")
        bitijimidu.setWindowModality(QtCore.Qt.NonModal)
        bitijimidu.setEnabled(True)
        bitijimidu.resize(600, 360)
        bitijimidu.setMaximumSize(QtCore.QSize(600, 360))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        bitijimidu.setFont(font)
        bitijimidu.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/PNG/chengliang.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        bitijimidu.setWindowIcon(icon)
        bitijimidu.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(bitijimidu)
        self.label.setGeometry(QtCore.QRect(0, 20, 600, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(bitijimidu)
        self.pushButton.setGeometry(QtCore.QRect(380, 290, 100, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(bitijimidu)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 130, 290, 40))
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
        self.lineEdit_4 = QtWidgets.QLineEdit(bitijimidu)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 230, 290, 40))
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
        self.lineEdit = QtWidgets.QLineEdit(bitijimidu)
        self.lineEdit.setGeometry(QtCore.QRect(290, 80, 290, 40))
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
        self.lineEdit_3 = QtWidgets.QLineEdit(bitijimidu)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 180, 290, 40))
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
        self.label_4 = QtWidgets.QLabel(bitijimidu)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(bitijimidu)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(bitijimidu)
        self.label_6.setGeometry(QtCore.QRect(20, 230, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(bitijimidu)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 260, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(bitijimidu)
        self.label_10.setGeometry(QtCore.QRect(40, 290, 250, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")

        self.retranslateUi(bitijimidu)
        QtCore.QMetaObject.connectSlotsByName(bitijimidu)

        # 只允许输入数字
        self.lineEdit.setValidator(QDoubleValidator())
        self.lineEdit_2.setValidator(QDoubleValidator())
        self.lineEdit_3.setValidator(QDoubleValidator())
        self.lineEdit_4.setValidator(QDoubleValidator())

        self.pushButton.clicked.connect(self.jisuan)

    def jisuan(self):
        global Vm,V,m,ρ
        Vm=self.lineEdit.text()
        V=self.lineEdit_2.text()
        m=self.lineEdit_3.text()
        ρ=self.lineEdit_4.text()
        if V==None or m==None or V =="" or m =="" or float(V)<0 or float(m)<0:
            QMessageBox.information(None, "提示说明", "请正确输入体积V和质量m！", QMessageBox.Ok)
        else:
            Vm=float(V)/float(m)
            ρ=1/Vm
            self.lineEdit_4.setText(str(ρ))
            self.lineEdit.setText(str(Vm))
            self.shuju()

    def datetime(self):
        global now_time
        now_time= datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")

    def shuju(self):
        self.datetime()
        def sql_insert(con, data):
                cursor = con.cursor()
                cursor.execute("insert into 比体积和密度 (日期,气体比体积Vm,气体体积V,气体质量m,气体密度ρ) values(?,?,?,?,?)", data)
                con.commit()
        data = (now_time,Vm,V,m,ρ)
        sql_insert(con, data)

    def retranslateUi(self, bitijimidu):
        _translate = QtCore.QCoreApplication.translate
        bitijimidu.setWindowTitle(_translate("bitijimidu", "比体积和密度计算V1.1 By ChengLiang"))
        self.label.setText(_translate("bitijimidu", "比体积和密度计算"))
        self.pushButton.setText(_translate("bitijimidu", "计算"))
        self.label_4.setText(_translate("bitijimidu", "气体体积V（L）"))
        self.label_5.setText(_translate("bitijimidu", "气体质量m（g）"))
        self.label_6.setText(_translate("bitijimidu", "气体密度ρ（g/L）"))
        self.label_3.setText(_translate("bitijimidu", "气体比体积Vm（L/g）"))
        self.label_10.setText(_translate("bitijimidu", "<html><head/><body><p>ρ=m/V=1/V<span style=\" vertical-align:sub;\">m</span></p></body></html>"))
import img_rc
import sys
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Mainwidow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_bitijimidu()  # 创建QT设计的窗体
    ui.setupUi(Mainwidow)  # 初始化设置
    Mainwidow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程