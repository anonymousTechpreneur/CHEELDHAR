# Form implementation generated from reading ui file '.\UI Designs\Suplier Add UI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CustomerAdd(object):
    def setupUi(self, CustomerAdd):
        CustomerAdd.setObjectName("CustomerAdd")
        CustomerAdd.resize(327, 323)
        CustomerAdd.setStyleSheet("background:rgb(255, 255, 255)")
        self.labelSuplierName = QtWidgets.QLabel(parent=CustomerAdd)
        self.labelSuplierName.setGeometry(QtCore.QRect(10, 10, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelSuplierName.setFont(font)
        self.labelSuplierName.setObjectName("labelSuplierName")
        self.textEditSuplierName = QtWidgets.QTextEdit(parent=CustomerAdd)
        self.textEditSuplierName.setGeometry(QtCore.QRect(10, 30, 181, 31))
        self.textEditSuplierName.setObjectName("textEditSuplierName")
        self.textEditPhoneNo = QtWidgets.QTextEdit(parent=CustomerAdd)
        self.textEditPhoneNo.setGeometry(QtCore.QRect(10, 90, 181, 31))
        self.textEditPhoneNo.setObjectName("textEditPhoneNo")
        self.labelPhoneNo = QtWidgets.QLabel(parent=CustomerAdd)
        self.labelPhoneNo.setGeometry(QtCore.QRect(10, 70, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelPhoneNo.setFont(font)
        self.labelPhoneNo.setObjectName("labelPhoneNo")
        self.textEditEmail = QtWidgets.QTextEdit(parent=CustomerAdd)
        self.textEditEmail.setGeometry(QtCore.QRect(10, 150, 181, 31))
        self.textEditEmail.setObjectName("textEditEmail")
        self.labelEmail = QtWidgets.QLabel(parent=CustomerAdd)
        self.labelEmail.setGeometry(QtCore.QRect(10, 130, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelEmail.setFont(font)
        self.labelEmail.setObjectName("labelEmail")
        self.textEditAddress = QtWidgets.QTextEdit(parent=CustomerAdd)
        self.textEditAddress.setGeometry(QtCore.QRect(10, 210, 181, 31))
        self.textEditAddress.setObjectName("textEditAddress")
        self.labelAddress = QtWidgets.QLabel(parent=CustomerAdd)
        self.labelAddress.setGeometry(QtCore.QRect(10, 190, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelAddress.setFont(font)
        self.labelAddress.setObjectName("labelAddress")
        self.DeleteData = QtWidgets.QPushButton(parent=CustomerAdd)
        self.DeleteData.setGeometry(QtCore.QRect(220, 20, 81, 24))
        self.DeleteData.setObjectName("DeleteData")
        self.AudioInputPushButton = QtWidgets.QPushButton(parent=CustomerAdd)
        self.AudioInputPushButton.setGeometry(QtCore.QRect(220, 120, 81, 31))
        self.AudioInputPushButton.setObjectName("AudioInputPushButton")
        self.SaveData = QtWidgets.QPushButton(parent=CustomerAdd)
        self.SaveData.setGeometry(QtCore.QRect(220, 80, 81, 21))
        self.SaveData.setObjectName("SaveData")
        self.labelBankDetail = QtWidgets.QLabel(parent=CustomerAdd)
        self.labelBankDetail.setGeometry(QtCore.QRect(10, 250, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelBankDetail.setFont(font)
        self.labelBankDetail.setObjectName("labelBankDetail")
        self.textEditBankDetail = QtWidgets.QTextEdit(parent=CustomerAdd)
        self.textEditBankDetail.setGeometry(QtCore.QRect(10, 270, 291, 31))
        self.textEditBankDetail.setObjectName("textEditBankDetail")

        self.retranslateUi(CustomerAdd)
        QtCore.QMetaObject.connectSlotsByName(CustomerAdd)

    def retranslateUi(self, CustomerAdd):
        _translate = QtCore.QCoreApplication.translate
        CustomerAdd.setWindowTitle(_translate("CustomerAdd", "Form"))
        self.labelSuplierName.setText(_translate("CustomerAdd", "Suplier Name"))
        self.labelPhoneNo.setText(_translate("CustomerAdd", "Phone no."))
        self.labelEmail.setText(_translate("CustomerAdd", "Email"))
        self.labelAddress.setText(_translate("CustomerAdd", "Address"))
        self.DeleteData.setText(_translate("CustomerAdd", "Delete"))
        self.AudioInputPushButton.setText(_translate("CustomerAdd", "Audio Input"))
        self.SaveData.setText(_translate("CustomerAdd", "Save"))
        self.labelBankDetail.setText(_translate("CustomerAdd", "Bank Details Demo"))
