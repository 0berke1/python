#define the max value of speed of cars model A and model B.
MAX_SPEED_A = 90
MAX_SPPED_B = 90

#define the capacitiy of the cars model A and model B
CAPACITY_A = 5
CAPACITY_B = 10


def main():

    print("welcome to traffic calculator. There are two types of cars : Model A and model B")
    print(f"model A cars have capacity of {CAPACITY_A}.")
    print(f"model B cars have capacity of {CAPACITY_B}.")
    print("both models go at the speed of 90 when there're no more than 10 cars on the road.")


    number_of_people = int(input("how many people will be on the road? "))

    numberofcarsA , numberofcarsB = numberofcars(number_of_people) #calculate how many cars are needed for each model to carry the given number of people.

    model = input("choose a model, A or B ")

    if model == "A":
        speed = speedofcars(numberofcarsA)

    elif model =="B":
        speed = speedofcars(numberofcarsB)


    print(f"the cars has to go at the speed {speed}. They have to slow down {MAX_SPEED_A - speed}. ")




    


#define the function that calculates how many cars of model A and model B are needed to transport a given number of people.
def numberofcars(number_of_people):
    #calculate the number of cars of model A and model B needed to transport a given number of people
    #return the number of cars of model A and model B needed to transport a given number of people
    number_of_cars_A = number_of_people // CAPACITY_A
    number_of_cars_B = number_of_people // CAPACITY_B
    return number_of_cars_A, number_of_cars_B

#define the function that calculates the speed of which the cars on the road has to go given the number of cars
def speedofcars(number_of_cars):

    if number_of_cars <= 10:
        speed = 90
    elif number_of_cars > 10:
        speed = 90 - 2 * number_of_cars


    return speed



main()
