[![Build Status](https://app.travis-ci.com/berpress/ui_dress_tests.svg?branch=main)](https://app.travis-ci.com/berpress/ui_dress_tests)# Тесты для приложения ["Курсы"](https://qacoursemoodle.innopolis.university)

![Курсы](logo.jpg)
## Установка
***
1. Создайте отдельную директорию на локальном компьютере
2. Скачайте все файлы которые расположены в [директории](https://github.com/berpress/ui_dress_tests) <br>
   git clone https://github.com/berpress/ui_dress_tests
3. Откройте проект
4. Установите все пакеты, которые указаны в файле requirements.txt <br>
pip install -r /path/to/requirements.txt


## Описание проекта
***

### Тест проверки формы авторизации
Позитивная проверка:
* проверка на то что мы можем авторизоваться в системе с валидным логином и паролем<br>

Негативные проверки:
* пустой логин
* пустой пароль

__Запуск в файле__: tests/auth/test_auth.py

### Тест по обновлению персональных данных
Позитивные проверки:
* заполнение всех полей формы валидными данными

Негативные проверки обязательных полей:
* поочередное заполнение обязательных полей формы невалидными данными
__Запуск в файле__: \tests\personal_data\test_personal_data.py

### Тест проверки формы регистрации
Позитивные проверки:
* заполнение формы валидными данными и авторизация под новым пользователем 

Негативные проверки обязательных полей:
* поочередное заполнение обязательных полей формы невалидными данными и проверка невозможности авторизации под новым пользователем
__Запуск в файле__: tests/sign_up/test_sign_up.py

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


testing application: http://automationpractice.com/
