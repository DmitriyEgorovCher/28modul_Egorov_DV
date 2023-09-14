� ������ ��������������: PageObject, Selenium � PyTest.

� �������� �������� ��������� requirements.txt ��� ��������� ����������� ��� ������������ ���������, 
settings.py � ��������� �������.

����� tests �������� ���� ��� ������� ����������: test
��� �� � ��� ��������� ����� chromedriver.exe ��� ������� ������ � ��������� google chrome.

����� pages �������� ��������� �����: base_page.py - ������� ��������, �� ������� ������������ ��� ��������� ������, 
Classes.py - �������� �����s ��� ������� ����������� � �����������, 
locators.py - ������ ��������� �� ��� ���������, 

��� ������� ������ ���������� ���������� ���������� ��������:
- pip install -r requirements.txt

������ ������ ��� ������ ������ � �������:

- python -m pytest -v --driver Chrome --driver-path chromedriver.exe Tests/test.py

���� ����� � ��� �������: https://docs.google.com/spreadsheets/d/1Vkgu_cpArLF7PAkpp0b10MjoIk4WsqzqgwctJEe5AW8/edit?usp=sharing

����������������� ����������: https://docs.google.com/document/d/1in5n9IS026cTxaJaYeMQFMl5rR776D2gt2OK49fUc78/edit?usp=sharing