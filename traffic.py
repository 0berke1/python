import math

#global variables. User inputs.
global SPEED_LIMIT
global CAPACITY_A
global CAPACITY_B
global NUMBER_OF_PEOPLE
global NUMBER_OF_ROADS 

def main():

    print("welcome to traffic calculator. There are two types of cars : Model A and model B") # print welcome message.

    #get the capacitiy of the models 
    global CAPACITY_A 
    CAPACITY_A = int(input("enter capacity for model A cars:"))                             

    global CAPACITY_B
    CAPACITY_B = int(input("enter capacity for model B cars:")) 

    #speed limit                                                                                     
    global SPEED_LIMIT 
    SPEED_LIMIT = int(input("enter the speed limit:")) 

    #number of roads
    global NUMBER_OF_ROADS
    NUMBER_OF_ROADS = int(input("enter the number of roads:"))                                      

    print(f"both models go at the speed of {SPEED_LIMIT} when there're no more than 10 cars on a single road.")

    #number of people
    global NUMBER_OF_PEOPLE
    NUMBER_OF_PEOPLE = int(input("how many people will be on the road? "))

    numberofcarsA, numberofcarsB = numberofcars(NUMBER_OF_PEOPLE) #calculate how many cars are needed for each model to carry the given number of people.

    model = input("choose a model, A or B ").capitalize()  #user chooses a model. Speed gets updated for the chosen model and returned.

    if model == "A":
        speed = speedofcars(numberofcarsA)
        print(f"{numberofcarsA} model A cars are needed to carry {NUMBER_OF_PEOPLE} people.")


    elif model =="B":
        speed = speedofcars(numberofcarsB)
        print(f"{numberofcarsB} model B cars are needed to carry {NUMBER_OF_PEOPLE} people.")


    print(f"the cars has to go at the speed {speed}. They have to slow down {SPEED_LIMIT - speed}. ")  #new speed limit is shown to the screen.



#define the function that calculates how many cars of model A and model B are needed to transport a given number of people.
def numberofcars(number_of_people):

    number_of_cars_A= number_of_people / CAPACITY_A
    number_of_cars_B = number_of_people / CAPACITY_B

    return math.ceil(number_of_cars_A), math.ceil(number_of_cars_B)


#define the function that calculates the speed of which the cars on the road has to go given the number of cars
def speedofcars(number_of_cars):

    change_of_speed = 2 #this variable determines the change ratio of the max speed per car.

    if number_of_cars <= 10 * NUMBER_OF_ROADS:  # this checks if each road has at least 10 cars. If not, each car can go at the speed limit. 
        speed = SPEED_LIMIT
    elif number_of_cars > 10 * NUMBER_OF_ROADS: # if each road is filled with at least 10 cars, then they will start slowing down.
        speed = SPEED_LIMIT - change_of_speed * (number_of_cars - 10 * NUMBER_OF_ROADS)

    return speed

main()
