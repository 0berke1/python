import math

list = []
cars_quantitiy_list = []

#global variables. User inputs.
global SPEED_LIMIT
global NUMBER_OF_ROADS
global NUMBER_OF_PEOPLE

def main():
    while True:
        try:
            #speed limit
            global SPEED_LIMIT                                                                        
            SPEED_LIMIT = int(input("enter the speed limit:")) 

            #number of roads
            global NUMBER_OF_ROADS
            NUMBER_OF_ROADS = int(input("enter the number of roads:"))

            print(f"models go at the speed of {SPEED_LIMIT} when there're no more than 10 cars on a single road.")

            #number of people
            global NUMBER_OF_PEOPLE
            NUMBER_OF_PEOPLE = int(input("how many people will be on the road? "))

            while True:
                try:

                    model_name = input("enter model name: ")
                    model_capacity = int(input(f"enter model capacity for {model_name}: "))

                    if not {"name":model_name, "capacity":model_capacity} in list:
                        list.append({"name" : model_name , "capacity" : model_capacity})
                    else:
                        print("model already exists.")
                        continue

                except EOFError:
                    break

            while True:
                try:

                    key_input = input("press L to list the models. Press C to calculate speed.").capitalize()


                    if key_input == "L":
                        print("model" , "  capacity ")

                        for i in range(len(list)):
                            print(list[i]["name"] , " " , list[i]["capacity"])

                    elif key_input == "C":
                        cars_quantitiy_list = numberofcars()

                        print(f"number of cars needed to carry {NUMBER_OF_PEOPLE} people for each model:")
                        for i in range(len(list)):
                            print(list[i]["name"] , " " , cars_quantitiy_list[i])

                        model_input = input("choose a model to calculate speed: ")

                        for i in range(len(list)):
                            if list[i]["name"] == model_input:
                                speed = speedofcars(cars_quantitiy_list[i])
                                break
                        
                        print(f"the cars has to go at the speed {speed}. They have to slow down {SPEED_LIMIT - speed}. ")  #new speed limit is shown to the screen.

                except EOFError:
                    break

        except EOFError:
            break
        





def numberofcars():

    local_list = []

    for i in range(len(list)):
        local_list.append(math.ceil(NUMBER_OF_PEOPLE / int(list[i]["capacity"])))

    return local_list

 

def speedofcars(number_of_cars):

    change_of_speed = 2 #this variable determines the change ratio of the max speed per car.

    if number_of_cars <= 10 * NUMBER_OF_ROADS:  # this checks if each road has at least 10 cars. If not, each car can go at the speed limit. 
        speed = SPEED_LIMIT
    elif number_of_cars > 10 * NUMBER_OF_ROADS: # if each road is filled with at least 10 cars, then they will start slowing down.
        speed = SPEED_LIMIT - change_of_speed * (number_of_cars - 10 * NUMBER_OF_ROADS)

    return speed







main()
