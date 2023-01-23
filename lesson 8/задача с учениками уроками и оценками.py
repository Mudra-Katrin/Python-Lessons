# Создать информационную систему позволяющую работать с учениками школы
# функции
# Добавление нового студента
# (Поля - имя, фамилия, название предмета, оценка)
# Добавление предмета
# Добавление оценки ученику по предмету
# Показ списка учеников
# Показ листа оценок конкретного ученика
# Выход из программы
  кому  Все
import model
import view
import os

def add_student():
    name = input("введите фамилию, имя (через пробел): ").strip()
    model.add_student(name)

def add_lesson():
    lesson = input("введите предмет: ").strip()
    model.add_lesson(lesson)

def show_student(data):
    view.show_student(data)
    s = input()


def start():
    while True:
        #os.system("cls")
        view.show_menu()
        while True:
            menu_input = int(input())
            if 0<menu_input<6:
                break
            else:
                print("неправильный ввод")
        match menu_input:
            case 1:
                add_student()
            case 2:
                add_lesson()
            case 3:
                data = model.get_data()
                show_student(data)
            case 5:
                exit()
import controller as contr

contr.start()
data = {}


def get_data():
    return data

def a_data(record): # запись данных
    data.append(record)
    
def add_student(name):
    data[name] = {}

def add_lesson(lesson):
    # print(lesson)
    # print(data)
    for key,value in data.items():
        value[lesson]=0
        # les = {lesson:0}
        # print(les)
    # for key in data.keys():
    #     data[key]=data[key][lesson]=0
    print(data)
def show_menu():
    print("выберите операцию:")
    print("1.Добавление нового студента")
    print("2.Добавление предмета")
    print("3.Показ списка учеников")
    print("4.Показ листа оценок конкретного ученика")
    print("5.Выход из программы")

def show_student(data):
    print(data.keys())