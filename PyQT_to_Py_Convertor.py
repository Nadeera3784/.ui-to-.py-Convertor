from PyQt4 import QtCore, QtGui
import sys
import os

class AppUI(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AppUI, self).__init__(parent)
        
        self.menuBar = QtGui.QMenuBar()
        self.menuBar.setStyleSheet("background-color: #E1E6F6; color: #20232C; border-image: none; border-style: none;")
        self.fileMenu = QtGui.QMenu("&Help", self)
        self.fileMenu.setStyleSheet("background-color: #E1E6F6;color: #20232C;")
        self.fileMenu.addAction("About Qt Convertor", self.about)
        self.menuBar.addMenu(self.fileMenu)
        
        frameStyle = QtGui.QFrame.Sunken | QtGui.QFrame.Panel
        
        self.nameLabel = QtGui.QLabel("Select Qt File:")
        self.nameLabel.setStyleSheet("color: #20232C;")
        self.directoryComboBox = self.createComboBox(QtCore.QDir.currentPath())
        self.browseButton = QtGui.QPushButton("&Browse")
        self.browseButton.clicked.connect(self.getOpenFileName)

        self.emptyLabel = QtGui.QLabel()
        self.emptyLabel.setFrameStyle(frameStyle)
        self.emptyLabel.show()
        
        self.saveLabel = QtGui.QLabel("Save as:")
        self.saveLabel.setStyleSheet("color: #20232C;")
        self.saveComboBox = self.createComboBox()
        self.saveComboBox.setStyleSheet("color: #20232C;")
        self.saveComboBox.hide()
        self.saveButton = QtGui.QPushButton("&Save")
        self.saveButton.clicked.connect(self.getSaveFileName)
        
        self.convertButton = QtGui.QPushButton("&Convert Now")
        self.convertButton.clicked.connect(self.initConvert)
        #self.convertButton.setEnabled(True)
        
        buttonLayout_01 = QtGui.QHBoxLayout()
        buttonLayout_01.addWidget(self.browseButton)
        buttonLayout_01.addStretch()

        buttonLayout_02 = QtGui.QHBoxLayout()
        buttonLayout_02.addWidget(self.saveButton)
        buttonLayout_02.addStretch()

        mainLayout = QtGui.QGridLayout()
    
        mainLayout.setMenuBar(self.menuBar)
        mainLayout.addWidget(self.nameLabel, 0, 0)
        mainLayout.addWidget(self.directoryComboBox, 0, 1)
        mainLayout.addLayout(buttonLayout_01, 0, 2)
        mainLayout.addWidget(self.saveLabel, 1, 0, QtCore.Qt.AlignTop)
        mainLayout.addWidget(self.saveComboBox, 1, 1)
        mainLayout.addWidget(self.emptyLabel, 1, 1)
        mainLayout.addLayout(buttonLayout_02, 1, 2)
        mainLayout.addWidget(self.convertButton, 2, 1)
        
        self.setLayout(mainLayout)
        
        self.setWindowTitle("QT to Py Convertor")
        self.setWindowIcon(QtGui.QIcon(':/images/logo.png'))
        #self.setStyleSheet("background-color: #E1E6F6;")
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        
    def createComboBox(self, text=""):
        comboBox = QtGui.QComboBox()
        comboBox.setEditable(True)
        comboBox.addItem(text)
        comboBox.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        return comboBox
            
    def getOpenFileName(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, caption="Open", filter="Designer UI Files (*.ui)")
        if fileName :
            if self.directoryComboBox.findText(fileName) == -1:
                self.directoryComboBox.addItem(fileName)

            self.directoryComboBox.setCurrentIndex(self.directoryComboBox.findText(fileName))
            
    def getSaveFileName(self):
       fileName = QtGui.QFileDialog.getSaveFileName(self, "Save As", filter="Python Files (*.py)")
       if fileName :
           self.saveComboBox.show()
           if self.saveComboBox.findText(fileName) == -1:
               self.saveComboBox.addItem(fileName)
               self.saveComboBox.setCurrentIndex(self.saveComboBox.findText(fileName))
       else :
           self.emptyLabel.hide()
           
    def initConvert(self):
        directory = self.directoryComboBox.currentText()
        save = self.saveComboBox.currentText()
        if directory == "" or save == "":
            QtGui.QMessageBox.critical(self, "Error", "Please select .ui file path and save path")
        else:
            os.system("pyuic4 -x " + directory + " -o " + save )
            QtGui.QMessageBox.information(self, "Success", "Done!!!")
        
    def about(self):
        QtGui.QMessageBox.about(self, "About", "Simple Application to Convert QT(.ui) files to .py")


  

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)

    App = AppUI()
    
    App.show()
    import pydoc 
    sys.exit(app.exec_())
