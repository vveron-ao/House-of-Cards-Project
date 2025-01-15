# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Nune Papoyan
#               Veronica O'Neill
#               Daniel Meza
#               Sundeep Chidambaram
# Section:      559
# Assignment:   LAB: Final Project
# Date:         December 07, 2024


# importing necessary libraries
import matplotlib.pyplot as plt
from turtle import Turtle as T, done, Screen


# global variable used to calculate the penny stacks in kilograms.
avg_penny_weight = 0.0015551738


def reading_file():
    '''This function will read the CSV file and analyze the data to compare it to Team 18's results.'''

    # initializing empty lists to append file data
    whole_data = []
    tot_prof = []
    proj_acc = []
    height_data = []
    weight_data = []

    # Collecting data
    with open("HouseofCardsResults.csv", 'r') as file:
        file.readline() # skiping first line
        file.readline() # skiping second line
        whole_data = file.readlines()  # Read all lines after the 2nd line

    # Process all rows and split into different lists
    for line in whole_data:
        data = line.strip().split(",")
        # data content [<team number>, <Total Profit>, <Profit Accuracy>, <Height>, <# Pennies>]
        
        # Distributing all datas from each row into thier respective category 
        tot_prof.append(data[1])
        proj_acc.append(data[2])
        height_data.append(data[3])
        weight_data.append(data[4])


    # Conversions
    for i in range(len(height_data)):

        try:
            # Converting Total Profit into a number
            tot_prof[i] = float(tot_prof[i])
            # Converting Profit Accuracy in to a number
            proj_acc[i] = float(proj_acc[i].strip('%'))

            # Extract height data & convert to cm
            height_data[i] = float(height_data[i]) * 2.54
            # Extract weight data and convert to kg
            weight_data[i] = float(weight_data[i]) * avg_penny_weight

        except (IndexError, ValueError):
            print(f"Skipping invalid row")

    return tot_prof, proj_acc, height_data, weight_data


def graphs():
    '''
    This function plots 2 graphs. The graphs being ploted are: A Height vs. Weight Graph and a \n
    Profit vs. % Error graph. Both being compared to the other teams'.
    '''
    # Data collection
    tot_prof, proj_acc, height_data, weight_data = reading_file()

    ###### Height vs. Weight graph ######
    # Compare our performance with other team using graph (Height (y) vs Weight (x))

    # Creating figure
    plt.figure("Graph A")
    plt.title('Height vs. Weight - Team Results in Comparison with Other Teams')  # Fixed typo in title

    # Grahping
    plt.scatter(weight_data, height_data, color='magenta', label='Previous Teams') 
    plt.scatter(converted_weight, converted_height, color='blue', label='Our Team Results')

    # Labels
    plt.xlabel("Weight (kg)")
    plt.ylabel("Height (cm)")
    plt.legend()
   


    ###### Total Profit vs. Profit Percent Error ######
    # Compare our performance with other team using graph (profit (y) vs profit percent error (x)

    # Creating figure
    plt.figure("Graph B", figsize=(8,5))
    plt.title("Total Profit vs. Profit Percent Error - Team Results in Comparison with Other Teams")

    # Graphing
    plt.scatter(proj_acc, tot_prof, color = 'magenta', label='Previous Teams')
    plt.scatter(teamAcc, teamProfit, color='blue', label='Our Team Results')


    # Labels
    plt.xlabel("Profit Percent Error (%)")
    plt.ylabel("Total Profit ($)")
    plt.legend()

    
    # Show the figures
    plt.show()

def cal_profit(values):
    numCards, tape, scissors, time, height, strength, structure = values
    '''
    This functions calculates a teams profit.\n
    Parameters:\n
    numCards (int) : the number of cards used to build the structure\n
    tape (int) : the number of rolls of tape used\n
    scissors (int) : number of scissors used\n
    time (time) : time it took to build structure in minutes\n
    height (int) : the structure's height in inches\n
    strength (int) : number of additional pennies stacks with held\n
    structure (bool) : True if the structure was successfully built\n
    Returns the calculated profit
    '''
    profit = 0
    if structure: profit += 100000

    profit -= 1000*numCards + tape*10000 + scissors*5000
    profit += (height-36)*2000 + (strength-1)*500

    if time <25:
        profit+=(25-time)*1000
    elif time > 25:
        profit -= (time-25)*2000
    return profit

def cal_accuracy(predictedProfits, actualProfits):
    '''Calculates and returns the project accuracy'''
    return int((1 - (abs(predictedProfits-actualProfits)/actualProfits))*100)

def userData():
    '''
    Gets the user inputs for number of cards used, number of tape, number of scissors,\n
    amount of time it took to build, height of structure in inches and number, number of penny stack it stood\n
    and most importantly if the build was succesfull.\n
    Then returns all those values in the order of:\n
    numCards, tape, scissors, time, height, strength, structure
    '''
    num_cards = int(input("number of cards used: "))
    num_tape = int(input("number of tape rolls used: "))
    num_scissors = int(input("number of scissors: "))
    num_time = int(input("how much time (minutes): "))
    num_height = int(input("how tall was your tower in inches: "))
    num_penny = int(input("number of penny stacks held: "))
    num_W_L = input("Was tower succesful?(Y or N) ")=='Y'
    return num_cards, num_tape, num_scissors, num_time, num_height, num_penny, num_W_L

# Creating Break
print()
user_data = userData()
totProfit = cal_profit(user_data)

# Output of user's estimated profit
print(f"\nYour estimated profit is ${totProfit}\n")

# Team Data and calculations
team_data = (88, 1, 0, 25, 68, 1, True)
teamProfit  = cal_profit(team_data)
teamAcc = cal_accuracy(teamProfit, 66000)
converted_height = team_data[4] * 2.54
converted_weight = team_data[5] * (10*avg_penny_weight)

reading_file()
graphs()

with open("Team_Results.txt", 'w') as team_results_file:
    team_results_list = [str(18), str(teamProfit), str(teamAcc)+"%", str(team_data[4]), str(team_data[5]*10)]
    # Append team results to the file
    team_results_file.write(','.join(map(str, team_results_list)))

with open("HouseofCardsResults.csv", 'a') as csvFile:
    csvFile.write(",".join(team_results_list))

def turtle_drawing():
    '''This functions uses Turtle to draw the Team 18's tower design.'''
    build = T( )
    build.write("68 in", font=("Times New Roman", 12, "normal"))
    build.penup()
    build.goto(-60,200)
    build.pendown()
    build.circle(40,)
    build.penup()
    build.circle(40,90)
    build.pendown()
    build.right(180)
    build.forward(400)
    build.right(90)
    build.forward(80)
    build.right(90)
    build.forward(400)
    build.right(180)
    build.penup()
    build.forward(300)
    build.right(40)
    build.pendown()
    build.forward(60)
    build.left(130)
    build.forward(30)
    build.left(55)
    build.forward(15)
    build.right(145)
    #Leg one done ^
    build.penup()
    build.forward(30)
    build.pendown()

    #Leg 2 start
    build.right(90)
    build.forward(60)
    build.right(90)
    build.forward(45)
    build.right(90)
    build.forward(44)
    build.penup()
    build.forward(40)
    build.left(90)
    build.forward(25)
    build.right(180)
    build.pendown()

    build.right(28)
    build.forward(150)
    build.left(120)
    build.forward(30)
    build.left(60)
    build.forward(100)

    build.left(36)
    build.forward(42)
    build.penup()
    build.left(140)
    build.forward(150)


    build.right(30)
    build.forward(20)

    build.right(170)
    build.forward(47)
    build.right(190)
    build.pendown()
    build.forward(45)

    build.left(128)

    build.forward(50)
    build.left(65)
    build.forward(68)

    #Third leg start
    build.penup()
    build.forward(40)
    build.left(50)
    build.forward(79)
    build.right(90)
    build.pendown()
    build.right(91)

    build.forward(45)
    build.left(180)
    build.forward(45)
    build.right(147)
    build.forward(160)
    build.right(136)
    build.forward(36)
    build.right(45)
    build.forward(98)
    build.penup()
    build.left(149)
    build.forward(65)
    build.left(50)
    build.pendown()
    build.forward(70)
    build.left(60)
    build.forward(55)
    build.left(119)
    build.forward(57)

    #leg 4

    build.penup()
    build.forward(47)
    build.right(50)
    build.forward(60)
    build.pendown()
    build.right(130)
    build.forward(70)
    build.right(145)
    build.forward(30)
    build.right(30)
    build.forward(24)
    build.right(180)
    build.right(40)

    build.penup()
    build.right(14)
    build.forward(25)
    build.pendown()
    build.left(90)
    build.forward(55)
    build.left(91)
    build.forward(50)
    build.left(90)
    build.forward(55)

    build.penup()
    build.seth(180)
    build.goto(250, -200)
    build.pendown()
    build.showturtle()
    build.forward(50)
    build.goto(225, -200)
    build.seth(90)
    build.forward(500)
    build.goto(250, 300)
    build.goto(200, 300)

    build.penup()
    build.goto(100, -225)
    build.seth(60)
    build.pendown()
    build.forward(25)
    build.right(180)
    build.forward(50)
    build.seth(60)
    build.forward(150)
    build.right(90)
    build.forward(25)
    build.right(180)
    build.forward(50)

    done()
turtle_drawing()
