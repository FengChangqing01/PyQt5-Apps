# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mwin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MWin(object):
    def setupUi(self, MWin):
        MWin.setObjectName("MWin")
        MWin.resize(720, 400)
        MWin.setMinimumSize(QtCore.QSize(720, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        MWin.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/music-box.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MWin.setWindowIcon(icon)
        MWin.setIconSize(QtCore.QSize(40, 40))
        self.centralWidget = QtWidgets.QWidget(MWin)
        self.centralWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(5, 5, 0, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.searchBtn = QtWidgets.QToolButton(self.tab)
        self.searchBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.searchBtn.setObjectName("searchBtn")
        self.horizontalLayout.addWidget(self.searchBtn)
        self.downloadBtn = QtWidgets.QToolButton(self.tab)
        self.downloadBtn.setEnabled(True)
        self.downloadBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.downloadBtn.setObjectName("downloadBtn")
        self.horizontalLayout.addWidget(self.downloadBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.mtable = QtWidgets.QTableWidget(self.tab)
        self.mtable.setAlternatingRowColors(True)
        self.mtable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.mtable.setObjectName("mtable")
        self.mtable.setColumnCount(0)
        self.mtable.setRowCount(0)
        self.mtable.horizontalHeader().setStretchLastSection(True)
        self.mtable.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.mtable)
        self.tabWidget.addTab(self.tab, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab2)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dtable = QtWidgets.QTableWidget(self.tab2)
        self.dtable.setObjectName("dtable")
        self.dtable.setColumnCount(6)
        self.dtable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dtable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dtable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dtable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dtable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.dtable.setHorizontalHeaderItem(5, item)
        self.dtable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.dtable)
        self.tabWidget.addTab(self.tab2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MWin.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MWin)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 720, 23))
        self.menuBar.setObjectName("menuBar")
        MWin.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MWin)
        self.statusBar.setObjectName("statusBar")
        MWin.setStatusBar(self.statusBar)

        self.retranslateUi(MWin)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MWin)

    def retranslateUi(self, MWin):
        _translate = QtCore.QCoreApplication.translate
        MWin.setWindowTitle(_translate("MWin", "Lossless Music Box v1.0.0 ©Lewis Tian"))
        self.comboBox.setItemText(0, _translate("MWin", "QQ"))
        self.comboBox.setItemText(1, _translate("MWin", "kuwo"))
        self.comboBox.setItemText(2, _translate("MWin", "xiami"))
        self.comboBox.setItemText(3, _translate("MWin", "kugou"))
        self.comboBox.setItemText(4, _translate("MWin", "baidu"))
        self.comboBox.setItemText(5, _translate("MWin", "netease"))
        self.searchBtn.setText(_translate("MWin", "Search"))
        self.searchBtn.setShortcut(_translate("MWin", "Return"))
        self.downloadBtn.setText(_translate("MWin", "Download"))
        self.downloadBtn.setShortcut(_translate("MWin", "Ctrl+Return"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MWin", "Home"))
        item = self.dtable.horizontalHeaderItem(0)
        item.setText(_translate("MWin", "song"))
        item = self.dtable.horizontalHeaderItem(1)
        item.setText(_translate("MWin", "singer"))
        item = self.dtable.horizontalHeaderItem(2)
        item.setText(_translate("MWin", "album"))
        item = self.dtable.horizontalHeaderItem(3)
        item.setText(_translate("MWin", "cover"))
        item = self.dtable.horizontalHeaderItem(4)
        item.setText(_translate("MWin", "lrc"))
        item = self.dtable.horizontalHeaderItem(5)
        item.setText(_translate("MWin", "url"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MWin", "Download"))

import res_rc
