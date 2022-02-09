# Скрипты для взлома электронного дневника

Скрипт содержит 3 функции для взлома [электронного дневника](https://github.com/devmanorg/e-diary):

- fix_marks - для исправления плохих оценок
- remove_chastisements - для удаления замечаний
- create_commendation - для создания похвалы

### Использование

Для использования скриптов нужно запустить [интерактивную консоль](https://www.csestack.org/open-python-shell-django/) командой:

```
python manage.py shell
```

Чтобы использовать функции взлома нужно положить файл ```scripts.py``` рядом с manage.py и подключить через import.

Пример использования скрипта в интерактивной консоли:

```
(venv) ~ python manage.py shell
Python 3.8.10 (default, Nov 26 2021, 20:14:08) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from scripts import *
>>> create_commendation("Фролов Иван", "География")
>>> fix_marks("Фролов Иван")
>>> remove_chastisements("Фролов Иван")
```
