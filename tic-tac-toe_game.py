import math
list = []




def main():

    draw_empty(get_length())

    while True:
        row, column, sign = get_input()

        draw(row, column, sign)








def get_input():

    r = int(input("row: "))
    c = int(input("column: "))
    s = input("sign: ")

    return r, c ,s

def get_length():
    return int(input("length: "))



def draw_empty(length):
    global list

    for row in range(length):
        for column in range(length):

            if column == length - 1:
                print(" ")
                list.append({"row":row, "column":column,  "sign":" "})
            else:
                print(" |", end="")
                list.append({"row":row, "column":column, "sign":" "})




def draw(r, c, s):
    
    global list
    length = int(math.sqrt(len(list)))
    cell_iterator = 0

    for cell in list:
        if r == cell["row"] and c == cell["column"] and cell["sign"] == " ":
            cell["sign"] = s
            break
        else:
            continue
    
    for row in range(length):
        for column in range(length):

            if column == length - 1:
                print(f"{list[cell_iterator]["sign"]} ")
                cell_iterator += 1
            else:
                print(f"{list[cell_iterator]["sign"]} |", end="")
                cell_iterator += 1



main()






