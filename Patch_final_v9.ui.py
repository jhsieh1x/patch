# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Patch_final_v9.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os,time
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import *
import glob
import multiprocessing

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(597, 455)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 230, 571, 191))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 561, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 0, 2, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.lineEdit2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit2.setObjectName("lineEdit2")
        self.gridLayout.addWidget(self.lineEdit2, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 420, 131, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(270, 190, 305, 36))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 170, 91, 22))
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 51, 23))
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(70, 140, 246, 23))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_1.setObjectName("radioButton_1")
        self.horizontalLayout_2.addWidget(self.radioButton_1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(326, 140, 221, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 190, 120, 34))
        self.label_8.setObjectName("label_8")
        self.checkBox_9 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_9.setGeometry(QtCore.QRect(110, 200, 51, 16))
        self.checkBox_9.setObjectName("checkBox_9")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(110, 170, 463, 23))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_3.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_3.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_3.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_3.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout_3.addWidget(self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_7.setObjectName("checkBox_7")
        self.horizontalLayout_3.addWidget(self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_8.setObjectName("checkBox_8")
        self.horizontalLayout_3.addWidget(self.checkBox_8)
        global progress
        progress = self.progressBar
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_1.setText(_translate("Dialog", "..."))
        self.label_1.setText(_translate("Dialog", "Output :"))
        self.pushButton_2.setText(_translate("Dialog", "..."))
        self.label_3.setText(_translate("Dialog", "BIOS Folder:"))
        self.label_2.setText(_translate("Dialog", "IWFI :"))
        self.pushButton_3.setText(_translate("Dialog", "..."))
        self.label_4.setText(_translate("Dialog", "Single_BIOS:"))
        self.pushButton_4.setText(_translate("Dialog", "..."))
        self.pushButton_6.setText(_translate("Dialog", "Clear_Log"))
        self.pushButton_5.setText(_translate("Dialog", "Patch"))
        self.label_7.setText(_translate("Dialog", "BIOS_ROM Filter :"))
        self.label_5.setText(_translate("Dialog", "Code Base :"))
        self.radioButton_1.setText(_translate("Dialog", "All"))
        self.radioButton_2.setText(_translate("Dialog", "FSP"))
        self.radioButton_3.setText(_translate("Dialog", "EDK"))
        self.radioButton_4.setText(_translate("Dialog", "X_code"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">( Single_ BIOS skip this option)</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "Tool_Debug Mode :"))
        self.checkBox_9.setText(_translate("Dialog", "Enable"))
        self.checkBox.setText(_translate("Dialog", "All"))
        self.checkBox_2.setText(_translate("Dialog", "ICL"))
        self.checkBox_3.setText(_translate("Dialog", "Pro_ICL"))
        self.checkBox_4.setText(_translate("Dialog", "CFL"))
        self.checkBox_5.setText(_translate("Dialog", "Pro_CFL"))
        self.checkBox_6.setText(_translate("Dialog", "CNL"))
        self.checkBox_7.setText(_translate("Dialog", "Pro_CNL"))
        self.checkBox_8.setText(_translate("Dialog", "Single"))

    def pushbutton(self):
        self.pushButton_1.clicked.connect(self.output_dir)
        self.pushButton_2.clicked.connect(self.open_iwfi)
        self.pushButton_3.clicked.connect(self.bios_folder)
        self.pushButton_4.clicked.connect(self.single_file)
        self.pushButton_5.clicked.connect(self.patch)
        self.pushButton_6.clicked.connect(self.clear_log)
    def radio_button(self):
        self.radioButton_1.toggled.connect(self.code_base)
    def output_dir(self):
        global output_dir

        title = "Output Folder"
        path = "Y:/"
        options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(None,
                                                     title,
                                                     path, options=options)

        self.lineEdit_1.setText(str(directory))

        output_dir = str(directory)
        if str(directory) == "":
            self.textBrowser.append("Output folder no input")
        else:
            self.textBrowser.append("============== Output Folder =================")
            self.textBrowser.append("Output folder Path :")
            self.textBrowser.append(output_dir)

    def open_iwfi(self):
        # Open IWFI
        title = "IWFI File"
        path = ""
        file_type = "IWFI files (*.bin)"
        fname = QFileDialog.getOpenFileName(None, title, path, file_type)
        self.lineEdit2.setText(str(fname[0]))
        global iwfi_path
        iwfi_path = str(fname[0])

        # File Name
        global iwfi_name
        # Print File name
        iwfi_name = os.path.splitext(iwfi_path)[0]
        iwfi_name = os.path.basename(iwfi_name)
        self.textBrowser.append("============== IWFI Name =================")
        self.textBrowser.append("IWFI name: "+iwfi_name)

        # Get BIOS region begin offset address from IFWI BIN file offset 0x44 0x45.
        if iwfi_path == "":
          self.textBrowser.append("No input do nothing")

        else:

           with open(iwfi_path, 'rb') as ifwi_fileobj:
             ifwi_file = ifwi_fileobj.read()

           low_byte = ifwi_file[0x44]
           high_byte = ifwi_file[0x45]
           # ------------------ TEST -------------------------
           #self.textBrowser.append("Get BIOS region begin offset address from IFWI BIN file offset 0x44 0x45.")
           #self.textBrowser.append("offset 0x44: "+hex(low_byte))
           #self.textBrowser.append("offset 0x45: " + hex(high_byte))
           # ------------------ TEST END-------------------------
           bios_begin = (high_byte << 8) | low_byte
           bios_begin = bios_begin << 0x0C
           self.textBrowser.append("============== IWFI Information =================")
           self.textBrowser.append("BIOS Address from : "+hex(bios_begin))

           # Get BIOS region end offset address from IFWI BIN file offset 0x46 0x47.
           low_byte = ifwi_file[0x46]
           high_byte = ifwi_file[0x47]
           # ------------------ TEST -------------------------
           #self.textBrowser.append("Get BIOS region end offset address from IFWI BIN file offset 0x46 0x47")
           #self.textBrowser.append("offset 0x46: "+hex(low_byte))
           #self.textBrowser.append("offset 0x47: "+hex(high_byte))
           # ------------------ TEST END-------------------------

           bios_end = (high_byte << 8) | low_byte
           bios_end = (bios_end << 0x0C) | 0xFFF
           self.textBrowser.append("BIOS End Address : "+hex(bios_end))


           bios_len = bios_end - bios_begin + 1
           self.textBrowser.append("BIOS Length : "+hex(bios_len))
           self.textBrowser.append("IWFI Length : " +str( len(ifwi_file)))

    def single_file(self):
        # Open Single File
        title = "Joy"
        path = ""
        file_type = "BIOS Rom file (*.rom)"
        sfname = QFileDialog.getOpenFileName(None, title, path, file_type)
        self.lineEdit_4.setText(str(sfname[0]))
        global single_file
        single_file = str(sfname[0])
        self.textBrowser.append("============== Single File =================")
        self.textBrowser.append("Single BIOS file Path:")
        self.textBrowser.append(single_file)

    def checkbox_default(self):
        # self.checkBox.setChecked(True)
        #self.checkBox.stateChanged.connect(self.search_file)
        #self.checkBox_2.stateChanged.connect(self.search_file)
        #self.checkBox_3.stateChanged.connect(self.search_file)
        #self.checkBox_4.stateChanged.connect(self.search_file)
        #self.checkBox_5.stateChanged.connect(self.search_file)
        self.checkBox_9.stateChanged.connect(self.text)
        #self.checkBox_7.stateChanged.connect(self.search_file)

    def text(self):


        if self.checkBox_9.isChecked():


            self.checkBox_9.setText("Open")
            self.textBrowser.append("Debug_Mode Enable")
            Dialog.resize(600, 463)
            self.textBrowser.show()
        else:

            self.checkBox_9.setText("Close")
            Dialog.resize(600, 230)
            self.textBrowser.hide()

    def clear_log(self):
        self.textBrowser.setPlainText("")

    def bios_folder(self):
        options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(None,
                                                     "QFileDialog.getExistingDirectory()",
                                                     "", options=options)

        self.lineEdit_3.setText(str(directory))

        global bios_path
        bios_path = str(directory)

        if str(directory) == "":
                self.textBrowser.append("BIOS Rom folder no input")

        else:
                self.textBrowser.append("BIOS Rom Folder :")
                self.textBrowser.append(bios_path)


    def stitch(self, output, iwfi, BIOS_rom):
        progress.setValue(0)
        t1 = time.time()
        with open(iwfi, 'rb') as ifwi_fileobj:
            ifwi_file = ifwi_fileobj.read()
        with open(BIOS_rom, 'rb') as bios_fileobj:
            bios_file = bios_fileobj.read()

        # Get BIOS region begin offset address from IFWI BIN file offset 0x44 0x45.
        low_byte = ifwi_file[0x44]
        high_byte = ifwi_file[0x45]
        bios_begin = (high_byte << 8) | low_byte
        bios_begin = bios_begin << 0x0C

        # Get BIOS region end offset address from IFWI BIN file offset 0x46 0x47.
        low_byte = ifwi_file[0x46]
        high_byte = ifwi_file[0x47]
        bios_end = (high_byte << 8) | low_byte
        bios_end = (bios_end << 0x0C) | 0xFFF
        bios_len = bios_end - bios_begin + 1

        # Check if BIOS ROM file size matches BIOS region length in IFWI.
        if not (len(bios_file) == bios_len):
            print("The BIOS ROM file size does not match to BIOS region length descriptor in IFWI.")
            sys.exit(1)

        # Stich the BIOS ROM with IFWI BIN file.
        byte_index = 0
        combined_file = bytearray(len(ifwi_file))
        for index in range(bios_begin):
            combined_file[index] = ifwi_file[index]
            byte_index = byte_index + 1

        for byte in bios_file:
            combined_file[byte_index] = byte
            byte_index = byte_index + 1

        # Used IWFI Name create output folder
        output1 = output + "/" + iwfi_name + "_patched"
        print (output1)

        #self.textBrowser.append("Final Output Path" + output1)

        if not os.path.exists(output1):
            os.mkdir(output1)
        
        bios_name =os.path.splitext(BIOS_rom)[0]
        bios_name = os.path.basename(bios_name)
        print(bios_name)
        
        with open(output1 + "/" + bios_name + "_patched.bin", 'wb') as combined_fileobj:
            combined_fileobj.write(combined_file)

        t2 = time.time()
        cost_time = str(t2 - t1)
        print(cost_time)
        self.textBrowser.append("Spend " + cost_time + "finish patch")
        progress.setValue(100)

    def patch(self):

        if self.checkBox_8.isChecked():
            ui.stitch(output_dir, iwfi_path, single_file)

    def code_base(self):
        global fsp,edk,xcode

        if self.radioButton_1.isChecked():
            self.textBrowser.append("=================================")
            all = glob.glob(bios_path + '/*.rom')
            self.textBrowser.append("Total  rom file : " + str(len(all)))

            #  FSP
            fsp = []
            fsp_1 = glob.glob(bios_path + '/*FSP*.rom')
            self.textBrowser.append("===============FSP===============")
            for fsp_rom in fsp_1:
                fsp.append(fsp_rom)
                patch_file = os.path.splitext(fsp_rom)[0]
                patch_file = os.path.basename(patch_file)
                self.textBrowser.append(patch_file)
            self.textBrowser.append("=================================")
            self.textBrowser.append("Total FSP rom file : " + str(len(fsp_1)))

            #  EDK
            edk =[]
            edk_1 = glob.glob(bios_path + '/*EDK*.rom')
            edk_2 = [k for k in edk_1 if 'XCODE' not in k]
            self.textBrowser.append("===============EDK===============")
            for edk_rom in edk_2:
                edk.append(edk_rom)
                patch_file = os.path.splitext(edk_rom)[0]
                patch_file = os.path.basename(edk_rom)
                self.textBrowser.append(patch_file)
            self.textBrowser.append("=================================")
            self.textBrowser.append("Total EDK rom file : " + str(len(edk_2)))

            #  XCODE
            xcode = []
            xcode_1 = glob.glob(bios_path + '/*XCODE*.rom')
            self.textBrowser.append("===============XCODE===============")
            for xcode_rom in xcode_1:
                xcode.append(xcode_rom)
                patch_file = os.path.splitext(xcode_rom)[0]
                patch_file = os.path.basename(xcode_rom)
                self.textBrowser.append(patch_file)
            self.textBrowser.append("=================================")
            self.textBrowser.append("Total XCODE rom file : " + str(len(xcode_1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.pushbutton()
    ui.radio_button()
    ui.checkbox_default()
    ui.text()
    Dialog.show()

    sys.exit(app.exec_())
