# __init__.py
#
# Этот файл необходим для того, чтобы Python мог трактовать данную директорию как пакет.
# Наличие __init__.py позволяет использовать относительные импорты внутри пакета.
#
# В этот файл можно добавить код, который будет выполняться при импорте пакета, например:
# - Инициализацию пакета
# - Установку глобальных переменных
# - Настройку логирования
#
# Если данный файл пустой, то это нормально, так как его основная цель - указание Python,
# что данная директория является пакетом, и возможность использования относительных импортов.
#
# Пример использования:
#
# Структура:
# my_package/
#     __init__.py  # Пустой файл, либо с кодом инициализации
#     module1.py    # Модуль, содержащий функцию some_function
#     module2.py    # Модуль, который импортирует из module1.py
#
# В module2.py:
# from .module1 import some_function
