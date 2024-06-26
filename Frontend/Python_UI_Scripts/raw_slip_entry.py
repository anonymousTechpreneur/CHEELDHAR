from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QDateTime
from PyQt6.QtGui import QPixmap
import sqlalchemy
#from Backend.Create_database_connection import *
from STTLibCall import *

#db_conn, connector = connect()

class Ui_RawSlip(object):

    def sttAPI(self):
        output = {'customerId':"",'Customer_Name':"",'Customer_Phone_Number':""}
        output = Speech()
        self.customer_details.append(str([output['customerId'],output['Customer_Name'],output['Customer_Phone_Number']]))
        print("Go to UI")

    def update_combo_box(self):
        """
        Clears and repopulates the combo box with updated customer details.
        """
        self.CustomerDetailcomboBox.clear()
        for customer_detail in self.customer_details:
            print(customer_detail)
            self.CustomerDetailcomboBox.addItem(str(customer_detail))

    def setupUi(self, RawSlip):
        # self.db_conn, self.connector = connect()
        # disconnect(self.connector)
        self.customer_details = ["Select Customer"]
        RawSlip.setObjectName("RawSlip")
        RawSlip.resize(802, 600)
        RawSlip.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(parent=RawSlip)
        self.centralwidget.setObjectName("centralwidget")
        self.DataEntryTableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.DataEntryTableWidget.setGeometry(QtCore.QRect(0, 160, 801, 401))
        self.DataEntryTableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.DataEntryTableWidget.setMouseTracking(True)
        self.DataEntryTableWidget.setTabletTracking(True)
        self.DataEntryTableWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.DataEntryTableWidget.setAcceptDrops(True)
        self.DataEntryTableWidget.setAutoFillBackground(True)
        self.DataEntryTableWidget.setStyleSheet("")
        self.DataEntryTableWidget.setObjectName("DataEntryTableWidget")
        self.DataEntryTableWidget.setColumnCount(8)
        self.DataEntryTableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.DataEntryTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.DataEntryTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.DataEntryTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.DataEntryTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.DataEntryTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.DataEntryTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.DataEntryTableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.DataEntryTableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.DataEntryTableWidget.setHorizontalHeaderItem(7, item)
        self.timeInput = QtWidgets.QTimeEdit(QDateTime.currentDateTime().time(),parent=self.centralwidget)
        self.timeInput.setGeometry(QtCore.QRect(500, 50, 81, 31))
        self.timeInput.setObjectName("timeInput")
        self.dateInput = QtWidgets.QDateEdit(QDateTime.currentDateTime().date(),parent=self.centralwidget)
        self.dateInput.setGeometry(QtCore.QRect(400, 50, 91, 31))
        self.dateInput.setObjectName("dateInput")
        self.SaveData = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SaveData.setGeometry(QtCore.QRect(610, 130, 81, 21))
        self.SaveData.setObjectName("SaveData")
        self.DeleteData = QtWidgets.QPushButton(parent=self.centralwidget)
        self.DeleteData.setGeometry(QtCore.QRect(710, 90, 81, 24))
        self.DeleteData.setObjectName("DeleteData")
        self.PrintData = QtWidgets.QPushButton(parent=self.centralwidget)
        self.PrintData.setGeometry(QtCore.QRect(710, 130, 81, 21))
        self.PrintData.setObjectName("PrintData")
        self.PaymentTableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.PaymentTableWidget.setGeometry(QtCore.QRect(150, 90, 431, 61))
        self.PaymentTableWidget.setObjectName("PaymentTableWidget")
        self.PaymentTableWidget.setColumnCount(4)
        self.PaymentTableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.PaymentTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.PaymentTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PaymentTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.PaymentTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.PaymentTableWidget.setHorizontalHeaderItem(3, item)
        self.AudioInputPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.AudioInputPushButton.setGeometry(QtCore.QRect(610, 90, 81, 31))
        self.AudioInputPushButton.setObjectName("AudioInputPushButton")
        self.PaymentDetail = QtWidgets.QLabel(parent=self.centralwidget)
        self.PaymentDetail.setGeometry(QtCore.QRect(10, 90, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.PaymentDetail.setFont(font)
        self.PaymentDetail.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.PaymentDetail.setObjectName("PaymentDetail")
        self.BillNoLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.BillNoLabel.setGeometry(QtCore.QRect(590, 50, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.BillNoLabel.setFont(font)
        self.BillNoLabel.setObjectName("BillNoLabel")
        self.BillNoEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.BillNoEdit.setGeometry(QtCore.QRect(650, 50, 141, 31))
        self.BillNoEdit.setObjectName("BillNoEdit")
        self.CustomerDetailcomboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.CustomerDetailcomboBox.setGeometry(QtCore.QRect(10, 50, 271, 31))
        self.CustomerDetailcomboBox.setObjectName("CustomerDetailcomboBox")
        self.CustomerDetailcomboBox.addItem("")
        self.pushButtonAddCustomer = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAddCustomer.setGeometry(QtCore.QRect(290, 50, 101, 31))
        self.pushButtonAddCustomer.setObjectName("pushButtonAddCustomer")
        self.CreditDebitcomboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.CreditDebitcomboBox.setGeometry(QtCore.QRect(10, 120, 121, 31))
        self.CreditDebitcomboBox.setObjectName("CreditDebitcomboBox")
        self.CreditDebitcomboBox.addItem("")
        self.CreditDebitcomboBox.addItem("")
        self.labelGaneshJi = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelGaneshJi.setGeometry(QtCore.QRect(340, 0, 141, 41))
        #self.labelGaneshJi.setStyleSheet("background-image: url(:Ganesh_Ji.jpg);")
        self.labelGaneshJi.setText("")
        self.labelGaneshJi.setObjectName("labelGaneshJi")
        pixmap = QPixmap('E:\CHEELDHAR\Frontend\Ganesh_Ji.jpg')
        self.labelGaneshJi.setPixmap(pixmap)

        RawSlip.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=RawSlip)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 22))
        self.menubar.setObjectName("menubar")
        self.menuRaw_Slip = QtWidgets.QMenu(parent=self.menubar)
        self.menuRaw_Slip.setObjectName("menuRaw_Slip")
        self.menuGST_Slip = QtWidgets.QMenu(parent=self.menubar)
        self.menuGST_Slip.setObjectName("menuGST_Slip")
        self.menuHome = QtWidgets.QMenu(parent=self.menubar)
        self.menuHome.setObjectName("menuHome")
        RawSlip.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=RawSlip)
        self.statusbar.setObjectName("statusbar")
        RawSlip.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuRaw_Slip.menuAction())
        self.menubar.addAction(self.menuGST_Slip.menuAction())
        self.AudioInputPushButton.clicked.connect(lambda:self.sttAPI())
        self.pushButtonAddCustomer.clicked.connect(self.update_combo_box)

        self.retranslateUi(RawSlip)
        QtCore.QMetaObject.connectSlotsByName(RawSlip)
        RawSlip.setTabOrder(self.CustomerDetailcomboBox, self.pushButtonAddCustomer)
        RawSlip.setTabOrder(self.pushButtonAddCustomer, self.dateInput)
        RawSlip.setTabOrder(self.dateInput, self.timeInput)
        RawSlip.setTabOrder(self.timeInput, self.BillNoEdit)
        RawSlip.setTabOrder(self.BillNoEdit, self.AudioInputPushButton)
        RawSlip.setTabOrder(self.AudioInputPushButton, self.DataEntryTableWidget)
        RawSlip.setTabOrder(self.DataEntryTableWidget, self.PaymentTableWidget)
        RawSlip.setTabOrder(self.PaymentTableWidget, self.SaveData)
        RawSlip.setTabOrder(self.SaveData, self.PrintData)
        RawSlip.setTabOrder(self.PrintData, self.DeleteData)

    def retranslateUi(self, RawSlip):
        _translate = QtCore.QCoreApplication.translate
        RawSlip.setWindowTitle(_translate("RawSlip", "MainWindow"))
        item = self.DataEntryTableWidget.verticalHeaderItem(0)
        item.setText(_translate("RawSlip", "1."))
        item = self.DataEntryTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("RawSlip", "Product Detail"))
        item = self.DataEntryTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("RawSlip", "SKU No."))
        item = self.DataEntryTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("RawSlip", "Quantity"))
        item = self.DataEntryTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("RawSlip", "Price/piece"))
        item = self.DataEntryTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("RawSlip", "Discount"))
        item = self.DataEntryTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("RawSlip", "Firm"))
        item = self.DataEntryTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("RawSlip", "Net Price"))
        item = self.DataEntryTableWidget.horizontalHeaderItem(7)
        item.setText(_translate("RawSlip", "Action"))
        self.SaveData.setText(_translate("RawSlip", "Save"))
        self.DeleteData.setText(_translate("RawSlip", "Delete"))
        self.PrintData.setText(_translate("RawSlip", "Print"))
        item = self.PaymentTableWidget.verticalHeaderItem(0)
        item.setText(_translate("RawSlip", "1."))
        item = self.PaymentTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("RawSlip", "Total"))
        item = self.PaymentTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("RawSlip", "Cash"))
        item = self.PaymentTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("RawSlip", "Online"))
        item = self.PaymentTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("RawSlip", "Remaining"))
        self.AudioInputPushButton.setText(_translate("RawSlip", "Audio Input"))
        self.PaymentDetail.setText(_translate("RawSlip", "Payment Details ->"))
        self.BillNoLabel.setText(_translate("RawSlip", "Bill No. -"))
        self.BillNoEdit.setHtml(_translate("RawSlip", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A1CUST01012024</p></body></html>"))
        self.CustomerDetailcomboBox.setItemText(0, _translate("RawSlip", "Customer Detail"))
        self.pushButtonAddCustomer.setText(_translate("RawSlip", "Add Customer"))
        self.CreditDebitcomboBox.setItemText(0, _translate("RawSlip", "Credit"))
        self.CreditDebitcomboBox.setItemText(1, _translate("RawSlip", "Debit"))
        self.menuRaw_Slip.setTitle(_translate("RawSlip", "Raw Slip"))
        self.menuGST_Slip.setTitle(_translate("RawSlip", "GST Slip"))
        self.menuHome.setTitle(_translate("RawSlip", "Home"))
