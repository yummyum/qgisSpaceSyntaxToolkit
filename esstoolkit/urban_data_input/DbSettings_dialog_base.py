# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DbSettings_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DbSettingsDialogBase(object):
    def setupUi(self, DbSettingsDialogBase):
        DbSettingsDialogBase.setObjectName("DbSettingsDialogBase")
        DbSettingsDialogBase.resize(285, 166)
        self.layoutWidget = QtWidgets.QWidget(DbSettingsDialogBase)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.dbCombo = QtWidgets.QComboBox(self.layoutWidget)
        self.dbCombo.setObjectName("dbCombo")
        self.gridLayout.addWidget(self.dbCombo, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.schemaCombo = QtWidgets.QComboBox(self.layoutWidget)
        self.schemaCombo.setObjectName("schemaCombo")
        self.gridLayout.addWidget(self.schemaCombo, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.nameLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.nameLineEdit.setText("")
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.gridLayout.addWidget(self.nameLineEdit, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okButton = QtWidgets.QPushButton(self.layoutWidget)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DbSettingsDialogBase)
        QtCore.QMetaObject.connectSlotsByName(DbSettingsDialogBase)

    def retranslateUi(self, DbSettingsDialogBase):
        _translate = QtCore.QCoreApplication.translate
        DbSettingsDialogBase.setWindowTitle(_translate("DbSettingsDialogBase", "DbSettings"))
        self.label_5.setText(_translate("DbSettingsDialogBase", "database"))
        self.label_6.setText(_translate("DbSettingsDialogBase", "schema"))
        self.label_7.setText(_translate("DbSettingsDialogBase", "table name"))
        self.okButton.setText(_translate("DbSettingsDialogBase", "OK"))
