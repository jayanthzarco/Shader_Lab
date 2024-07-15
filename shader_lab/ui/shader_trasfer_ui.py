from PySide6 import QtWidgets
from shader_lab.maya_commands import MayaCmds


class SourceListWID(QtWidgets.QListWidget):
    def __init__(self):
        super().__init__()

    def populate_data(self, data, clear=True):
        if clear:
            self.clear()
        for item in data:
            if "|" in item:
                self.addItem(data.spilt("|")[-1])
            else:
                self.addItem(item)


class DestListWID(QtWidgets.QListWidget):
    def __init__(self):
        super().__init__()

    def populate_data(self, data, clear=True):
        if clear:
            self.clear()
        for item in data:
            self.addItem(item)


class ShaderTransferUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        # main_layout
        self.main_layout = QtWidgets.QVBoxLayout(self.central_widget)

        # list wid layout
        self.list_layout = QtWidgets.QHBoxLayout()

        # source list wid
        self.section1 = QtWidgets.QWidget()
        self.section1_layout = QtWidgets.QVBoxLayout(self.section1)
        self.source_list_wid = SourceListWID()
        self.section1_layout.addWidget(self.source_list_wid)

        # source btn layout
        self.source_h_btn_layout = QtWidgets.QHBoxLayout()
        self.source_h_btn = QtWidgets.QPushButton("LOAD")
        self.source_radio_btn = QtWidgets.QRadioButton("Hierarchy")
        self.source_clear_btn = QtWidgets.QPushButton("CLEAR")

        self.source_h_btn_layout.addWidget(self.source_h_btn)
        self.source_h_btn_layout.addWidget(self.source_radio_btn)
        self.source_h_btn_layout.addWidget(self.source_clear_btn)

        # adding layout to source list
        self.section1_layout.addLayout(self.source_h_btn_layout)
        self.list_layout.addWidget(self.section1)

        # dest list wid
        self.section2 = QtWidgets.QWidget()
        self.section2_layout = QtWidgets.QVBoxLayout(self.section2)
        self.dest_list_wid = DestListWID()
        self.section2_layout.addWidget(self.dest_list_wid)
        self.list_layout.addWidget(self.section2)

        # destination button layout
        self.dest_h_btn_layout = QtWidgets.QHBoxLayout()
        self.dest_h_btn = QtWidgets.QPushButton("LOAD")
        self.dest_radio_btn = QtWidgets.QRadioButton("HIERARCHY")
        self.dest_clear_btn = QtWidgets.QPushButton("CLEAR")

        self.dest_h_btn_layout.addWidget(self.dest_h_btn)
        self.dest_h_btn_layout.addWidget(self.dest_radio_btn)
        self.dest_h_btn_layout.addWidget(self.dest_clear_btn)

        # adding layout to dest list
        self.section2_layout.addLayout(self.dest_h_btn_layout)
        self.main_layout.addLayout(self.list_layout)

        # adding option and transfer to the ui
        self.radio_h_btn_layout = QtWidgets.QHBoxLayout()
        self.uv_radio_btn = QtWidgets.QCheckBox("UV")
        self.txt_radio_btn = QtWidgets.QCheckBox("Texture")
        self.transfer_btn = QtWidgets.QPushButton("Transfer")
        self.status_bar = QtWidgets.QProgressBar()
        self.status_bar.setValue(20)
        self.radio_h_btn_layout.addWidget(self.uv_radio_btn)
        self.radio_h_btn_layout.addWidget(self.txt_radio_btn)
        self.radio_h_btn_layout.addWidget(self.status_bar)
        self.radio_h_btn_layout.addWidget(self.transfer_btn)
        # adding selection option ot main layout
        self.main_layout.addLayout(self.radio_h_btn_layout)

        # maya cmds
        self.maya = MayaCmds()

        # connection
        self._connection()

    def _connection(self):
        self.source_h_btn.clicked.connect(self._source_load)
        self.source_clear_btn.clicked.connect(self.source_list_wid.clear)
        self.dest_h_btn.clicked.connect(self._dest_load)
        self.dest_clear_btn.clicked.connect(self.dest_list_wid.clear)
        self.transfer_btn.clicked.connect(self._transfer)

    def _source_load(self):
        if self.source_radio_btn.isChecked():
            hierarchy = True
        else:
            hierarchy = False
        self.input_data = self.maya.return_selection(hierarchy=hierarchy)
        self.source_list_wid.populate_data(data=self.input_data, clear=True)

    def _dest_load(self):
        print("DESTINATION LOADING ..")

    def _transfer(self):
        print("TRANSFERRING")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = ShaderTransferUI()
    win.show()
    app.exec_()
