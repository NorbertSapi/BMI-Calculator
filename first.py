
def choose_hight_measurement()
    measurement = input("Would you like to use kg or lbs?")
        if measurement == "kg"
            #if answer kg = True
            kg = input("Please enter your weight in kg: ")
            meter = input("Please enter your height in meter: ")

            my_bmi = float(kg) / float(meter).__pow__(2)
            print("Your BMI index is {0:4.2f}".format(my_bmi))
        elif measurement == "lbs"
            lbs = input("Please enter your weight in lbs ")
            inches = input("Please enter your height in inches: ")
            my_bmi = float(lbs) / float(inches) / float(inches) * 703
            print("Your BMI index is {0:4.2f}".format(my_bmi))
        else:
            print("You need to choose between kg or lbs!")

