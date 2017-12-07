# Ближайшие бары

Этот скрипт получает файл с данными в json формате от data.mos.ru, после находит самый большой и маленкие бары, а также ближайший бар от координат введенным пользовательем и выводит их в консоль.

# Как использовать

```python

import bars

json_content = load_data(r'd:\PythonScript\Devman\bars.json')
big_bars = get_biggest_bar(json_content)
smallest_bars = get_smallest_bar(json_content)
latitude = input('Введите координаты latitude: ')
longitude = input('Введите координаты longitude: ')
get_closest_bar(json_content, latitude, longitude) 

```

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py # possibly requires call of python3 executive instead of just python
# FIXME вывести пример ответа скрипта

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
