import math

#define the number of people that's gonna be on the road.
number_of_people = 0



def main():

    print("welcome to traffic calculator. There are two types of cars : Model A and model B")
    CAPACITY_A = int(input("enter capacity for model A cars:"))    
    CAPACITY_B = int(input("enter capacity for model B cars:"))
    MAX_SPEED = int(input("enter the speed limit:"))
    print(f"both models go at the speed of {MAX_SPEED} when there're no more than 10 cars on the road.")


    number_of_people = int(input("how many people will be on the road? "))

    numberofcarsA , numberofcarsB = numberofcars(number_of_people, CAPACITY_A, CAPACITY_B) #calculate how many cars are needed for each model to carry the given number of people.

    model = input("choose a model, A or B ").capitalize()

    if model == "A":
        speed = speedofcars(numberofcarsA, MAX_SPEED)
        print(f"{numberofcarsA} model A cars are needed to carry {number_of_people} people.")


    elif model =="B":
        speed = speedofcars(numberofcarsB, MAX_SPEED)
        print(f"{numberofcarsB} model B cars are needed to carry {number_of_people} people.")



    print(f"the cars has to go at the speed {speed}. They have to slow down {MAX_SPEED - speed}. ")
   



    


#define the function that calculates how many cars of model A and model B are needed to transport a given number of people.
def numberofcars(number_of_people , capacitiyA, capacityB):

    number_of_cars_A= number_of_people / capacitiyA
    number_of_cars_B = number_of_people / capacityB

    return math.ceil(number_of_cars_A), math.ceil(number_of_cars_B)

#define the function that calculates the speed of which the cars on the road has to go given the number of cars
def speedofcars(number_of_cars, max_speed):

    change_of_speed = 2 #this variable determines the change ratio of the max speed per car.

    if number_of_cars <= 10:
        speed_local = max_speed
    elif number_of_cars > 10:
        speed_local = max_speed - change_of_speed * (number_of_cars - 10)

    return speed_local



main()
