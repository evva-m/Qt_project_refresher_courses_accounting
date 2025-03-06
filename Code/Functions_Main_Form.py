from UI_Main_Form import UIMainForm
from PyQt6.QtCore import QDate
import os
from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QFileDialog, QMessageBox
from errors import FillFieldsError
from PyQt6.QtGui import QColor
from xlsxwriter.workbook import Workbook
from DataBaseConnection import glob_con, glob_cur


class MainForm(QWidget, UIMainForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.startSrch.clicked.connect(self.Srch)
        self.filter = False
        self.endSrch.clicked.connect(self.Srch)

        self.newTchrBtn.clicked.connect(self.newTchr)
        self.exportBtn.clicked.connect(self.export)

        self.LoadNamesToDelete()
        self.deleteTchrBtn.clicked.connect(self.delete_tchr)

        self.calendarWidget.setMaximumDate(QDate.fromString(glob_cur.execute(f"""SELECT 
                        CURRENT_DATE""").fetchone()[0], 'yyyy-MM-dd'))
        self.calendarWidget.hide()
        self.listView.hide()
        self.okDateBtn.hide()
        self.selectDateBtn.clicked.connect(self.selectDate)
        self.okDateBtn.clicked.connect(self.okDate)

        self.checkList = [self.checkBox_0, self.checkBox_1, self.checkBox_9, self.checkBox_2, self.checkBox_10,
                          self.checkBox_11, self.checkBox_3, self.checkBox_4, self.checkBox_5, self.checkBox_6,
                          self.checkBox_7, self.checkBox_8]
        for check in self.checkList:
            check.setChecked(True)
            check.checkStateChanged.connect(self.loadTable)

        self.loadTable()
        self.loadScansBtn.clicked.connect(self.loadScan)
        self.DBcopyBtn.clicked.connect(self.copy)

        self.updDateBtn.clicked.connect(self.updateStartDates)

    def updateStartDates(self):
        for i in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(i, 2) is not None:
                glob_cur.execute(f"""UPDATE teachers SET date_start = DATE('{self.tableWidget.item(i, 2).text()}') 
                WHERE name = '{self.tableWidget.item(i, 0).text()}'""")
        glob_con.commit()

    def loadTable(self):
        if self.filter:
            names = glob_cur.execute(f'''SELECT name, date_start, teacher_id FROM teachers 
            WHERE name LIKE "{self.searchEdit.text()}%"''').fetchall()
            if names is None:
                return
        else:
            names = glob_cur.execute(f'SELECT name, date_start, teacher_id FROM teachers').fetchall()

        courses = glob_cur.execute('''SELECT courses.teacher_id, courses.earnDate, courses_dir.hours,
           courses_dir.name FROM courses, courses_dir WHERE courses.course_id = courses_dir.course_id 
           GROUP BY courses.id''').fetchall()

        data = {name[:2]: [i[1:] for i in courses if i[0] == name[2]] for name in names}

        tableDict = dict()
        for name, courses in data.items():
            date = name[1]
            while glob_cur.execute(f'SELECT "{date}" < CURRENT_DATE').fetchone()[0]:
                prev = date
                date = glob_cur.execute(f'SELECT DATE("{date}", "+3 years")').fetchone()[0]

            corrCourses = [i for i in courses if glob_cur.execute(f'''SELECT 
            DATE("{i[0]}") >= "{prev}" AND DATE("{i[0]}") < "{date}"''').fetchone()[0] == 1]
            hours = sum(int(i[1]) for i in corrCourses)

            prev_year1 = sum([int(i[1]) for i in courses if glob_cur.execute(f'''SELECT 
            DATE("{i[0]}") >= DATE(CURRENT_DATE, "-1 year")''').fetchone()[0] == 1])
            prev_year2 = sum([int(i[1]) for i in courses if glob_cur.execute(f'''SELECT DATE("{i[0]}") < 
            DATE(CURRENT_DATE, "-1 years") AND DATE("{i[0]}") > DATE(CURRENT_DATE, "-2 years")''').fetchone()[0] == 1])

            hours_year1 = (108 - hours + abs(108 - hours)) // 2
            x = hours_year1
            hours_year3 = 0
            hours_year2 = 0
            if glob_cur.execute(f'SELECT DATE("{date}", "-1 year") > CURRENT_DATE').fetchone()[0]:
                if glob_cur.execute(f'SELECT DATE("{date}", "-2 year") > CURRENT_DATE').fetchone()[0]:
                    # k = доля дней в 3-й год до конца ПКП от всех оставшихся дней
                    k = glob_cur.execute(f"""SELECT 1 / ROUND(((365 * 2) + JULIANDAY('{date}') - 
                    JULIANDAY(DATE(CURRENT_DATE, '+2 years'))) / ABS(JULIANDAY('{date}') - 
                    JULIANDAY(DATE(CURRENT_DATE, '+2 years'))), 1)""").fetchone()[0]
                    nextk = glob_cur.execute(f"""SELECT 1 / ROUND((365 * 3) / (JULIANDAY(DATE(CURRENT_DATE, '+3 years')) 
                    - JULIANDAY('{date}')), 1)""").fetchone()[0]
                    hours_year3 += int(hours_year1 * k + 108 * nextk)
                    hours_year2 = int(hours_year1 * ((1 - k) / 2))
                    hours_year1 = int(hours_year1 * ((1 - k) / 2))
                else:
                    k = glob_cur.execute(f"""SELECT 1 / ROUND((365 + JULIANDAY('{date}') - 
                                        JULIANDAY(DATE(CURRENT_DATE, '+1 years'))) / ABS(JULIANDAY('{date}') - 
                                        JULIANDAY(DATE(CURRENT_DATE, '+1 years'))), 1)""").fetchone()[0]
                    nextk = glob_cur.execute(f"""SELECT 1 / ROUND((365 * 3) / (JULIANDAY(DATE(CURRENT_DATE, '+2 years')) 
                                        - JULIANDAY('{date}')), 1)""").fetchone()[0]
                    hours_year3 += 108 // 3
                    val_yr2 = int(hours_year1 * k) + int(((hours_year1 * k) - int(hours_year1 * k)) * 2)
                    hours_year2 = val_yr2 + int(108 * nextk) + int(((108 * nextk) - int(108 * nextk)) * 2)
                    val_yr1 = int(hours_year1 * (1 - k)) + int(((hours_year1 * (1 - k)) -
                                                                int(hours_year1 * (1 - k))) * 2)
                    hours_year1 = val_yr1 + (x - val_yr2 - val_yr1)
            else:
                nextk = glob_cur.execute(f"""SELECT 1 / ROUND((365 * 3) / (JULIANDAY(DATE(CURRENT_DATE, '+1 years')) 
                                                        - JULIANDAY('{date}')), 1)""").fetchone()[0]
                hours_year3 += 108 // 3
                hours_year2 = 108 // 3
                hours_year1 += int(108 * nextk) + int(((108 * nextk) - int(108 * nextk)) * 2)

            corrCourses = [i[::-1] for i in sorted(corrCourses, key=lambda x: QDate.fromString(x[0], 'yyyy-MM-dd'))]
            if len(corrCourses) == 0:
                corrCourses.append(['Курсы не пройдены', '', ''])
            tableDict[(name[0], date, name[1], hours, prev_year1, prev_year2, hours_year1,
                       hours_year2, hours_year3)] = corrCourses

        self.tableWidget.setColumnCount(12)
        self.tableWidget.setRowCount(0)

        SpanList = []
        courses_sum = 0
        for val in sorted(tableDict):
            SpanList.append([courses_sum, len(tableDict[val])])
            courses_sum += len(tableDict[val])

        self.tableWidget.setHorizontalHeaderLabels(['ФИО', "Персональный\nконец периода",
                                                    "Дата начала работы",
                                                    "Количество часов\nна текущий момент",
                                                    "Часы за\nпрошлый год", "Часы за\nпозапрошлый год",
                                                    "1 год", "2 год", "3 год",
                                                    "Название курса", "Объем", "Дата"])
        courses_show = False
        for i in range(9, 11):
            if self.checkList[i].isChecked():
                courses_show = True
                break
        for key, val in sorted(tableDict.items()):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for i, elem in enumerate(key):
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, i, QTableWidgetItem(str(elem)))
            if courses_show:
                for j, piece in enumerate(val[0]):
                    self.tableWidget.setItem(self.tableWidget.rowCount() - 1, j + 9, QTableWidgetItem(str(piece)))
                for i, elem in enumerate(val[1:]):
                    self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                    for j, piece in enumerate(elem):
                        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, j + 9, QTableWidgetItem(str(piece)))

        self.tableWidget.resizeColumnsToContents()
        if courses_show:
            for span in SpanList:
                for i in range(9):
                    self.tableWidget.setSpan(span[0], i, span[1], 1)

        num = 0
        for row in range(self.tableWidget.rowCount()):
            if not self.tableWidget.item(row, 1) is None:
                if glob_cur.execute(f"""SELECT CURRENT_DATE < DATE('{self.tableWidget.item(row, 1).text()}', 
                '-2 years')""").fetchone()[0] == 1:
                    self.tableWidget.item(row, 6).setBackground(QColor(255, 200, 200))
                    self.tableWidget.item(row, 7).setBackground(QColor(255, 200, 200))
                    self.tableWidget.item(row, 8).setBackground(QColor(255, 240, 150))
                    continue
                elif glob_cur.execute(f"""SELECT CURRENT_DATE < DATE('{self.tableWidget.item(row, 1).text()}', 
                '-1 years')""").fetchone()[0] == 1:
                    self.tableWidget.item(row, 6).setBackground(QColor(255, 200, 200))
                    self.tableWidget.item(row, 7).setBackground(QColor(255, 240, 150))
                    self.tableWidget.item(row, 8).setBackground(QColor(200, 255, 230))
                    continue
                else:
                    self.tableWidget.item(row, 6).setBackground(QColor(255, 240, 150))
                    self.tableWidget.item(row, 7).setBackground(QColor(200, 255, 230))
                    self.tableWidget.item(row, 8).setBackground(QColor(200, 255, 230))
        for col_index in range(12):
            if not self.checkList[col_index].isChecked():
                self.tableWidget.removeColumn(col_index - num)
                num += 1

    def Srch(self):  # фильтрует таблицу по строке поиска и отменяет фильтр
        if self.sender() is self.startSrch:
            self.filter = True
            self.loadTable()
        else:
            self.filter = False
            self.loadTable()

    def newTchr(self):  # добавление нового учителя в БД
        try:

            values = [self.nameTchrEdit_1.text(), self.nameTchrEdit_2.text(), self.nameTchrEdit_3.text(),
                      self.dateTchrEdit.text()]
            if '' in values:
                raise FillFieldsError
            glob_cur.execute(f"""INSERT INTO teachers (name, date_start) 
            VALUES ('{" ".join(values[:3])}', DATE('{values[3]}'))""")
            glob_con.commit()
            self.errTchrLbl.setText('')
            self.loadTable()
            self.nameTchrEdit_1.setText('')
            self.nameTchrEdit_2.setText('')
            self.nameTchrEdit_3.setText('')
            self.dateTchrEdit.setText('')
            self.LoadNamesToDelete()
        except FillFieldsError:
            self.errTchrLbl.setText("Не все поля заполнены")

    def delete_tchr(self):  # удаление учителя из бд
        if self.tchrsBox.currentIndex() == 0:
            self.errDelLbl.setText('Учитель не выбран')
            return
        self.errDelLbl.setText('')
        id = \
        glob_cur.execute(f"SELECT teacher_id FROM teachers WHERE name = '{self.tchrsBox.currentText()}'").fetchone()[0]
        glob_cur.execute(f"""DELETE FROM teachers WHERE teacher_id = {id}""")
        glob_cur.execute(f"""DELETE FROM courses WHERE teacher_id = {id}""")
        glob_con.commit()
        self.loadTable()
        self.LoadNamesToDelete()

    def LoadNamesToDelete(self):  # обновляет список учителей для удаления
        self.tchrsBox.clear()
        names = sorted([i[0] for i in glob_cur.execute('SELECT name FROM teachers').fetchall()])
        names.insert(0, 'Не выбрано')
        self.tchrsBox.addItems(names)

    def export(self):  # выгружает таблицу по выбранному пути
        fileName, ok = QFileDialog.getSaveFileName(
            self,
            "Сохранить файл",
            ".",
            "Excel (*.xlsx)"
        )
        if not fileName:
            return
        workbook = Workbook(fileName)
        worksheet = workbook.add_worksheet()
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                if row == 0:
                    worksheet.write(row, col, self.tableWidget.horizontalHeaderItem(col).text())
                if self.tableWidget.item(row, col) is None:
                    self.tableWidget.setItem(row, col, QTableWidgetItem(''))
                worksheet.write(row + 1, col, self.tableWidget.item(row, col).text())
        workbook.close()

    def loadScan(self):  # создает папку со сканами сертификатов в репозитории программы
        scans = glob_cur.execute('''SELECT teachers.name, courses.earnDate, courses.Scan, courses.scanType FROM courses, 
        teachers WHERE teachers.teacher_id = courses.teacher_id AND Scan IS NOT NULL''').fetchall()
        scans.sort(key=lambda x: x[0])
        os.makedirs('./ScansDir', exist_ok=True)
        for i, scan in enumerate(scans):
            with open(f'./ScansDir/{scan[0]} {scan[1]} {i}.{scan[3]}',
                      'wb') as out:  # брать не jpg, а расширение из базы, которое должно загружаться при загрузке файла
                out.write(scan[2])
        QMessageBox.information(self, '', """Сканы загружены в папку ScansDir, которая 
        создалась в папке с этой программой""", buttons=QMessageBox.StandardButton.Yes)

    def copy(self):  # копирует бд в выбранный каталог
        dir_path = QFileDialog.getExistingDirectory(self, 'Выберите папку', '')
        with open('Courses_db.sqlite', 'rb') as database:
            copydb = database.read()
        with open(dir_path + '/БД КПК копия.sqlite', 'wb') as out:
            out.write(copydb)
        QMessageBox.information(self, '', f"База данных скопирована в папку {dir_path}",
                                buttons=QMessageBox.StandardButton.Yes)

    def selectDate(self):
        self.calendarWidget.show()
        self.okDateBtn.show()
        self.listView.show()

    def okDate(self):
        self.dateTchrEdit.setText(self.calendarWidget.selectedDate().toString('yyyy-MM-dd'))
        self.okDateBtn.hide()
        self.listView.hide()
        self.calendarWidget.hide()
