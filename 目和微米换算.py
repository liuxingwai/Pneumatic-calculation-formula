# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '目和微米换算.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QMessageBox, QFileDialog
from PyQt5.QtGui import *
import sqlite3
import datetime
from sqlite3 import Error


#连接数据库
def sql_connection():
    try:
        # con = sqlite3.connect("目和微米换算数据库.db")
        con = sqlite3.connect("公式集合数据库.db")
        return con
    except Error:
        print(Error)
con = sql_connection()
#创建表
def sql_table(con):
    try:
        # 创建游标
        cursor = con.cursor()
        cursor.execute("create table 目和微米换算 (日期,目,微米)")
        # 提交事务
        con.commit()
    except Error:
        print(Error)
sql_table(con)


class Ui_muweimi(QMainWindow):
    def setupUi(self, muweimi):
        muweimi.setObjectName("muweimi")
        muweimi.setWindowModality(QtCore.Qt.NonModal)
        muweimi.setEnabled(True)
        muweimi.resize(320, 350)
        muweimi.setMaximumSize(QtCore.QSize(320, 350))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        muweimi.setFont(font)
        muweimi.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/PNG/chengliang.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        muweimi.setWindowIcon(icon)
        muweimi.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(muweimi)
        self.label.setGeometry(QtCore.QRect(0, 20, 320, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        # self.pushButton = QtWidgets.QPushButton(muweimi)
        # self.pushButton.setGeometry(QtCore.QRect(100, 290, 110, 40))
        # font = QtGui.QFont()
        # font.setFamily("黑体")
        # font.setPointSize(18)
        # self.pushButton.setFont(font)
        # self.pushButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        # self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(muweimi)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 170, 200, 40))
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
        self.radioButton = QtWidgets.QRadioButton(muweimi)
        self.radioButton.setGeometry(QtCore.QRect(30, 80, 120, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(muweimi)
        self.radioButton_2.setGeometry(QtCore.QRect(170, 80, 120, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit = QtWidgets.QLineEdit(muweimi)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(90, 120, 200, 40))
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
        self.label_4 = QtWidgets.QLabel(muweimi)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 50, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(muweimi)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 50, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(muweimi)
        self.label_8.setGeometry(QtCore.QRect(30, 230, 261, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setKerning(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(muweimi)
        QtCore.QMetaObject.connectSlotsByName(muweimi)

        #创建信号槽
        # self.pushButton.clicked.connect(self.jisuan)
        self.radioButton.toggled.connect(self.cleck)
        self.radioButton_2.toggled.connect(self.cleck)
        self.lineEdit.editingFinished.connect(self.jisuan)
        self.lineEdit_2.editingFinished.connect(self.jisuan)


        #设置数字输入
        self.lineEdit.setValidator(QDoubleValidator())
        self.lineEdit_2.setValidator(QDoubleValidator())

    def retranslateUi(self, muweimi):
        _translate = QtCore.QCoreApplication.translate
        muweimi.setWindowTitle(_translate("muweimi", "目和微米换算V1.1 By ChengLiang"))
        self.label.setText(_translate("muweimi", "目和微米换算"))
        # self.pushButton.setText(_translate("muweimi", "计算"))
        self.radioButton.setText(_translate("muweimi", "计算目"))
        self.radioButton_2.setText(_translate("muweimi", "计算微米"))
        self.label_4.setText(_translate("muweimi", "微米"))
        self.label_3.setText(_translate("muweimi", "目"))
        self.label_8.setText(_translate("muweimi", "<html><head/><body><p>目=14832.4/微米</p></body></html>"))

    def cleck(self):
        if self.radioButton.isChecked():
            self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.lineEdit_2.setStyleSheet("background-color: rgb(85, 255, 255);")
        if self.radioButton_2.isChecked():
            self.lineEdit.setStyleSheet("background-color: rgb(85, 255, 255);")
            self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")

    def jisuan(self):
        global M,μ
        M =self.lineEdit.text()
        μ = self.lineEdit_2.text()
        if self.radioButton.isChecked():
            if μ==None or μ=="" or float(μ)<=0:
                QMessageBox.information(None, "使用提示", "微米数据错误，请检查后重新输入！", QMessageBox.Ok)
            else:
                μ = float(self.lineEdit_2.text())
                M = round(14832.4 / μ, 10)
                self.lineEdit.setText(str(M))
                self.shuju()
        if self.radioButton_2.isChecked():
            if M==None or M=="" or float(M)<=0:
                QMessageBox.information(None, "使用提示", "微米数据错误，请检查后重新输入！", QMessageBox.Ok)
            else:
                M = float(self.lineEdit.text())
                μ = round(14832.4 / M, 10)
                self.lineEdit_2.setText(str(μ))
                self.shuju()


    def datetime(self):
        global now_time
        now_time= datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")

    def shuju(self):
        self.datetime()
        def sql_insert(con, data):
                cursor = con.cursor()
                cursor.execute("insert into 目和微米换算(日期,目,微米) values(?,?,?)", data)
                con.commit()
        data = (now_time,M, μ)
        sql_insert(con, data)

import img_rc
import sys
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Mainwidow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_muweimi()  # 创建QT设计的窗体
    ui.setupUi(Mainwidow)  # 初始化设置
    Mainwidow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
