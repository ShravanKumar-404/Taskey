from PyQt5 import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import sys
import os
import winapps

interface, _ = uic.loadUiType('task.ui')


class MainApp(QMainWindow, interface):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui()
        self.buttons()
        self.tabs.tabBar().setVisible(False)

    def ui(self):
        self.tabs.setCurrentIndex(0)
        self.setFixedSize(630, 500)

    def buttons(self):
        self.runningbutton.clicked.connect(self.running_apps)
        self.app_other_button.clicked.connect(self.apps_and_other)
        self.historybutton.clicked.connect(self.history)

        self.app_other_remove.clicked.connect(self.apps_and_other_remove)
        self.app_other_remove_all.clicked.connect(
            self.apps_and_other_remove_all)
        self.app_other_open.clicked.connect(self.apps_and_other_open)
        self.app_other_add.clicked.connect(self.apps_and_other_add)

        self.recents_selectall.clicked.connect(self.recents_all)
        self.recents_add.clicked.connect(self.recents_adds)
        self.recents_open.clicked.connect(self.recents_opens)

    ########### Running ############

    def running_apps(self):
        self.tabs.setCurrentIndex(0)

    ########## Appliccations ###########

    apps = []
    to_open_apps = []

    def apps_and_other(self):
        self.tabs.setCurrentIndex(1)

    def apps_and_other_add(self):
        self.apps_other_status.setText('')

        location = QFileDialog.getOpenFileName(
            self, 'Add Files', filter=("All Files(*.*);;Executables(*.exe);;Text Files(*.txt)"))
        self.apps_other_list.addItem(f'{location[0]}')

        self.apps_other_selected_number.setText(
            str(self.apps_other_list.count()))

    def apps_and_other_remove(self):
        for item in self.apps_other_list.selectedItems():
            self.apps_other_list.takeItem(self.apps_other_list.row(item))

        self.apps_other_selected_number.setText(
            str(self.apps_other_list.count()))

    def apps_and_other_remove_all(self):
        self.apps_other_list.clear()

        self.apps_other_selected_number.setText(
            str(self.apps_other_list.count()))

    def apps_and_other_open(self):
        all_items = [str(self.apps_other_list.item(
            index).text()) for index in range(self.apps_other_list.count())]

        print(all_items)

        if all_items == []:
            self.apps_other_status.setText('Please Add Files')
        else:
            for app in all_items:
                os.startfile(app)

        ########## Recents ##############

    def recents_apps(self):
        self.tabs.setCurrentIndex(2)

    def recents_adds(self):
        pass

    def recents_opens(self):
        pass

    def recents_closes(self):
        pass

    def recents_all(self):
        pass


def main():
    apps = QApplication(sys.argv)
    window = MainApp()
    window.show()
    apps.exec_()


if __name__ == "__main__":
    main()
