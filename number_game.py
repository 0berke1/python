import random

list = [

    {"sayi_digit" : 0 , "sayi_alfabetik" : "sıfır"},
    {"sayi_digit" : 1 , "sayi_alfabetik" : "bir"},
    {"sayi_digit" : 2 , "sayi_alfabetik" : "iki"},
    {"sayi_digit" : 3 , "sayi_alfabetik" : "üç"},
    {"sayi_digit" : 4 , "sayi_alfabetik" : "dört"},
    {"sayi_digit" : 5 , "sayi_alfabetik" : "beş"},
    {"sayi_digit" : 6 , "sayi_alfabetik" : "altı"},
    {"sayi_digit" : 7 , "sayi_alfabetik" : "yedi"},
    {"sayi_digit" : 8 , "sayi_alfabetik" : "sekiz"},
    {"sayi_digit" : 9 , "sayi_alfabetik" : "dokuz"}

]

while True:
    baslat = input("rasgele bir sayı için B tuşuna bas.").capitalize()
    dy = False

    if baslat == "B":
        global sayi
        sayi = random.randint(0,9)
        
        while True:

            tahmin = input(f"şansına çıkan sayı: {sayi} , peki bu sayı nedir?")

            for i in range(len(list)):
                if sayi == list[i]["sayi_digit"]:
                    if tahmin == list[i]["sayi_alfabetik"]:
                        print(f"doğru! {sayi} = {tahmin}")
                        dy = True
                        break
                    else:
                        print(f"yanlış! tekrar dene. ")
                        dy = False
                        break

            if dy == True:
                break
            else:
                continue
                        
                               
    else:
        continue

