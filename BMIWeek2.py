# this is week 2
#import math for power meter
import math

#create a function to calculate bmi
def choose_hight_measurement(bmi):
    measurement = input("Would you like to use kg or lbs?")
    # add ErrorHandling!!!
    if measurement == "kg":
        kg = float(input("Please enter your weight in kg: "))
        meter = input("Please enter your height in meter: ")
        bmi = float(kg) / math.pow(float(meter), 2)
        print("Your BMI index is {0:4.2f}".format(bmi))
        return bmi
    elif measurement == "lbs":
        lbs = input("Please enter your weight in lbs ")
        inches = input("Please enter your height in inches: ")
        bmi = float(lbs) / float(inches) / float(inches) * 703
        print("Your BMI index is {0:4.2f}".format(bmi))
        return bmi
    else:
        print("You need to choose between kg or lbs!")
        choose_hight_measurement("kg")

def add_bmi_result(result):
    if my_bmi < 18.00:
        print("Underweight")
    elif my_bmi >= 19 and my_bmi < 25:
        print("Healthy")
    elif my_bmi >= 25 and my_bmi < 30:
        print("Overweight")
    elif my_bmi >= 30 and myBMI < 40:
        print("Obese")
    else:
        "Extremely Obese"

# get input from user and interact
my_name = input("Please enter you name ")
print('Hello %s nice to meet you.' % my_name)

# call choose_hight_measurement function
my_bmi=choose_hight_measurement("kg")

# call bmi_result function
add_bmi_result("True")
