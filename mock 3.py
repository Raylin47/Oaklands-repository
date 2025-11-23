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
     return int(inputs)
    except:
     print("sorry wrong data type try again")
     while True:
          try:
              inputs = int(input())
              return inputs
          except ValueError:
            print("sorry wrong data type try again")

options = {"Lamborghini Gallardo": {"price":59, "ID":1},
           "Lamborghini Huracan": {"price":59,  "ID":2}}

#options = {"Lamborghini Gallardo": 59, #59£
           #"Lamborghini Huracan": 59, #59£
           #"Ferrari F40": 39, #39£
           #"Porsche Boxster":39,#39£
           #"Audi A5": 39, #39£
           #"BMW I8":39, #39£
           #"Lotus Elise":30} #30£

name = input("please enter your name:")
adress = input("Enter your adress:")


phone_num = validation(input("Enter your phone number:"))
print(type(phone_num), phone_num)
NumCarsToDrive = validation(input("enter the amount of cars you'd like to drive, maximum 5:"))

while NumCarsToDrive>5 or 0>=NumCarsToDrive:
    print("Cannot drive more than 5 cars")
    NumCarsToDrive = validation(input("enter the amount of cars you'd like to drive, maximum 5:"))
user_input = {1: "Lamborghini Gallardo"}

CarNum = 0
count = 0
chosen_cars = {}
for keys in options.keys():
    count += 1
    print(f"{count}.",keys)
while CarNum < NumCarsToDrive:
   CarsToDrive = validation(input("which of the following cars would you like to drive? please enter a number:"))
   if CarsToDrive>count or CarsToDrive<=0:
       print("there is no such an option please try again")
       continue
   else:
        for car, info in options.items():
            if car in chosen_cars:
                print(f"Unfortunately you already have chosen {car}")
                continue
            elif info["ID"] == CarsToDrive:
                print("your choice has been accepted")
                chosen_cars.update({car:info["price"]})
                CarNum +=1
                print(CarNum,"your option is", CarsToDrive)
        
additional_laps = input("Would you like additional laps? yes/no:") #additional laps 15£
num_aditional_laps = validation((input("enter the amount of additional laps:")))

