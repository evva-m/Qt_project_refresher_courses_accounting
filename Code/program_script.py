import sys
from Functions_Main_Form import MainForm
from Functions_Teacher_Form import TeacherForm
from PyQt6.QtWidgets import QApplication, QScrollArea
from DataBaseConnection import glob_con


class TableViewScroll(QScrollArea):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 200, 1100, 790)
        self.wdg = MainForm()
        self.setWidget(self.wdg)
        self.wdg.backBtn.clicked.connect(self.run)
        self.wdg.tableWidget.cellDoubleClicked.connect(self.run)

    def run(self):  # скрывает себя и показывает вторую форму
        if self.sender() is self.wdg.tableWidget:
            if self.wdg.tableWidget.item(self.wdg.tableWidget.currentRow(), 0) is None or \
                    self.wdg.tableWidget.currentColumn() == 2:
                return
            else:  # если кликнута конкретная ячейка, задает аргументом show имя учителя
                teacherView.show(self.wdg.tableWidget.item(self.wdg.tableWidget.currentRow(), 0).text())
        else:
            teacherView.show()
        self.hide()
        self.wdg.errTchrLbl.setText('')
        self.wdg.errDelLbl.setText('')

    def closeEvent(self, a0):  # закрывает глобальное соединение с БД
        glob_con.close()
        a0.accept()


class TeacherViewScroll(QScrollArea):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 200, 780, 661)
        self.wdg = TeacherForm()

        self.setWidget(self.wdg)
        self.wdg.backBtn.clicked.connect(self.run)

    def show(self, name=None):  # показывает форму учителя либо дефолтную, либо информацию по заданному учителю
        if name is not None:
            self.wdg.tchrsBox.setCurrentIndex(self.wdg.names.index(name))
        else:
            self.wdg.tchrsBox.setCurrentIndex(0)
        self.wdg.load_table_courses()
        self.setVisible(True)

    def run(self):
        tableView.show()
        tableView.wdg.loadTable()
        self.wdg.errorLab.setText('')
        self.wdg.showPathEdit.setText('')
        self.wdg.coursesBox.setCurrentIndex(0)
        self.wdg.registEdit.clear()
        self.wdg.numEdit.clear()
        self.wdg.dateCourseEdit.clear()
        self.hide()

    def closeEvent(self, a0):
        glob_con.close()
        a0.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    teacherView = TeacherViewScroll()
    tableView = TableViewScroll()
    tableView.show()
    sys.exit(app.exec())
