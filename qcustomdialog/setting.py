# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 646)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_basic = QtWidgets.QFrame(self.centralwidget)
        self.frame_basic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_basic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_basic.setObjectName("frame_basic")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_basic)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.frame_basic)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 145))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.groupBox)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBox_desktop = QtWidgets.QCheckBox(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_desktop.sizePolicy().hasHeightForWidth())
        self.checkBox_desktop.setSizePolicy(sizePolicy)
        self.checkBox_desktop.setObjectName("checkBox_desktop")
        self.horizontalLayout_8.addWidget(self.checkBox_desktop)
        spacerItem = QtWidgets.QSpacerItem(588, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_3 = QtWidgets.QFrame(self.groupBox)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_show_all = QtWidgets.QCheckBox(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_show_all.setFont(font)
        self.checkBox_show_all.setObjectName("checkBox_show_all")
        self.horizontalLayout_4.addWidget(self.checkBox_show_all)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7, 0, QtCore.Qt.AlignLeft)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.frame_basic, 0, QtCore.Qt.AlignTop)
        self.frame_search = QtWidgets.QFrame(self.centralwidget)
        self.frame_search.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_search.setObjectName("frame_search")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_search)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_search)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 1677777))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox_remind = QtWidgets.QCheckBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_remind.setFont(font)
        self.checkBox_remind.setObjectName("checkBox_remind")
        self.verticalLayout_5.addWidget(self.checkBox_remind)
        self.frame_4 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox_last_dir = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_last_dir.setObjectName("checkBox_last_dir")
        self.horizontalLayout_5.addWidget(self.checkBox_last_dir)
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8, 0, QtCore.Qt.AlignLeft)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBox_last_types = QtWidgets.QCheckBox(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_last_types.setFont(font)
        self.checkBox_last_types.setObjectName("checkBox_last_types")
        self.horizontalLayout_7.addWidget(self.checkBox_last_types)
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.frame = QtWidgets.QFrame(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.spinBox_limit_file_size = QtWidgets.QSpinBox(self.frame)
        self.spinBox_limit_file_size.setMinimumSize(QtCore.QSize(70, 0))
        self.spinBox_limit_file_size.setReadOnly(False)
        self.spinBox_limit_file_size.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_limit_file_size.setMaximum(199)
        self.spinBox_limit_file_size.setProperty("value", 100)
        self.spinBox_limit_file_size.setObjectName("spinBox_limit_file_size")
        self.horizontalLayout_2.addWidget(self.spinBox_limit_file_size)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout_5.addWidget(self.frame, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.verticalLayout.addWidget(self.frame_search)
        self.frame_office = QtWidgets.QFrame(self.centralwidget)
        self.frame_office.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_office.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_office.setObjectName("frame_office")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_office)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_office = QtWidgets.QGroupBox(self.frame_office)
        self.groupBox_office.setObjectName("groupBox_office")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_office)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_9 = QtWidgets.QFrame(self.groupBox_office)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.frame_9)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11, 0, QtCore.Qt.AlignLeft)
        self.spinBox_limit_office_time = QtWidgets.QSpinBox(self.frame_9)
        self.spinBox_limit_office_time.setMinimumSize(QtCore.QSize(70, 0))
        self.spinBox_limit_office_time.setMinimum(3)
        self.spinBox_limit_office_time.setProperty("value", 5)
        self.spinBox_limit_office_time.setObjectName("spinBox_limit_office_time")
        self.horizontalLayout_9.addWidget(self.spinBox_limit_office_time, 0, QtCore.Qt.AlignLeft)
        self.label_5 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_10.addWidget(self.frame_9, 0, QtCore.Qt.AlignLeft)
        self.frame_8 = QtWidgets.QFrame(self.groupBox_office)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_10.addWidget(self.frame_8)
        self.verticalLayout_9.addWidget(self.groupBox_office)
        self.verticalLayout.addWidget(self.frame_office)
        self.frame_auto_run = QtWidgets.QFrame(self.centralwidget)
        self.frame_auto_run.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_auto_run.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_auto_run.setObjectName("frame_auto_run")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_auto_run)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_auto_run = QtWidgets.QGroupBox(self.frame_auto_run)
        self.groupBox_auto_run.setCheckable(True)
        self.groupBox_auto_run.setObjectName("groupBox_auto_run")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_auto_run)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_auto_run)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9)
        self.frame_5 = QtWidgets.QFrame(self.groupBox_auto_run)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setContentsMargins(0, 2, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.button_fix_auto = QtWidgets.QPushButton(self.frame_5)
        self.button_fix_auto.setObjectName("button_fix_auto")
        self.horizontalLayout_6.addWidget(self.button_fix_auto, 0, QtCore.Qt.AlignLeft)
        self.label_12 = QtWidgets.QLabel(self.frame_5)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_8.addWidget(self.frame_5)
        self.verticalLayout_7.addWidget(self.groupBox_auto_run)
        self.verticalLayout.addWidget(self.frame_auto_run)
        self.frame_right_menu = QtWidgets.QFrame(self.centralwidget)
        self.frame_right_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_right_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_right_menu.setObjectName("frame_right_menu")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_right_menu)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_right_menu = QtWidgets.QGroupBox(self.frame_right_menu)
        self.groupBox_right_menu.setMaximumSize(QtCore.QSize(16777215, 110))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_right_menu.setFont(font)
        self.groupBox_right_menu.setCheckable(True)
        self.groupBox_right_menu.setObjectName("groupBox_right_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_right_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_right_menu)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.groupBox_right_menu)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 2, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.button_fix_right = QtWidgets.QPushButton(self.frame_2)
        self.button_fix_right.setObjectName("button_fix_right")
        self.horizontalLayout_3.addWidget(self.button_fix_right, 0, QtCore.Qt.AlignLeft)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_4.addWidget(self.groupBox_right_menu)
        self.verticalLayout.addWidget(self.frame_right_menu)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "基本设置"))
        self.checkBox_desktop.setText(_translate("MainWindow", "是否保持桌面图标"))
        self.checkBox_show_all.setText(_translate("MainWindow", "是否允许显示全部文件"))
        self.label_7.setText(_translate("MainWindow", "（此功能可以查看搜索的全部文件，但可能会影响软件稳定性,非必要不建议开启）"))
        self.groupBox_3.setTitle(_translate("MainWindow", "搜索设置"))
        self.checkBox_remind.setText(_translate("MainWindow", "是否搜索完成进行提醒"))
        self.checkBox_last_dir.setText(_translate("MainWindow", "是否记住上次搜索目录"))
        self.checkBox_last_types.setText(_translate("MainWindow", "是否记住上次搜索时的文件类型"))
        self.label_3.setText(_translate("MainWindow", "文件限制："))
        self.spinBox_limit_file_size.setSuffix(_translate("MainWindow", "MB"))
        self.label_4.setText(_translate("MainWindow", "（超过文件限制的文件将不进行搜索）"))
        self.groupBox_office.setTitle(_translate("MainWindow", "Office设置"))
        self.label_11.setText(_translate("MainWindow", "限制时间："))
        self.spinBox_limit_office_time.setSuffix(_translate("MainWindow", "S"))
        self.label_5.setText(_translate("MainWindow", "（如果用户未在规定时间内响应Office的提示框，将直接对当前文档报错处理。）"))
        self.groupBox_auto_run.setTitle(_translate("MainWindow", "开机自启"))
        self.label_9.setText(_translate("MainWindow", "此功能将允许软件开机自行启动"))
        self.label_10.setText(_translate("MainWindow", "如果无法正常开机自启，进行"))
        self.button_fix_auto.setText(_translate("MainWindow", "修复"))
        self.label_12.setText(_translate("MainWindow", "。"))
        self.groupBox_right_menu.setTitle(_translate("MainWindow", "右键菜单"))
        self.label.setText(_translate("MainWindow", "此功能可以在文件夹或者空白处右键快速启动搜索。"))
        self.label_2.setText(_translate("MainWindow", "如果右键菜单无法正常运行，进行"))
        self.button_fix_right.setText(_translate("MainWindow", "修复"))
        self.label_6.setText(_translate("MainWindow", "。"))
