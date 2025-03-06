# Form implementation generated from reading ui file 'UI_Main_Form.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class UIMainForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1078, 798)
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=Form)
        self.calendarWidget.setGeometry(QtCore.QRect(410, 190, 400, 350))
        self.calendarWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.calendarWidget.setAutoFillBackground(True)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SelectionMode.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.HorizontalHeaderFormat.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.ISOWeekNumbers)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.searchLbl = QtWidgets.QLabel(parent=Form)
        self.searchLbl.setGeometry(QtCore.QRect(400, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.searchLbl.setFont(font)
        self.searchLbl.setObjectName("searchLbl")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(860, 140, 201, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.nameTchrEdit_1 = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameTchrEdit_1.setFont(font)
        self.nameTchrEdit_1.setObjectName("nameTchrEdit_1")
        self.verticalLayout.addWidget(self.nameTchrEdit_1)
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.nameTchrEdit_2 = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameTchrEdit_2.setFont(font)
        self.nameTchrEdit_2.setObjectName("nameTchrEdit_2")
        self.verticalLayout.addWidget(self.nameTchrEdit_2)
        self.label_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.nameTchrEdit_3 = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameTchrEdit_3.setFont(font)
        self.nameTchrEdit_3.setText("")
        self.nameTchrEdit_3.setObjectName("nameTchrEdit_3")
        self.verticalLayout.addWidget(self.nameTchrEdit_3)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.selectDateBtn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.selectDateBtn.setFont(font)
        self.selectDateBtn.setObjectName("selectDateBtn")
        self.verticalLayout.addWidget(self.selectDateBtn)
        self.dateTchrEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.dateTchrEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateTchrEdit.setFont(font)
        self.dateTchrEdit.setObjectName("dateTchrEdit")
        self.verticalLayout.addWidget(self.dateTchrEdit)
        self.errTchrLbl = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.errTchrLbl.setFont(font)
        self.errTchrLbl.setText("")
        self.errTchrLbl.setObjectName("errTchrLbl")
        self.verticalLayout.addWidget(self.errTchrLbl)
        self.startSrch = QtWidgets.QPushButton(parent=Form)
        self.startSrch.setGeometry(QtCore.QRect(680, 60, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startSrch.setFont(font)
        self.startSrch.setObjectName("startSrch")
        self.okDateBtn = QtWidgets.QPushButton(parent=Form)
        self.okDateBtn.setGeometry(QtCore.QRect(690, 540, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.okDateBtn.setFont(font)
        self.okDateBtn.setObjectName("okDateBtn")
        self.listView = QtWidgets.QListView(parent=Form)
        self.listView.setGeometry(QtCore.QRect(400, 170, 421, 411))
        self.listView.setObjectName("listView")
        self.exportBtn = QtWidgets.QPushButton(parent=Form)
        self.exportBtn.setGeometry(QtCore.QRect(280, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exportBtn.setFont(font)
        self.exportBtn.setObjectName("exportBtn")
        self.endSrch = QtWidgets.QPushButton(parent=Form)
        self.endSrch.setGeometry(QtCore.QRect(760, 60, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.endSrch.setFont(font)
        self.endSrch.setObjectName("endSrch")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 811, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.newTchrBtn = QtWidgets.QPushButton(parent=Form)
        self.newTchrBtn.setGeometry(QtCore.QRect(940, 510, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.newTchrBtn.setFont(font)
        self.newTchrBtn.setObjectName("newTchrBtn")
        self.searchEdit = QtWidgets.QLineEdit(parent=Form)
        self.searchEdit.setGeometry(QtCore.QRect(400, 60, 271, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.searchEdit.setFont(font)
        self.searchEdit.setText("")
        self.searchEdit.setObjectName("searchEdit")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(590, 590, 474, 191))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_0 = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_0.setFont(font)
        self.checkBox_0.setObjectName("checkBox_0")
        self.gridLayout.addWidget(self.checkBox_0, 0, 0, 1, 1)
        self.checkBox_1 = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setObjectName("checkBox_1")
        self.gridLayout.addWidget(self.checkBox_1, 1, 0, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout.addWidget(self.checkBox_10, 4, 0, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 2, 0, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 6, 1, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout.addWidget(self.checkBox_11, 6, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 3, 0, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 4, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 3, 1, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 2, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 1, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 590, 514, 161))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.tchrsBox = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_3)
        self.tchrsBox.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tchrsBox.setFont(font)
        self.tchrsBox.setEditable(True)
        self.tchrsBox.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.NoInsert)
        self.tchrsBox.setObjectName("tchrsBox")
        self.horizontalLayout.addWidget(self.tchrsBox)
        self.deleteTchrBtn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deleteTchrBtn.setFont(font)
        self.deleteTchrBtn.setObjectName("deleteTchrBtn")
        self.horizontalLayout.addWidget(self.deleteTchrBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.errDelLbl = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.errDelLbl.setFont(font)
        self.errDelLbl.setText("")
        self.errDelLbl.setObjectName("errDelLbl")
        self.verticalLayout_3.addWidget(self.errDelLbl)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 80, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.loadScansBtn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.loadScansBtn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.loadScansBtn.setObjectName("loadScansBtn")
        self.horizontalLayout_2.addWidget(self.loadScansBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, 80, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.DBcopyBtn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.DBcopyBtn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.DBcopyBtn.setObjectName("DBcopyBtn")
        self.horizontalLayout_3.addWidget(self.DBcopyBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.label_12 = QtWidgets.QLabel(parent=Form)
        self.label_12.setGeometry(QtCore.QRect(10, 60, 391, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(685, 10, 371, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_15 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.backBtn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.backBtn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout_4.addWidget(self.backBtn)
        self.updDateBtn = QtWidgets.QPushButton(parent=Form)
        self.updDateBtn.setGeometry(QtCore.QRect(860, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.updDateBtn.setFont(font)
        self.updDateBtn.setObjectName("updDateBtn")
        self.searchLbl.raise_()
        self.verticalLayoutWidget.raise_()
        self.startSrch.raise_()
        self.exportBtn.raise_()
        self.endSrch.raise_()
        self.label_5.raise_()
        self.tableWidget.raise_()
        self.newTchrBtn.raise_()
        self.searchEdit.raise_()
        self.listView.raise_()
        self.calendarWidget.raise_()
        self.okDateBtn.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.label_12.raise_()
        self.horizontalLayoutWidget.raise_()
        self.updDateBtn.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.searchLbl.setText(_translate("Form", "Поиск по учителю:"))
        self.label_4.setText(_translate("Form", "Добавить нового учителя:"))
        self.label.setText(_translate("Form", "Фамилия:"))
        self.label_6.setText(_translate("Form", "Имя:"))
        self.label_7.setText(_translate("Form", "Отчество:"))
        self.label_2.setText(_translate("Form", "Дата начала работы:"))
        self.selectDateBtn.setText(_translate("Form", "Выбрать дату"))
        self.startSrch.setText(_translate("Form", "Поиск"))
        self.okDateBtn.setText(_translate("Form", "Подтвердить"))
        self.exportBtn.setText(_translate("Form", "OK"))
        self.endSrch.setText(_translate("Form", "Отменить"))
        self.label_5.setText(_translate("Form", "Выгрузить отчет в формате Excel:"))
        self.newTchrBtn.setText(_translate("Form", "Добавить"))
        self.label_9.setText(_translate("Form", "Колонки:"))
        self.checkBox_0.setText(_translate("Form", "ФИО"))
        self.checkBox_1.setText(_translate("Form", "Персональный конец периода"))
        self.checkBox_10.setText(_translate("Form", "Часы за прошлый год"))
        self.checkBox_9.setText(_translate("Form", "Дата начала работы"))
        self.checkBox_8.setText(_translate("Form", "Дата окончания курса"))
        self.checkBox_11.setText(_translate("Form", "Часы за позапрошлый год"))
        self.checkBox_2.setText(_translate("Form", "Количество часов в текущем периоде"))
        self.checkBox_7.setText(_translate("Form", "Объем курса"))
        self.checkBox_6.setText(_translate("Form", "Название курса"))
        self.checkBox_5.setText(_translate("Form", "План на 3 год"))
        self.checkBox_4.setText(_translate("Form", "План на 2 год"))
        self.checkBox_3.setText(_translate("Form", "План на 1 год"))
        self.label_8.setText(_translate("Form", "Удалить учителя:"))
        self.deleteTchrBtn.setText(_translate("Form", "Удалить"))
        self.label_10.setText(_translate("Form", "Выгрузить сканы сертификатов:"))
        self.loadScansBtn.setText(_translate("Form", "OK"))
        self.label_11.setText(_translate("Form", "Создать копию базы данных в выбранной папке:"))
        self.DBcopyBtn.setText(_translate("Form", "ОК"))
        self.label_12.setText(_translate("Form", "Информация о КПК по текущему 3-х летнему периоду"))
        self.label_15.setText(_translate("Form", "Информация по учителю / Добавить новый КПК:"))
        self.backBtn.setText(_translate("Form", "OK"))
        self.updDateBtn.setText(_translate("Form", "Сохранить изменения"))
