requirements.txt - зависимости команды запись и загрузка по списку;
pip freeze > requirements.txt  -генерирует файл  requirements.txt , записывая в файл все зависимости с их версиями
pip install -r requirements.txt - устанавливает все зависимости с файла.

Ввести данные в файл settings


 Тесты запускать в терминале с \tests
 с теста регистрации (без проблем)
 pytest test_registr.py > myoutput_registr.log

 авторизации  (с капчей)
 pytest test_auth.py > myoutput_auth.log

 восстонавление (с капчей и кодом смс)
 pytest test_pass_rec.py > myoutput_pass_rec.log

 либо по маркеру  pytest -m norm > myoutput_norm.log
 без кодов, но 3 тестах ввести капчу(5авто,4пасс,31регистр)