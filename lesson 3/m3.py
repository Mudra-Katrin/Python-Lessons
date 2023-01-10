#Напишите программу, которая определит позицию второго вхождения строки в 
# списке либо сообщит, что её нет.
list_str =  ["asa", "gfgh", "a1sa"]
sub_str = "asa"
count = 0
for i in range(len(list_str)):
    if list_str[i]==sub_str:
        count+=1
        if count == 2:
            print(i)
            break
if count<2:
        print("нет")

