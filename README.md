# Support_Bot
This bot will contains some feauters that become helpful for tech support and users.
I hope that this bot will be handsome.

Steps to enroll:

1. Аутентификация пользователя - (ИНН/КПП организации)
2. Создание темы запроса.
3. Указание приоритетности запроса.
4. Контактная информация, номер AnyDesk

Steps to create following message in iTop:

1. Создание запроса в БД на основе введенных данных (присвоение организации, наименования запроса, контактной информации, заполнение описания)
2. Выставление соответствующих статусов запросу.
3. Добавление нового запроса в iTop.

База данных для бота (только тестовая версия)
БД может быть организована сл. образом:

Таблица "Компании":

1. ID (уникальный идентификатор компании, например, целое число или генерируемый автоматически идентификатор)
2. Наименование (название компании, текстовое поле)
3. ИНН (индивидуальный налоговый номер компании, текстовое поле)

Таблица "Сотрудники":

1. ID (уникальный идентификатор сотрудника)
2. Имя (имя сотрудника, текстовое поле)
3. Компания_ID (связь с таблицей "Компании", указывает на ID компании, к которой относится сотрудник)

Каждая компания имеет уникальный ID и может быть связана со своими сотрудниками через поле "Компания_ID" в таблице "Сотрудники"