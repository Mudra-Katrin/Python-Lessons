
def IsWensday():
    print("Введите день недели и проверим выходной ли он")
    day = int(input())
    return "Да" if 5 < day else "Нет"

print(IsWensday())
input("Press Enter to continue...")