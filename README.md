# Учет курсов повышения квалификации
**Задание проекта:** написать программу на основе фреймворка PyQt6,
предназначенную для учета часов курсовой подготовки педагогических
сотрудников. Программа удобна в случае, если в образовательной организации
предусмотрено минимальное количество часов курсовой подготовки, которые
должны быть пройдены педагогическим работником в каждый трехлетний
период его работы. 

### Программа должна реализовывать следующий функционал:
- добавление нового учителя в базу данных (БД);
- удаление учителя из БД;
- добавление нового курса в базу курсов;
- добавление новых сведений о курсах повышения квалификации (КПК)
учителя;
- изменение и удаление сведений о КПК учителя;
- просмотр в табличной форме информации по курсам повышения учителей
текущего трехлетнего периода;
- просмотр подробной информации по курсам всех периодов работы
выбранного учителя;
- возможность выгрузить сканы сертификатов по курсам в папку ScansDir,
которая создается в папке с программой;
- копирование базы данных в выбранную пользователем папку;
- формирование отчета по пройденным учителями КПК с использованием
реляционной базы данных, содержащий следующие поля: ФИО учителя,
персональный конец периода (ПКП), дата начала работы, количество часов за
текущий период, часы за прошлый и позапрошлый года, необходимые часы на
ближайшие 3 года, поля с информацией о пройденных учителями курсах
повышения квалификации за текущий период;
- возможность выбора столбцов для отображения в отчете;
- поиск по учителю;
- выгрузка отчета в формат .xlsx;
### Описание идеи:
программа представляет собой приложение на PyQt6. Использована
четырехтабличная база данных SQLite. Отображение отчета и курсов учителей
реализовано на основе виджета QTableWidget. Отображение форм таблицы
отчета и сведений о КПК учителя: QScrollArea и QWidget.
### Описание реализации:
Основные классы: класс таблицы с отчетом - TableViewScroll с виджетом
класса TableView, класс КПК учителей - TeacherViewScroll с виджетом класса
TeacherView. На первой форме можно посмотреть таблицу с отчетом о КПК
учителей, где также отображаются КПК, пройденные ими в их текущий
трехлетний период. Также есть функция выгрузки таблицы в формате xlsx. Можно
скрыть ненужные столбцы таблицы и сделать поиск по фамилии учителя. На этой
же форме есть функции добавления учителя, удаления учителя, резервного
копирования БД в выбранную папку и выгрузка сканов КПК. На форме
добавления учителя можно выбрать учителя, после этого в таблице будет
представлена информация обо всех пройденных ими КПК. Выбранному учителю
можно добавить сведения о его КПК, а также добавить новый курс в справочник
курсов. База данных содержит 4 таблицы: таблица courses: каждая запись – новый
пройденный учителем курс; таблица teachers – справочник учителей с датами их
поступления на работу для расчета их ПКП; таблица courses_dir – справочник
курсов с информацией о названии курса, объеме часов, организации и городе для
нормализации таблицы courses в случае прохождения учителями одинаковых
курсов повышения; таблица geo_city – справочник городов РФ, взят с сайта
Федеральные округа, регионы и города РФ база MySQL. Таблица courses_dir
обеспечивает хранение изображений сканов сертификатов в формате BLOB.

**Использованные технологии:** событийно управляемый интерфейс, базы
данных, работа с файлами, диалоговые окна.

**Необходимые для запуска библиотеки:** PyQt6, XlsxWriter
