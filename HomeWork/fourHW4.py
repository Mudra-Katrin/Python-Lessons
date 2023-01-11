# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
def transform_polinom(user_polynom: str, user_file: str):
    polyn = user_polynom.replace('$', '')
    polyn = polyn.replace('**', '^')
    polyn = polyn.replace(' ', '')
    polyn = polyn[:-2]
    return polyn

my_file1='f_polinom4_5_1.md' # Файл c записью 1-го многочлена
my_file2='f_polinom4_5_2.md' # Файл c записью 2-го многочлена

def read_file(user_file):
    with open(user_file, 'r', encoding='utf-8') as pol:
        result = pol.read()
        return result
