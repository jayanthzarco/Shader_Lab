from PySide6 import QtWidgets, QtCore
from shader_lab.ui.export_lab_ui import ExportLAB
from shader_lab.ui.shader_trasfer_ui import ShaderTransferUI
# import maya.OpenMayaUI as omui
# from shiboken2 import wrapInstance


# def get_maya_main_window():
#     maya_win = omui.MQtUtil.mainWindow()
#     return wrapInstance(int(maya_win), QtWidgets.QWidget)


class UI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SHADER_LAB")
        self.wid1 = ExportLAB()
        self.wid2 = ShaderTransferUI()

        # with open("D:/git/zarco___/shader_lab/shader_lab/ui/export_lab_style.css", "r") as file:
        #     self.wid1.setStyleSheet(file.read())
        self.tab1 = QtWidgets.QTabWidget()
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.tab1)
        self.tab1.addTab(self.wid1, "Export_Lab")
        self.tab1.addTab(self.wid2, "Shader_Transfer")
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = UI()
    # win.setParent(get_maya_main_window(), QtCore.Qt.Window)
    win.show()
    app.exec_()
