from UI_Teacher_Form import UITeacherForm
from DataBaseConnection import glob_con, glob_cur
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QFileDialog, QMessageBox
from errors import FillFieldsError, CourseNameError, HoursQuantityError, TeacherSelectionError, NumberError
from PyQt6.QtGui import QColor


class TeacherForm(QWidget, UITeacherForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = []
        self.isDel = False
        self.new_course_fields = [self.nameEdit, self.hoursEdit, self.placeEdit]
        self.addCourseInfoBtn.setEnabled(False)

        self.names = sorted([i[0] for i in glob_cur.execute('SELECT name FROM teachers').fetchall()])
        self.names.insert(0, 'Не выбрано')
        self.tchrsBox.addItems(self.names)
        self.tchrsBox.currentIndexChanged.connect(self.load_table_courses)

        self.calendarWidget.hide()
        self.listView.hide()
        self.okDateBtn.hide()
        self.selectDateBtn.clicked.connect(self.selectDate)
        self.okDateBtn.clicked.connect(self.okDate)

        self.fname = ''
        self.ftype = ''
        self.loadImgBtn.clicked.connect(self.load_img)

        self.cityBox.addItems(sorted([i[0] for i in glob_cur.execute("""SELECT name FROM geo_city""").fetchall()]))

        self.courses_list = sorted(glob_cur.execute('''SELECT courses_dir.course_id, courses_dir.name, 
                        geo_city.name FROM courses_dir, geo_city WHERE courses_dir.city = geo_city.id''').fetchall(),
                                   key=lambda x: x[1])
        self.coursesBox.addItems([', '.join(course[1:]) for course in self.courses_list])
        self.coursesBox.currentIndexChanged.connect(self.show_course_info)
        self.show_course_info()

        self.coursesTchr.setColumnCount(6)
        self.coursesTchr.setHorizontalHeaderLabels(
            ['Название', "Объем", "Номер", "Дата выдачи", "Организация", "Город"])
        self.newCourse.stateChanged.connect(self.course_check)
        self.addCourseInfoBtn.clicked.connect(self.add_course_info)
        self.saveCourseBtn.clicked.connect(self.save_course)
        self.coursesTchr.cellDoubleClicked.connect(self.change_back)
        self.updatedbBtn.clicked.connect(self.update_db)
        self.coursesTchr.verticalHeader().sectionDoubleClicked.connect(self.delete)
        self.updatedbBtn_2.clicked.connect(self.update_DB_date_start)

    def show_course_info(self):
        to_show = glob_cur.execute(f"""SELECT name, hours, place, city FROM courses_dir 
        WHERE course_id = {self.courses_list[self.coursesBox.currentIndex()][0]}""").fetchone()
        for i, widget in enumerate(self.new_course_fields):
            widget.setText(str(to_show[i]))
        try:
            self.cityBox.setCurrentText(glob_cur.execute(f'''SELECT name FROM geo_city 
            WHERE id = "{to_show[-1]}"''').fetchone()[0])
        except Exception as err:
            print(err)

    def load_table_courses(self):
        if self.tchrsBox.currentIndex() == 0:
            self.selectDateBtn.setEnabled(False)
            self.coursesTchr.clearContents()
            self.coursesTchr.setRowCount(0)
            self.dateStartEdit.setEnabled(False)
            self.updatedbBtn_2.setEnabled(False)
            self.dateStartEdit.setText('')
            return
        self.updatedbBtn_2.setEnabled(True)
        self.dateStartEdit.setEnabled(True)
        self.selectDateBtn.setEnabled(True)
        self.dateStartEdit.setText(glob_cur.execute(f"""SELECT date_start FROM teachers 
        WHERE name = '{self.tchrsBox.currentText()}'""").fetchone()[0])
        self.calendarWidget.setMinimumDate(QDate.fromString(glob_cur.execute(f"""SELECT date_start FROM teachers 
        WHERE name = '{self.tchrsBox.currentText()}'""").fetchone()[0], 'yyyy-MM-dd'))
        self.calendarWidget.setMaximumDate(QDate.fromString(glob_cur.execute(f"""SELECT 
        CURRENT_DATE""").fetchone()[0], 'yyyy-MM-dd'))

        self.data = glob_cur.execute(f"""SELECT courses.id, courses_dir.name, courses_dir.hours, courses.number, 
        courses.earnDate, courses_dir.place, geo_city.name
        FROM courses, courses_dir, teachers, geo_city WHERE courses.course_id = courses_dir.course_id 
        AND teachers.teacher_id = courses.teacher_id AND teachers.name = '{self.tchrsBox.currentText()}' 
        AND geo_city.id = courses_dir.city""").fetchall()
        self.data.sort(key=lambda x: QDate.fromString(x[4], 'yyyy-MM-dd'), reverse=True)
        self.coursesTchr.setRowCount(0)
        for i, row in enumerate(self.data):
            self.coursesTchr.setRowCount(self.coursesTchr.rowCount() + 1)
            for j, elem in enumerate(row[1:]):
                self.coursesTchr.setItem(i, j, QTableWidgetItem(str(elem)))
        self.coursesTchr.resizeColumnsToContents()

    def course_check(self):  # активация и дезактивация режима добавления нового курса в справочник
        if self.newCourse.isChecked():
            self.course_clear()
            self.coursesBox.setEnabled(False)
            self.addCourseInfoBtn.setEnabled(True)
            self.saveCourseBtn.setEnabled(False)
            for widget in self.new_course_fields:
                widget.setEnabled(True)
            self.cityBox.setEnabled(True)
        else:
            self.show_course_info()
            self.coursesBox.setEnabled(True)
            self.addCourseInfoBtn.setEnabled(False)
            self.saveCourseBtn.setEnabled(True)
            for widget in self.new_course_fields:
                widget.setEnabled(False)
            self.cityBox.setEnabled(False)

    def add_course_info(self):  # добавление нового курса в справочник БД
        try:
            print(self.new_course_fields)
            courses_dir_val = [widget.text() for widget in self.new_course_fields]
            courses_dir_val.append(glob_cur.execute(f"""SELECT id FROM geo_city 
            WHERE name = '{self.cityBox.currentText()}'""").fetchone()[0])

            if '' in courses_dir_val:
                raise FillFieldsError
            if not ''.join(courses_dir_val[0].split()).isalpha():
                raise CourseNameError
            if not courses_dir_val[1].isdigit():
                raise HoursQuantityError
            flag = True
            if glob_cur.execute(f"""SELECT courses_dir.name FROM courses_dir, geo_city 
            WHERE courses_dir.name = '{self.nameEdit.text()}' 
            AND courses_dir.city = geo_city.id 
            AND geo_city.name = '{self.cityBox.currentText()}'""").fetchone() is not None:
                valid = QMessageBox.question(
                    self, '', f"Курс с таким названием и городом уже есть в базе. Точно добавить сведения?",
                    buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if valid == QMessageBox.StandardButton.No:
                    flag = False
            if flag:
                print(courses_dir_val)
                glob_cur.execute(f'''INSERT INTO courses_dir (name, hours, place, city) 
                                VALUES('{"', '".join(str(i) for i in courses_dir_val)}')''')
                glob_con.commit()
                self.courses_list = sorted(glob_cur.execute('''SELECT courses_dir.course_id, courses_dir.name, 
                geo_city.name FROM courses_dir, geo_city WHERE courses_dir.city = geo_city.id''').fetchall(),
                                           key=lambda x: x[1])
                self.coursesBox.clear()
                self.coursesBox.addItems([', '.join(course[1:]) for course in self.courses_list])
                print(self.courses_list)
                self.coursesBox.setCurrentIndex(self.courses_list.index((glob_cur.execute(
                    f'SELECT MAX(course_id) FROM courses_dir').fetchone()[0],
                                    courses_dir_val[0], glob_cur.execute(f"""SELECT name FROM geo_city 
                                                                WHERE id = {courses_dir_val[3]}""").fetchone()[0])))
                self.newCourse.setChecked(False)
        except FillFieldsError:
            self.errorLab.setText('Не все поля заполнены')
        except CourseNameError:
            self.errorLab.setText('Название курса должно быть только из букв и пробелов')
        except HoursQuantityError:
            self.errorLab.setText('Объем курса должен быть только из цифр')


    def save_course(self):  # добавление нового курса учителю
        try:
            if self.tchrsBox.currentIndex() == 0:
                raise TeacherSelectionError

            courses_val = [glob_cur.execute(f"""SELECT teacher_id FROM teachers 
            WHERE name = '{self.tchrsBox.currentText()}'""").fetchone()[0],
                           self.courses_list[self.coursesBox.currentIndex()][0], self.numEdit.text(),
                           self.dateCourseEdit.text()]

            if '' in courses_val or self.showPathEdit.text() == '':
                raise FillFieldsError
            if not self.numEdit.text().isdigit() or len(self.numEdit.text()) > 10:
                raise NumberError

            courses_val.append(self.registEdit.text())

            with open(self.fname, 'rb') as file:
                value = file.read()
            courses_val.append(value)
            courses_val.append(self.ftype)

            valid = QMessageBox.question(
                self, '', f"Действительно добавить курс учителю {self.tchrsBox.currentText()}?",
                buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if valid == QMessageBox.StandardButton.Yes:
                glob_cur.execute("""INSERT INTO courses (teacher_id, course_id, number, earnDate, registNumber, Scan, 
                scanType) VALUES (?, ?, ?, ?, ?, ?, ?)""", tuple(courses_val))
                glob_con.commit()
                QMessageBox.information(self, '', "Курс успешно добавлен", buttons=QMessageBox.StandardButton.Yes)

                self.errorLab.setText('')
                self.showPathEdit.setText('')
                self.coursesBox.setCurrentIndex(0)
                self.registEdit.clear()
                self.numEdit.clear()
                self.dateCourseEdit.clear()
                self.course_clear()
                self.show_course_info()
                self.load_table_courses()

        except TeacherSelectionError:
            self.errorLab.setText('Не выбран учитель')
        except FillFieldsError:
            self.errorLab.setText('Не все поля заполнены')
        except NumberError:
            self.errorLab.setText('Номер должен быть не длиннее 10 символов и содержать только цифры')
        except Exception as err:
            self.errorLab.setText(str(err))

    def course_clear(self):
        for widget in self.new_course_fields:
            widget.clear()
        self.cityBox.setCurrentIndex(0)

    def load_img(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать фото', '', "Images (*.png *.xpm *.jpg)")[0]
        if len(self.fname) > 0:
            self.ftype = self.fname[self.fname.index('.') + 1:]
            self.showPathEdit.setText(self.fname)

    def selectDate(self):
        self.calendarWidget.show()
        self.okDateBtn.show()
        self.listView.show()

    def okDate(self):
        self.dateCourseEdit.setText(self.calendarWidget.selectedDate().toString('yyyy-MM-dd'))
        self.okDateBtn.hide()
        self.listView.hide()
        self.calendarWidget.hide()

    def change_back(self):
        self.coursesTchr.item(self.coursesTchr.currentIndex().row(),
                              self.coursesTchr.currentIndex().column()).setBackground(QColor(100, 240, 240))

    def update_db(self):
        for row in range(self.coursesTchr.rowCount()):
            city = glob_cur.execute(f'''SELECT id FROM geo_city 
            WHERE name = "{self.coursesTchr.item(row, 5).text()}"''').fetchone()[0]
            course_id = glob_cur.execute(f"SELECT course_id FROM courses WHERE id = {self.data[row][0]}").fetchone()[0]
            glob_cur.execute(f"""UPDATE courses_dir SET name = '{self.coursesTchr.item(row, 0).text()}', 
            hours = {self.coursesTchr.item(row, 1).text()}, place = '{self.coursesTchr.item(row, 4).text()}', 
            city = {city} WHERE course_id = {course_id}""")
            glob_cur.execute(f"""UPDATE courses SET number = '{self.coursesTchr.item(row, 2).text()}', 
            earnDate = DATE('{self.coursesTchr.item(row, 3).text()}') WHERE id = {self.data[row][0]}""")
        glob_con.commit()
        self.load_table_courses()

    def delete(self):
        valid = QMessageBox.question(
            self, '', f'''Действительно удалить курс учителя {self.tchrsBox.currentText()} 
            "{self.coursesTchr.item(self.coursesTchr.verticalHeader().currentIndex().row(), 0).text()}"?''',
            buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if valid == QMessageBox.StandardButton.Yes:
            glob_cur.execute(f"""DELETE FROM courses
            WHERE id = {self.data[self.coursesTchr.verticalHeader().currentIndex().row()][0]}""")
            glob_con.commit()
            self.load_table_courses()

    def update_DB_date_start(self):
        glob_cur.execute(f"""UPDATE teachers SET date_start = DATE('{self.dateStartEdit.text()}') 
        WHERE name = '{self.tchrsBox.currentText()}'""")
        glob_con.commit()
