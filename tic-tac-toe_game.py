import math
list = []




def main():

    draw_empty(get_length())

    while True:
        row, column, sign = get_input()

        draw(row, column, sign)

        if check(row, column, sign):
            print("won")
        else:
            continue



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


def check(r, c, s):

    global list
    length = int(math.sqrt(len(list)))

    i = list.index({"row": r, "column": c, "sign": s})

    if i >= 0 and i <= length - 1:
        for r in range(length - 1):
            if(list[r]["sign"] == list[r+1]["sign"] == s):
                continue
            else:
                col = i
                for c in range(length - 1):
                    if(list[col]["sign"] == list[col+length]["sign"] == s):
                        col = col + length
                        continue
                    else:
                        return False
        return True

            
    elif i >= length and i <= (2*length - 1):
        for r in range(length, 2*length - 1):
            if(list[r]["sign"] == list[r+1]["sign"] == s):
                continue
            else:
                col = i - length
                for c in range(length - 1):
                    if(list[col]["sign"] == list[col+length]["sign"] == s):
                        col = col + length
                        continue
                    else:
                        return False
        return True

    elif i >= 2*length and i <= 3*length - 1:
        for r in range(2*length, 3*length - 1):
            if(list[r]["sign"] == list[r+1]["sign"] == s):
                continue
            else:
                col = i - 2*length
                for c in range(length - 1):
                    if(list[col]["sign"] == list[col+length]["sign"] == s):
                        col = col + length
                        continue
                    else:
                        return False
        return True






