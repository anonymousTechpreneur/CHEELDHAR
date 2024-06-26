# Form implementation generated from reading ui file '.\UI Designs\Inventory Add UI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background:rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SaveData = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SaveData.setGeometry(QtCore.QRect(10, 330, 81, 21))
        self.SaveData.setObjectName("SaveData")
        self.DeleteData = QtWidgets.QPushButton(parent=self.centralwidget)
        self.DeleteData.setGeometry(QtCore.QRect(700, 320, 81, 24))
        self.DeleteData.setObjectName("DeleteData")
        self.AudioInputPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.AudioInputPushButton.setGeometry(QtCore.QRect(370, 320, 81, 31))
        self.AudioInputPushButton.setObjectName("AudioInputPushButton")
        self.labelProductName = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelProductName.setGeometry(QtCore.QRect(10, 0, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelProductName.setFont(font)
        self.labelProductName.setObjectName("labelProductName")
        self.textEditHSNNo = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEditHSNNo.setGeometry(QtCore.QRect(240, 260, 181, 31))
        self.textEditHSNNo.setObjectName("textEditHSNNo")
        self.ProductDetailcomboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.ProductDetailcomboBox.setGeometry(QtCore.QRect(10, 30, 271, 31))
        self.ProductDetailcomboBox.setObjectName("ProductDetailcomboBox")
        self.ProductDetailcomboBox.addItem("")
        self.pushButtonAddProduct = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAddProduct.setGeometry(QtCore.QRect(300, 30, 101, 31))
        self.pushButtonAddProduct.setObjectName("pushButtonAddProduct")
        self.labelHSNNo = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelHSNNo.setGeometry(QtCore.QRect(240, 230, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelHSNNo.setFont(font)
        self.labelHSNNo.setObjectName("labelHSNNo")
        self.textEditQuantity = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEditQuantity.setGeometry(QtCore.QRect(10, 110, 141, 31))
        self.textEditQuantity.setObjectName("textEditQuantity")
        self.labelQuantity = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelQuantity.setGeometry(QtCore.QRect(10, 80, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelQuantity.setFont(font)
        self.labelQuantity.setObjectName("labelQuantity")
        self.labelQuantity_Unit = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelQuantity_Unit.setGeometry(QtCore.QRect(170, 80, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelQuantity_Unit.setFont(font)
        self.labelQuantity_Unit.setObjectName("labelQuantity_Unit")
        self.textEditQuantity_Unit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEditQuantity_Unit.setGeometry(QtCore.QRect(170, 110, 81, 31))
        self.textEditQuantity_Unit.setObjectName("textEditQuantity_Unit")
        self.labelMFD = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelMFD.setGeometry(QtCore.QRect(280, 80, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelMFD.setFont(font)
        self.labelMFD.setObjectName("labelMFD")
        self.labelExpiry = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelExpiry.setGeometry(QtCore.QRect(430, 80, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelExpiry.setFont(font)
        self.labelExpiry.setObjectName("labelExpiry")
        self.dateEditMFD = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEditMFD.setGeometry(QtCore.QRect(280, 110, 121, 31))
        self.dateEditMFD.setObjectName("dateEditMFD")
        self.dateEditExpiry = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEditExpiry.setGeometry(QtCore.QRect(430, 110, 111, 31))
        self.dateEditExpiry.setObjectName("dateEditExpiry")
        self.dateEditBill = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEditBill.setGeometry(QtCore.QRect(560, 110, 111, 31))
        self.dateEditBill.setObjectName("dateEditBill")
        self.labelBillDate = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelBillDate.setGeometry(QtCore.QRect(560, 80, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelBillDate.setFont(font)
        self.labelBillDate.setObjectName("labelBillDate")
        self.labelPurchaseValue = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelPurchaseValue.setGeometry(QtCore.QRect(10, 160, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelPurchaseValue.setFont(font)
        self.labelPurchaseValue.setObjectName("labelPurchaseValue")
        self.textEditPurchaseValue = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEditPurchaseValue.setGeometry(QtCore.QRect(10, 190, 141, 31))
        self.textEditPurchaseValue.setObjectName("textEditPurchaseValue")
        self.textEditOtherCost = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEditOtherCost.setGeometry(QtCore.QRect(170, 190, 141, 31))
        self.textEditOtherCost.setObjectName("textEditOtherCost")
        self.labelOtherCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelOtherCost.setGeometry(QtCore.QRect(170, 160, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelOtherCost.setFont(font)
        self.labelOtherCost.setObjectName("labelOtherCost")
        self.textEditMinSellPrice = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEditMinSellPrice.setGeometry(QtCore.QRect(330, 190, 141, 31))
        self.textEditMinSellPrice.setObjectName("textEditMinSellPrice")
        self.labelMinSellPrice = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelMinSellPrice.setGeometry(QtCore.QRect(330, 160, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelMinSellPrice.setFont(font)
        self.labelMinSellPrice.setObjectName("labelMinSellPrice")
        self.textEditMaxSellPrice = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEditMaxSellPrice.setGeometry(QtCore.QRect(490, 190, 141, 31))
        self.textEditMaxSellPrice.setObjectName("textEditMaxSellPrice")
        self.labelMaxSellPrice = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelMaxSellPrice.setGeometry(QtCore.QRect(490, 160, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelMaxSellPrice.setFont(font)
        self.labelMaxSellPrice.setObjectName("labelMaxSellPrice")
        self.pushButtonAddSuplier = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAddSuplier.setGeometry(QtCore.QRect(700, 30, 101, 31))
        self.pushButtonAddSuplier.setObjectName("pushButtonAddSuplier")
        self.labelSuplierName = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelSuplierName.setGeometry(QtCore.QRect(410, 0, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelSuplierName.setFont(font)
        self.labelSuplierName.setObjectName("labelSuplierName")
        self.SuplierDetailcomboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.SuplierDetailcomboBox.setGeometry(QtCore.QRect(410, 30, 271, 31))
        self.SuplierDetailcomboBox.setObjectName("SuplierDetailcomboBox")
        self.SuplierDetailcomboBox.addItem("")
        self.labelApplicableGST = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelApplicableGST.setGeometry(QtCore.QRect(640, 160, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelApplicableGST.setFont(font)
        self.labelApplicableGST.setObjectName("labelApplicableGST")
        self.textEditApplicableGST = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEditApplicableGST.setGeometry(QtCore.QRect(640, 190, 141, 31))
        self.textEditApplicableGST.setObjectName("textEditApplicableGST")
        self.labelPurchaseBill = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelPurchaseBill.setGeometry(QtCore.QRect(10, 230, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelPurchaseBill.setFont(font)
        self.labelPurchaseBill.setObjectName("labelPurchaseBill")
        self.textEditPurchaseBill = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEditPurchaseBill.setGeometry(QtCore.QRect(10, 260, 211, 31))
        self.textEditPurchaseBill.setObjectName("textEditPurchaseBill")
        self.labelFirmAttach = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelFirmAttach.setGeometry(QtCore.QRect(440, 230, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelFirmAttach.setFont(font)
        self.labelFirmAttach.setObjectName("labelFirmAttach")
        self.FirmDetailcomboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.FirmDetailcomboBox.setGeometry(QtCore.QRect(440, 260, 341, 31))
        self.FirmDetailcomboBox.setObjectName("FirmDetailcomboBox")
        self.FirmDetailcomboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuHome = QtWidgets.QMenu(parent=self.menubar)
        self.menuHome.setObjectName("menuHome")
        self.menuInventory_Add = QtWidgets.QMenu(parent=self.menubar)
        self.menuInventory_Add.setObjectName("menuInventory_Add")
        self.menuInventory_Check = QtWidgets.QMenu(parent=self.menubar)
        self.menuInventory_Check.setObjectName("menuInventory_Check")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuInventory_Add.menuAction())
        self.menubar.addAction(self.menuInventory_Check.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SaveData.setText(_translate("MainWindow", "Save"))
        self.DeleteData.setText(_translate("MainWindow", "Delete"))
        self.AudioInputPushButton.setText(_translate("MainWindow", "Audio Input"))
        self.labelProductName.setText(_translate("MainWindow", "Product Name"))
        self.ProductDetailcomboBox.setItemText(0, _translate("MainWindow", "Product Detail"))
        self.pushButtonAddProduct.setText(_translate("MainWindow", "Add Product"))
        self.labelHSNNo.setText(_translate("MainWindow", "HSN No."))
        self.labelQuantity.setText(_translate("MainWindow", "Quantity"))
        self.labelQuantity_Unit.setText(_translate("MainWindow", "Quantity Unit"))
        self.labelMFD.setText(_translate("MainWindow", "Manufacturing Date"))
        self.labelExpiry.setText(_translate("MainWindow", "Expiry Date"))
        self.labelBillDate.setText(_translate("MainWindow", "Bill Date"))
        self.labelPurchaseValue.setText(_translate("MainWindow", "Purchase Value Per Unit"))
        self.labelOtherCost.setText(_translate("MainWindow", "Other Cost Per Unit"))
        self.labelMinSellPrice.setText(_translate("MainWindow", "Min Selling Value"))
        self.labelMaxSellPrice.setText(_translate("MainWindow", "Max Selling Value"))
        self.pushButtonAddSuplier.setText(_translate("MainWindow", "Add Suplier"))
        self.labelSuplierName.setText(_translate("MainWindow", "Suplier Name"))
        self.SuplierDetailcomboBox.setItemText(0, _translate("MainWindow", "Suplier Detail"))
        self.labelApplicableGST.setText(_translate("MainWindow", "Applicable GST"))
        self.labelPurchaseBill.setText(_translate("MainWindow", "Purchase Bill Detail"))
        self.labelFirmAttach.setText(_translate("MainWindow", "Firm Attach"))
        self.FirmDetailcomboBox.setItemText(0, _translate("MainWindow", "Firm Detail"))
        self.menuHome.setTitle(_translate("MainWindow", "Home"))
        self.menuInventory_Add.setTitle(_translate("MainWindow", "Inventory Add"))
        self.menuInventory_Check.setTitle(_translate("MainWindow", "Inventory Check"))
