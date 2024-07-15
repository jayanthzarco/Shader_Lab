from PySide6 import QtWidgets
from shader_lab.maya_commands import MayaCmds


class ListWID(QtWidgets.QListWidget):
    def __init__(self):
        super().__init__()

    def populate_data(self, data, clear=False):
        if clear:
            self.clear()
        for item in data:
            self.addItem(item)


class ExportLAB(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        # main layout
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        # list wid section1
        self.section1 = QtWidgets.QWidget()
        self.section1_layout = QtWidgets.QHBoxLayout(self.section1)
        self.list_wid = ListWID()
        self.section1_layout.addWidget(self.list_wid)

        self.layout.addWidget(self.section1)

        # load button section2
        self.section2 = QtWidgets.QWidget()
        self.section2_layout = QtWidgets.QHBoxLayout(self.section2)

        self.load_button = QtWidgets.QPushButton("LOAD")
        self.load_all_button = QtWidgets.QPushButton("LOAD ALL")
        self.radio_hi = QtWidgets.QRadioButton("Hierarchy")
        self.clear_btn = QtWidgets.QPushButton("CLEAR")

        self.section2_layout.addWidget(self.load_button)
        self.section2_layout.addWidget(self.radio_hi)
        self.section2_layout.addWidget(self.load_all_button)
        self.section2_layout.addWidget(self.clear_btn)

        self.layout.addWidget(self.section2)

        # export button section3
        self.section3 = QtWidgets.QWidget()
        self.section3_layout = QtWidgets.QHBoxLayout(self.section3)
        self.export_button = QtWidgets.QPushButton("EXPORT")
        self.export_group_button = QtWidgets.QPushButton("EXPORT AS GROUP")

        self.section3_layout.addWidget(self.export_button)
        self.section3_layout.addWidget(self.export_group_button)

        self.layout.addWidget(self.section3)

        # maya cmds
        self.maya = MayaCmds()
        # connection
        self._connection()
        # css_ids
        self.css_id_section()

    def _load_function(self):
        if self.radio_hi.isChecked():
            hierarchy = True
        else:
            hierarchy = False
        self.input_data = self.maya.return_shaders(hi=hierarchy, scene=False)
        self.list_wid.populate_data(data=self.input_data, clear=False)

    def _load_all_function(self):
        self.list_wid.clear()
        self.input_data = self.maya.return_shaders(scene=True)
        self.list_wid.populate_data(data=self.input_data, clear=True)

    def _export_function(self):
        print("exporting ...")
        self.maya.export_shaders(group=False)

    def _export_all_function(self):
        print("exporting everthing")
        self.maya.export_shaders(group=True)

    def _connection(self):
        self.load_button.clicked.connect(self._load_function)
        self.load_all_button.clicked.connect(self._load_all_function)
        self.export_button.clicked.connect(self._export_function)
        self.export_group_button.clicked.connect(self._export_all_function)
        self.clear_btn.clicked.connect(self.list_wid.clear)

    def css_id_section(self):
        self.central_widget.setProperty("class", "central_widget")
        self.section1.setProperty("class", "section1")
        self.list_wid.setProperty("class", "list_wid")
        self.section2.setProperty("class", "section2")
        self.load_button.setProperty("class", "load_button")
        self.radio_hi.setProperty("class", "radio_hi")
        self.load_all_button.setProperty("class", "load_all_button")
        self.section3.setProperty("class", "section3")
        self.export_button.setProperty("class", "export")
        self.export_group_button.setProperty("class", "export_as_group")
        self.clear_btn.setProperty("class", "clear")


def _run():
    print("Running...")
    app = QtWidgets.QApplication([])
    win = ExportLAB()
    with open("D:/Jayanth/Maya/shader_lab/shader_lab/ui/export_lab_style.css", "r") as file:
        win.setStyleSheet(file.read())
    win.show()
    app.exec_()


# _run()