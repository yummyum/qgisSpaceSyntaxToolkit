# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/petros/Projects/SpaceSyntaxToolkit/code/qgisSpaceSyntaxToolkit/esstoolkit/analysis/engines/DepthmapNet/ui_DepthmapNetSettingsWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DepthmapNetSettingsWidget(object):
    def setupUi(self, axialDepthmapTab):
        axialDepthmapTab.setObjectName("axialDepthmapTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(axialDepthmapTab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.axialDepthmapAnalysisLayout = QtWidgets.QHBoxLayout()
        self.axialDepthmapAnalysisLayout.setObjectName("axialDepthmapAnalysisLayout")
        self.verticalLayout.addLayout(self.axialDepthmapAnalysisLayout)
        self.axialDepthmapSettingsLayout = QtWidgets.QGridLayout()
        self.axialDepthmapSettingsLayout.setObjectName("axialDepthmapSettingsLayout")
        self.axialDepthmapAxialRadio = QtWidgets.QRadioButton(axialDepthmapTab)
        self.axialDepthmapAxialRadio.setChecked(True)
        self.axialDepthmapAxialRadio.setObjectName("axialDepthmapAxialRadio")
        self.axialDepthmapSettingsLayout.addWidget(self.axialDepthmapAxialRadio, 0, 0, 1, 1)
        self.axialDepthmapSegmentRadio = QtWidgets.QRadioButton(axialDepthmapTab)
        self.axialDepthmapSegmentRadio.setObjectName("axialDepthmapSegmentRadio")
        self.axialDepthmapSettingsLayout.addWidget(self.axialDepthmapSegmentRadio, 0, 1, 1, 2)
        self.axialDepthmapSettingsButton = QtWidgets.QPushButton(axialDepthmapTab)
        self.axialDepthmapSettingsButton.setObjectName("axialDepthmapSettingsButton")
        self.axialDepthmapSettingsLayout.addWidget(self.axialDepthmapSettingsButton, 0, 3, 1, 1)
        self.line = QtWidgets.QFrame(axialDepthmapTab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.axialDepthmapSettingsLayout.addWidget(self.line, 1, 0, 1, 4)
        self.axialDepthmapAnalysisLayout1 = QtWidgets.QHBoxLayout()
        self.axialDepthmapAnalysisLayout1.setSpacing(0)
        self.axialDepthmapAnalysisLayout1.setObjectName("axialDepthmapAnalysisLayout1")
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.axialDepthmapAnalysisLayout1.addItem(spacerItem)
        self.axialDepthmapRadiusLabel = QtWidgets.QLabel(axialDepthmapTab)
        self.axialDepthmapRadiusLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.axialDepthmapRadiusLabel.setObjectName("axialDepthmapRadiusLabel")
        self.axialDepthmapAnalysisLayout1.addWidget(self.axialDepthmapRadiusLabel)
        self.axialDepthmapSettingsLayout.addLayout(self.axialDepthmapAnalysisLayout1, 2, 0, 1, 1)
        self.axialDepthmapRadiusText = QtWidgets.QLineEdit(axialDepthmapTab)
        self.axialDepthmapRadiusText.setObjectName("axialDepthmapRadiusText")
        self.axialDepthmapSettingsLayout.addWidget(self.axialDepthmapRadiusText, 2, 1, 1, 3)
        self.axialDepthmapWeightCheck = QtWidgets.QCheckBox(axialDepthmapTab)
        self.axialDepthmapWeightCheck.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.axialDepthmapWeightCheck.setObjectName("axialDepthmapWeightCheck")
        self.axialDepthmapSettingsLayout.addWidget(self.axialDepthmapWeightCheck, 3, 0, 1, 1)
        self.axialDepthmapWeightCombo = QtWidgets.QComboBox(axialDepthmapTab)
        self.axialDepthmapWeightCombo.setObjectName("axialDepthmapWeightCombo")
        self.axialDepthmapSettingsLayout.addWidget(self.axialDepthmapWeightCombo, 3, 1, 1, 3)
        self.axialDepthmapAnalysisLayout2 = QtWidgets.QHBoxLayout()
        self.axialDepthmapAnalysisLayout2.setSpacing(0)
        self.axialDepthmapAnalysisLayout2.setObjectName("axialDepthmapAnalysisLayout2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.axialDepthmapAnalysisLayout2.addItem(spacerItem1)
        self.axialDepthmapRadiusLabel1 = QtWidgets.QLabel(axialDepthmapTab)
        self.axialDepthmapRadiusLabel1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.axialDepthmapRadiusLabel1.setObjectName("axialDepthmapRadiusLabel1")
        self.axialDepthmapAnalysisLayout2.addWidget(self.axialDepthmapRadiusLabel1)
        self.axialDepthmapSettingsLayout.addLayout(self.axialDepthmapAnalysisLayout2, 4, 0, 1, 1)
        self.axialDepthmapOutputText = QtWidgets.QLineEdit(axialDepthmapTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axialDepthmapOutputText.sizePolicy().hasHeightForWidth())
        self.axialDepthmapOutputText.setSizePolicy(sizePolicy)
        self.axialDepthmapOutputText.setObjectName("axialDepthmapOutputText")
        self.axialDepthmapSettingsLayout.addWidget(self.axialDepthmapOutputText, 4, 1, 1, 3)
        self.verticalLayout.addLayout(self.axialDepthmapSettingsLayout)
        self.axialDepthmapDownload = QtWidgets.QLabel(axialDepthmapTab)
        self.axialDepthmapDownload.setAlignment(QtCore.Qt.AlignRight)
        self.axialDepthmapDownload.setOpenExternalLinks(True)
        self.axialDepthmapDownload.setObjectName("axialDepthmapDownload")
        self.verticalLayout.addWidget(self.axialDepthmapDownload)

        self.retranslateUi(axialDepthmapTab)

    def retranslateUi(self, axialDepthmapTab):
        _translate = QtCore.QCoreApplication.translate
        self.axialDepthmapAxialRadio.setText(_translate("DepthmapNetSettingsWidget", "Axial"))
        self.axialDepthmapSegmentRadio.setText(_translate("DepthmapNetSettingsWidget", "Segment"))
        self.axialDepthmapSettingsButton.setText(_translate("DepthmapNetSettingsWidget", "Settings"))
        self.axialDepthmapRadiusLabel.setText(_translate("DepthmapNetSettingsWidget", "Radius:"))
        self.axialDepthmapRadiusText.setText(_translate("DepthmapNetSettingsWidget", "2,4,n"))
        self.axialDepthmapWeightCheck.setText(_translate("DepthmapNetSettingsWidget", "Weight:"))
        self.axialDepthmapRadiusLabel1.setText(_translate("DepthmapNetSettingsWidget", "Output table:"))
        self.axialDepthmapDownload.setToolTip(_translate("DepthmapNetSettingsWidget", "https://varoudis.github.io/depthmapX/"))
        self.axialDepthmapDownload.setText(_translate("DepthmapNetSettingsWidget", "<qt><a href=\"http://archtech.gr/varoudis/depthmapX/?dir=depthmapXnet\"><span style=\" text-decoration: underline; color:#0000ff;\">Download depthmapXnet...</a></qt>"))
