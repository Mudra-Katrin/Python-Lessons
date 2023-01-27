
import random
maps=[1,2,3,
      4,5,6,
      7,8,9]
victories = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def check_victories():
    for i in victories:
        if maps[i[0]]==maps[i[1]]==maps[i[2]]:         
            return True        
        else:
            return False
 
def print_maps():
    print(maps[0],end="")
    print(maps[1],end="")
    print(maps[2])
    
    print(maps[3],end="")
    print(maps[4],end="")
    print(maps[5])
    
    print(maps[6],end="")
    print(maps[7],end="")
    print(maps[8])

print_maps()    
name1 = input("Введите имя первого игрока - ")    
name2 = input("Введите имя второго игрока - ")   

first_turn = random.choice([name1,name2])
print(first_turn)
game_over = False

cur_turn = first_turn

while not game_over:
    if cur_turn==first_turn:
        symbol = "X"
        step=int(input("введите номер клетки от 1 до 9 для вашего хода"))
        if maps[int(step)-1] == "X" or maps[int(step)-1]=="0":
            print ("Occupied!!! Try Again")
            continue
        maps[step-1] = symbol
    else:
        symbol="0"
        step = int(input("введите номер клетки от 1 до 9 для вашего хода"))
        if maps[int(step)-1]== "X" or maps[int(step)-1]=="0":
            print ("Occupied!!! Try Again")
            continue
        maps[step-1] = symbol
    print_maps()
    if check_victories():
        print(f"победил игрок {cur_turn}")
        game_over = True
    cur_turn = name2 if cur_turn==name1 else name1        
        

