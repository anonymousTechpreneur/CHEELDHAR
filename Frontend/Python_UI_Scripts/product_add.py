# Form implementation generated from reading ui file '.\UI Designs\Product Add UI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ProductAdd(object):
    def setupUi(self, ProductAdd):
        ProductAdd.setObjectName("ProductAdd")
        ProductAdd.resize(327, 323)
        ProductAdd.setStyleSheet("background:rgb(255, 255, 255)")
        self.labelProductName = QtWidgets.QLabel(parent=ProductAdd)
        self.labelProductName.setGeometry(QtCore.QRect(10, 10, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelProductName.setFont(font)
        self.labelProductName.setObjectName("labelProductName")
        self.textEditProductName = QtWidgets.QTextEdit(parent=ProductAdd)
        self.textEditProductName.setGeometry(QtCore.QRect(10, 30, 181, 31))
        self.textEditProductName.setObjectName("textEditProductName")
        self.textEditProductCategory = QtWidgets.QTextEdit(parent=ProductAdd)
        self.textEditProductCategory.setGeometry(QtCore.QRect(10, 90, 181, 31))
        self.textEditProductCategory.setObjectName("textEditProductCategory")
        self.labelProductCategory = QtWidgets.QLabel(parent=ProductAdd)
        self.labelProductCategory.setGeometry(QtCore.QRect(10, 70, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelProductCategory.setFont(font)
        self.labelProductCategory.setObjectName("labelProductCategory")
        self.textEditProductDescription = QtWidgets.QTextEdit(parent=ProductAdd)
        self.textEditProductDescription.setGeometry(QtCore.QRect(10, 150, 291, 101))
        self.textEditProductDescription.setObjectName("textEditProductDescription")
        self.labelProductDescription = QtWidgets.QLabel(parent=ProductAdd)
        self.labelProductDescription.setGeometry(QtCore.QRect(10, 130, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelProductDescription.setFont(font)
        self.labelProductDescription.setObjectName("labelProductDescription")
        self.DeleteData = QtWidgets.QPushButton(parent=ProductAdd)
        self.DeleteData.setGeometry(QtCore.QRect(220, 20, 81, 24))
        self.DeleteData.setObjectName("DeleteData")
        self.AudioInputPushButton = QtWidgets.QPushButton(parent=ProductAdd)
        self.AudioInputPushButton.setGeometry(QtCore.QRect(220, 110, 81, 31))
        self.AudioInputPushButton.setObjectName("AudioInputPushButton")
        self.SaveData = QtWidgets.QPushButton(parent=ProductAdd)
        self.SaveData.setGeometry(QtCore.QRect(220, 70, 81, 21))
        self.SaveData.setObjectName("SaveData")

        self.retranslateUi(ProductAdd)
        QtCore.QMetaObject.connectSlotsByName(ProductAdd)

    def retranslateUi(self, ProductAdd):
        _translate = QtCore.QCoreApplication.translate
        ProductAdd.setWindowTitle(_translate("ProductAdd", "Form"))
        self.labelProductName.setText(_translate("ProductAdd", "Product Name"))
        self.labelProductCategory.setText(_translate("ProductAdd", "Product Category"))
        self.labelProductDescription.setText(_translate("ProductAdd", "Product Description"))
        self.DeleteData.setText(_translate("ProductAdd", "Delete"))
        self.AudioInputPushButton.setText(_translate("ProductAdd", "Audio Input"))
        self.SaveData.setText(_translate("ProductAdd", "Save"))
