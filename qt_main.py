import sys
import os
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent = None) :
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.toolButton.clicked.connect(self.openFile)
        self.ui.pushButton.clicked.connect(self.rearrange)

    def openFile(self):
        file, _ = QFileDialog.getOpenFileName(self, "Open file", "", "MIDI files (*.mid)")
        if file:
            self.ui.lineEdit.setText(file)
           
    def rearrange(self):
        velocity_threshold = self.ui.spinBox.value()
        timeSpan_threshold = self.ui.spinBox_2.value()
        separate_threshold = self.ui.spinBox_3.value()
        continue_threshold = self.ui.spinBox_4.value()
        path = self.ui.lineEdit.text()
        from MIDIRearrange import param_check
        timeSpan_threshold,separate_threshold,msg_list = param_check(velocity_threshold,timeSpan_threshold,separate_threshold,continue_threshold,path)
        if len(msg_list)>0:
            QMessageBox.information(None,"这是一个信息框",'\r\n'.join(msg_list) )
        if(path is None or path == '' or os.path.exists(path) == False):
            QMessageBox.critical(None, "File Not Found", "没有找到midi文件哦，请选择midi文件(.mid)。")
            # print ('\r\nPlease select correct MIDI(.mid) file')
            return None

        from MIDIRearrange import midiRearrange
        msg = midiRearrange(velocity_threshold,timeSpan_threshold,separate_threshold,continue_threshold,path)
        QMessageBox.information(None,"这是一个信息框",msg)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle("MIDI Rearrange")
    win.show()
    app.exit(app.exec_())