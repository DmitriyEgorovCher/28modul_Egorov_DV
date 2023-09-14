# 28modul_Egorov_DV
В проект использовались: PageObject, Selenium и PyTest.

В корневом каталоге находятся requirements.txt для установки необходимых для тестирования библиотек, 
settings.py с тестовыми данными.

Папка tests содержит файл для запуска автотестов: test
так же в ней находятся файлы chromedriver.exe для запуска тестов с браузером google chrome.

Папка pages содержит следующие файлы: base_page.py - базовая страница, от которой унаследованы все остальные классы, 
Classes.py - содержит классs для страниц авторизации и регистрации, 
locators.py - список локаторов на веб страницах, 

Для запуска тестов необходимо установить библиотеки командой:
- pip install -r requirements.txt

Запуск тестов при помощи команд в консоли:

- python -m pytest -v --driver Chrome --driver-path chromedriver.exe Tests/test.py

Тест кейсы и баг репорты: https://docs.google.com/spreadsheets/d/1Vkgu_cpArLF7PAkpp0b10MjoIk4WsqzqgwctJEe5AW8/edit?usp=sharing

Отредактированные требования: https://docs.google.com/document/d/1in5n9IS026cTxaJaYeMQFMl5rR776D2gt2OK49fUc78/edit?usp=sharing
