'''
This is a Simple BMI Calculator.
My goal is to develop a small Python project in 2 weeks to learn and practise PYTHON3 as a new programming language.
'''

# get input from user and interact
my_name = input("Please enter you name ")
print('Hello ' + my_name + ' nice to meet you.')

# get the weight and the height information
my_weight = input('Please enter your weight in kg ')
my_height = input('Please enter your height in cm ')
print("{} you are {} cm tall and your weight is {} kg.".format(my_name, my_height, my_weight))


# I collect data in cm to make it easy for the user to answer.
# convert cm to meter
my_height_in_meter = int(my_height) / 100

# count my_bmi
my_bmi = float(my_weight)/float(my_height_in_meter).__pow__(2)
print("Your BMI index is {0:4.2f}".format(my_bmi))


#myBMI = float(count_bmi())
bmi = float(my_bmi)

# what does your BMI means
if my_bmi < 18.00:
    print("Underweight")
elif my_bmi >=19 and my_bmi <25:
    print("Healthy")
elif my_bmi >= 25 and my_bmi < 30:
    print("Overweight")
elif my_bmi >= 30 and myBMI <40:
    print("Obese")
else:"Extremely Obese"

