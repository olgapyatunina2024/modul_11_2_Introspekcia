def introspection_info(obj):
    # Тип объекта
    obj_type = type(obj).__name__

    # Атрибуты объекта
    attributes = dir(obj)

    # Методы объекта
    methods = [method for method in attributes if callable(getattr(obj, method))]

    # Модуль объекта
    module = obj.__class__.__module__

    # Словарь объекта
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module},

    return info

# Интроспекция числа
number_info = introspection_info(42)
print(number_info)

# Интроспекция строки
string_info = introspection_info('Urban')
print(string_info)

# Интроспекция списка
list_info = introspection_info([1, -15, 7.23, 'qu-qu'])
print(list_info)