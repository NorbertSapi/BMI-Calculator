# This is my BMI class
import math


# create class BMI3
class BMI3:
    pass

    def __init__(self, name):
        assert isinstance(name, object)
        self.name = name

# this method counts BMI
    def choose_weight_measurement(self):
        measurement = input("Would you like to use kg or lbs? ")
# this part use meter and kg to count BMI
        if measurement == "kg":
            kg = float(input("Please enter your weight in kg: "))
            cm = input("Please enter your height in centimeter: ")
            meter = float(cm) / 100
            bmi = float(kg) / math.pow(float(meter), 2)
            print("Your BMI index is {0:4.2f}".format(bmi))
            # what does your BMI means
            if bmi < 18.00:
                print("Underweight")
            elif 19 <= bmi < 25:
                print("Healthy")
            elif 25 <= bmi < 30:
                print("Overweight")
            elif 30 <= bmi < 40:
                print("Obese")
            else:
                "Extremely Obese"
# this part use lbs and inches to count BMI
        elif measurement == "lbs":
            lbs = input("Please enter your weight in lbs ")
            inches = input("Please enter your height in inches: ")
            bmi = float(lbs) / float(inches) / float(inches) * 703
            print("Your BMI index is {0:4.2f}".format(bmi))
            # what does your BMI means
            if bmi < 18.00:
                print("Underweight")
            elif 19 <= bmi < 25:
                print("Healthy")
            elif 25 <= bmi < 30:
                print("Overweight")
            elif 30 <= bmi < 40:
                print("Obese")
            else:
                "Extremely Obese"
# this part handle wrong input for the measurement choice
        else:
            print("You need to choose between kg or lbs!")
            self.choose_weight_measurement()
