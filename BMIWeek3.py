# This is my 3rd week in "Wonderland. - said Alice
# Version 3 for BMI Calculator

from BMI3 import BMI3

# create global variable "my_name"
# get input from user and interact
my_name = input("Please enter you name ")
print('Hello %s nice to meet you.' % my_name)

# use global variable "my name" as a value for BMI3 class
name1 = BMI3(my_name)
# call choose_height_measurement function
name1.choose_weight_measurement()

# call bmi_result method
# name1.bmi_result()

