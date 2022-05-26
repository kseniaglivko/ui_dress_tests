[![Build Status](http://kseniaglivko.teamcity.com/app/rest/builds/buildType:(id:UiDressTests_Build)/statusIcon)](https://kseniaglivko.teamcity.com/viewType.html?buildTypeId=UiDressTests_Build&guest=1)

# Тесты для приложения ["Курсы"](https://qacoursemoodle.innopolis.university)

![Курсы](logo.png)

## Установка
***
1. ```git clone https://github.com/berpress/ui_dress_tests```
2. Открыть проект в IDE
3. Активировать виртуальное окружение (*внимание: имеются переменные окружения!*)
4. ```pip install -r requirements.txt```
5. ```pre-commit install```


## Описание проекта
***
Целью написания данного набора тестов является проверка корректной работы основного функционала приложения. <br> В данный тестовый набор вошли следующие проверки:
### Тест проверки формы авторизации
Позитивная проверка:
* проверка на то что мы можем авторизоваться в системе с валидным логином и паролем<br>

Негативные проверки:
* пустой логин
* пустой пароль

__тест-кейсы__: [на форму авторизации](https://docs.google.com/spreadsheets/d/1OQ8zjJmgeb0Bb6UenDapVIFmVbjRmoW0eBtqThQK5xA/edit#gid=0)

__Запуск в файле__: tests/auth/test_auth.py

### Тест по обновлению персональных данных
Позитивные проверки:
* заполнение всех полей формы валидными данными

Негативные проверки обязательных полей:
* поочередное заполнение обязательных полей формы невалидными данными

__тест-кейсы__: [на форму заполнения персональных данных](https://docs.google.com/spreadsheets/d/1OQ8zjJmgeb0Bb6UenDapVIFmVbjRmoW0eBtqThQK5xA/edit#gid=1621977626)

__Запуск в файле__: \tests\personal_data\test_personal_data.py

### Тест проверки формы регистрации
Позитивные проверки:
* заполнение формы валидными данными и авторизация под новым пользователем

Негативные проверки обязательных полей:
* поочередное заполнение обязательных полей формы невалидными данными и проверка невозможности авторизации под новым пользователем

__тест-кейсы__: [на форму регистрации](https://docs.google.com/spreadsheets/d/1OQ8zjJmgeb0Bb6UenDapVIFmVbjRmoW0eBtqThQK5xA/edit#gid=1310841361)

__Запуск в файле__: tests/sign_up/test_sign_up.py

### Тест проверки возможности создания и удаления курса
Позитивные проверки:
* заполнение формы валидными данными создание и удаление созданного курса

__тест-кейсы__: [на форму создания курса](https://docs.google.com/spreadsheets/d/1OQ8zjJmgeb0Bb6UenDapVIFmVbjRmoW0eBtqThQK5xA/edit#gid=1937322818)

__Запуск в файле__: tests/create_course/test_course_creation.py

## Создание отчетов при помощи Allure
***
Чтобы сгенерировать Allure отчет после прогона тестов необходимо выполнить два шага:
1. Скачать (установить) _**Allure commandline application**_  на свою операционную систему.

   **Для пользователей Windows** лучше выбрать один из 2-х нижеперечисленных вариантов:
   1) Установить _**Allure commandline application**_ через _**PowerShell**_ командой:
   <br>```scoop install allure```<br>
      смотри [видеоинструкцию](https://www.youtube.com/watch?v=3WuTSDkfuqQ) (таймкод с 0:38 по 1:10)
   2) Если у вас не установлен scoop, то тогда следует скачать _**Allure commandline application**_ вручную:<br>
      смотри [видеоинструкцию](https://www.youtube.com/watch?v=3WuTSDkfuqQ) (таймкод с 1:39 по 3:07)
   3) Также вне зависимости от способа установки _**Allure commandline application**_ на Windows,
   <br>для работы с **Allure** необходимо будет
   установить Java - [видеоинструкция](https://www.youtube.com/watch?v=6qASwPL86MM&t=1352s) (таймкод с 7:00 по 8:35)

   **Для пользователей Linux и MacOS** смотрите как установить
_**Allure commandline application**_ [тут](https://docs.qameta.io/allure/#_installing_a_commandline).

2. Создать данные о выполнении тестов, на основании которых будут сгенерированы отчеты.
<br>Для этого нужно запускать тесты следующей командой в терминале:<br>```pytest --alluredir=allure_reports```


После прогона тестов останется только сгенерировать отчет командой в терминале:
<br>```allure serve allure_reports```<br>(отчет будет представлен на страничке браузера)
