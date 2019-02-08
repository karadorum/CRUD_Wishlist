import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import ui
import webbrowser
from db_setup import Database
db = Database()


class App(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def widget_content(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        rows = db.show_data()
        for row in rows:
            index = rows.index(row)
            self.tableWidget.insertRow(index)
            self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(row[2]))

    def add_row(self):
        rowPosition = self.tableWidget.rowCount()
        wish = self.ui.lineEdit.text()
        desc = self.ui.lineEdit_2.text()
        url = self.ui.lineEdit_3.text()
        if len(wish) > 0 and len(desc) > 0:
            db.insert_data(wish, desc, url)

        self.widget_content()

    def remove_row(self):
        rowid = self.tableWidget.currentRow()
        wish = self.tableWidget.item(rowid, 0).text()
        description = self.tableWidget.item(rowid, 1).text()
        url = self.tableWidget.item(rowid, 2).text()
        db.delete_row(wish, description, url)
        self.widget_content()

    def open_add_dialog(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = ui.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.ui.buttonBox.accepted.connect(self.add_row)
        self.Dialog.show()

    def open_update_dialog(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = ui.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        currentrow = self.tableWidget.currentRow()
        self.ui.lineEdit.setText(self.tableWidget.item(currentrow, 0).text())
        self.ui.lineEdit_2.setText(self.tableWidget.item(currentrow, 1).text())
        self.ui.lineEdit_3.setText(self.tableWidget.item(currentrow, 2).text())
        self.ui.buttonBox.accepted.connect(self.change_row)
        self.Dialog.show()

    def change_row(self):
        currentrow = self.tableWidget.currentRow()
        wish = self.tableWidget.item(currentrow, 0).text()
        description = self.tableWidget.item(currentrow, 1).text()
        url = self.tableWidget.item(currentrow, 2).text()

        new_wish = self.ui.lineEdit.text()
        new_desc = self.ui.lineEdit_2.text()
        new_url = self.ui.lineEdit_3.text()
        db.change_data(wish, description, url, new_wish, new_desc, new_url)
        self.widget_content()

    def open_link(self):
        currentrow = self.tableWidget.currentRow()
        url = self.tableWidget.item(currentrow, 2).text()
        if self.tableWidget.currentColumn() == 2:
            webbrowser.open(url)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    window.widget_content()
    app.exec_()


if __name__ == "__main__":
    main()
