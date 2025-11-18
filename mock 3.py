#inputs - name, adresses, phone number, number of cars the customer would like to drive maximum 5, which cars the customer would like to drive, the number of additional laps.
#Output - Customer details, breakdown of costs, the total cost of experience.
#information - additional lap = 15£,
#Lamborghini Gallardo = 59
#Lamborghini Huracan = 59
#Ferrari F40 = 49
#Porsche Boxster = 39
# Audi A5 = 39
# BMW i8 = 39
# Lotus Elise = 30
def validation(inputs):
    try:
     int(inputs)
     return inputs
    except:
     print("sorry wrong data type try again, try again")
     while True:
          try:
              inputs = int(input())
              return inputs
          except ValueError:
            print("sorry wrong data type try again, try again")

options = {"Lamborghini Gallardo": 59,
           "Lamborghini Huracan": 59,
           "Ferrari F40": 39,
           "Porsche Boxster":39,
           "Audi A5": 39,
           "BMW I8":39,
           "Lotus Elise":30}

name = input("please enter your name:")
adress = input("Enter your adress:")


phone_num = validation(input("Enter your phone number:"))
NumCarsToDrive = validation(input("enter the amount of cars you'd like to drive, maximum 5:"))

while int(NumCarsToDrive)<5:
    print("Cannot drive more than 5 cars")
    NumCarsToDrive = validation(input("enter the amount of cars you'd like to drive, maximum 5:"))
for keys, value in options.items():
    print(keys)
CarsToDrive =input("which of the following cars would you like to drive?:")
additional_laps = input("Would you like additional laps? yes/no:")
num_aditional_laps = validation((input("enter the amount of additional laps:")))

