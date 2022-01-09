# 5***переменная тип***тип (взять): type(x)___идентификатор (проверить на связь с другими): id(x), a is b -> сравнить идентификаторы, a is None лучше, чем a == None___логическая проверка: isinstanse(x, int) -> True, False___две переменные ссылаются на один объект: list is new_list -> возвращает булево значение___число без знака: abs(-1)___список всех атрибутов объектов: dir()___посмотреть свойства и подсказки: help()___значение хэша для обьекта: hash(profit) -> лучше сравнивать по хешу неизменяемые объекты (быстрее)___логические: all() -> True если ВСЕ элементы списка/множества True, any() -> True если ХОТЯ БЫ ОДИН элемент списка True
# 6***ввод в консоли***два числа: x, y = map(int, input().split())___x, y, z = some_list___ввод списка парами: segments = [list(map(int, input().split())) for i in range(int(input()))]___ввод списка парами с сортировкой по второму элементу: work_list = sorted([sorted(map(int,input().split())) for i in range(int(input()))], name=lambda x: x[1])___ввод списка парами с сортировкой по первому элементу: segs = sorted([[int(i) for i in input().split()] for j in range(int(input()))])___ввод из двух строк 1 2 и 4 5 6: reader = (tuple(map(int, line.split())) for line in input) -> n_test, capacity = next(reader) [vals_n_weights] = reader или (n_test, capacity), vals_n_weights = reader___ввод массива чисел с пробелами: a = list(int(i) for i in input().split())___много пар чисел: A = [] for i in range(n_test): a, b = (int(i) for i in input().split()) A.append((a, b))
# 7***методы строк***длина строки: len()___поиск в строке (номер элемента): .find('a') и .rfind('a') -> с конца___замена в строке: .replase('a', 'b') -> создается новая строка___улучшалки строк: .lower() -> нижний регистр, .upper() -> верхний регистр, .strip() -> убрать пробелы___проверка строк: .isalpha() -> все буквы, isdigit() или isnumeric() -> все цифры
# 9***кортеж***неизменяемый список (const): my_tuple = (1, 2, 3), x = tuple()___добавить, изменить нельзя - можно сложить с таким-же: my_tuple + (5, 6)
# 10***множества***(как список, но хранит только уникальные объекты) создание: my_set = set([1, 2, 3]), my_set = {1, 2, 3}___действия: my_set | i_set -> объединение, my_set & i_set -> пересечение, my_set - i.set -> вычитание___методы множеств: .add -> добавление, .pop() discard() -> удаление, .update() -> обновление
# 11***операторы ветвления***сокращенная запись: if a: -> True !=0, False =0, if my_list: -> True - (список не пустой), False - (список пустой)___оператор pass: ничего не делать в этой строке, пропустить___проверка на отсутствие значения: val = none if val: print(str(val))
# 12***стиль языка***используется: i j k - для циклов, x y z - для координат, l I O - не называть так переменные___переменные, набранные в верхнем регистре - обычно константы - CONST (определяются глобально в начале)___если переменная цикла не важна используем подчеркивание: for _ in range(10):___в функции переменные обозначают: -_a, _d___переменные определяются не в начале, а перед использованием (лучше передать в функцию параметры и их использовать как локальные переменные)___делать много вычислений внутри print() - плохой стиль___произвольное число позиционных параметров - (*args), произвольное число именованных параметров - (**kwargs) kw - name word
# 13***полезные функции в цикле***вывод пар - номер в списке, значение: for i, animal in enumerate(zoo_pets): print(i, animal)
# 14***функции***параметры: позиционные, именованные или должны быть явно указаны - (x, y, *, z) ->  все после звездочки именованные___распаковка параметров: позиционных - res = module(*some_list) some_list = [1, 2, 3], именованных - ** (обычно словари), можно комбинировать все___самый лучший и устойчивый вызов - именованными параметрами___функция должна принимать от 3 до 7 параметров (больше - разбиваем), оптиум 2-5___по умолчанию: указываются при задании функции, применяются, если не изменили при вызове___значения по умолчанию вычисляются в точке определения функции, при компиляции___нельзя задавать изменяемый обьект в качестве параметра по умолчанию (список, словарь): def add_element_to_list(element, list_to_add=[]):___решение проблемы выше: def add_element_to_list(element, list_to_add=None): внутри кода -if list_to_add is None:list_to_add = []___произвольное число позиционных параметров: def print_them_all(*args): print(args) или for i, arg in enumerate(args): print('позиционный параметр:', i, arg)___произвольное число позиционных параметров можно использовать для заполнения базы данных___произвольное число именованных параметров: def print_them_all(**kwargs): print(kwargs) или for name, value in kwargs.items(): print('именованный аргумент:', name, '=', value)___комбинация произвольного числа позиционных и именованных параметров: def print_them_all_v3(*args, **kwargs): -> вызовы как на двух строках выше___при создании функции можно указывать как обычные параметры, так и произвольные параметры: def print_them_all_v4(a, b=5, *args, **kwargs) -> a и b не более пяти
# 15***быстрый вызов в pycharm***Ctrl +навести на функцию + кнопка мыши: вызвать определение функции
# Всегда используйте выражение def, а не присваивание лямбда-выражения к имени.
# s,t  = [input() for i in range(2)]

# Код, что бы чекать линки картинок со страницы. Ну вроде получилось. Так как есть вероятность получить картинки не только по абсолютному пути, но и по относительному - код пришлось чуть поправить
import requests
import re

site = 'https://stepik.org'
pattern = r'https[\S.]+(?:png|jpg|gif)'
string = requests.get(site).content
m_o = re.findall(pattern, string.decode('utf-8'))
print(m_o)

pattern = r'/[\S.]+(?:png|jpg|gif)'
m_o = re.findall(pattern, string.decode('utf-8'))
for i in range(len(m_o)):
    m_o[i] = site + m_o[i]
print(m_o)

s = r'\w*{}\w*'.format(input())
print(s)  # \w*функция\w*

# “Основы программирования на Python” – от факультета компьютерных наук высшей школы экономики:
# https://www.coursera.org/learn/python-osnovy-programmirovaniya
#
# “Специализация Программирование на Python” – 4 курса от mail.ru, мфти и “Фонда развития онлайн-образования”:
# https://www.coursera.org/specializations/programming-in-python
#
# Набор задачек по Python:
# https://stepik.org/course/431
#
# Курс по Python и Django от FreeCodeCamp.org:
# https://www.youtube.com/watch?v=F5mRW0jo-U4
#
# Свежий курс "Complete Programming Tutorial for Beginners":
# https://www.youtube.com/watch?v=_uQrJ0TkZlc

# Использование break - плохой тон, по возможности, следует обходиться без него
# Приведём пример использования continue (хотя при решении этой задачи можно и нужно обходиться без него)