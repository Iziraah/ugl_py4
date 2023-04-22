# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление. .

something = 5
some_dict = {}
some_dict.update({k : v for k, v in locals().copy().items() if k[:2] != '__' and k != 'some_dict'})
print(some_dict)

def make_dict():
    for k in locals().copy().items():
        some_dict.update(k)
    print (some_dict)
make_dict()