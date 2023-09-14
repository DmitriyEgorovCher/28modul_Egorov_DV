¬ проект использовались: PageObject, Selenium и PyTest.

¬ корневом каталоге наход€тс€ requirements.txt дл€ установки необходимых дл€ тестировани€ библиотек, 
settings.py с тестовыми данными.

ѕапка tests содержит файл дл€ запуска автотестов: test
так же в ней наход€тс€ файлы chromedriver.exe дл€ запуска тестов с браузером google chrome.

ѕапка pages содержит следующие файлы: base_page.py - базова€ страница, от которой унаследованы все остальные классы, 
Classes.py - содержит классs дл€ страниц авторизации и регистрации, 
locators.py - список локаторов на веб страницах, 

ƒл€ запуска тестов необходимо установить библиотеки командой:
- pip install -r requirements.txt

«апуск тестов при помощи команд в консоли:

- python -m pytest -v --driver Chrome --driver-path chromedriver.exe Tests/test.py

“ест кейсы и баг репорты: https://docs.google.com/spreadsheets/d/1Vkgu_cpArLF7PAkpp0b10MjoIk4WsqzqgwctJEe5AW8/edit?usp=sharing

ќтредактированные требовани€: https://docs.google.com/document/d/1in5n9IS026cTxaJaYeMQFMl5rR776D2gt2OK49fUc78/edit?usp=sharing