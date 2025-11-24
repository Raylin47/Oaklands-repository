
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
def CarOptions():
    count = 0
    for keys in options.keys():
     count += 1
     print(f"{count}.",keys)
    return count
def calculation():
    global CarCost
    CarCost = 0
    for car, price in chosen_cars.items():
      CarCost += price["price"]
      print(car, price["price"],"£")
       
options = {"Lamborghini Gallardo": {"price":59, "ID":1},
           "Lamborghini Huracan": {"price":59,  "ID":2},
           "Ferrari F40": {"price":39, "ID":3},
           "Porsche Boxster": {"price":39, "ID":4},
           "Audi A5": {"price":39, "ID":5},
           "BMW I8": {"price":39, "ID":6},
           "Lotus Elise": {"price":30, "ID":7}
           }

name = input("please enter your name:")
adress = input("Enter your adress:")


phone_num = validation(input("Enter your phone number:"))
NumCarsToDrive = validation(input("enter the amount of cars you'd like to drive, maximum 5:"))

while NumCarsToDrive>5 or 0>=NumCarsToDrive:
    print("Cannot drive more than 5 cars")
    NumCarsToDrive = validation(input("enter the amount of cars you'd like to drive, maximum 5:"))


CarNum = 0
chosen_cars = {}
chosen_ids = []
while CarNum < NumCarsToDrive:
   CarOptions()
   CarsToDrive = validation(input("which of the following cars would you like to drive? please enter a number:"))
   if CarsToDrive>CarOptions() or CarsToDrive<=0:
       print("there is no such an option please try again")
       continue
   for ID in chosen_cars.values():
     chosen_ids.append(ID["ID"])
   if CarsToDrive in chosen_ids:
           print("Error, you already have chosen that car")
           continue
   for car, info in options.items():
            if info["ID"] == CarsToDrive:
                print("your choice has been accepted")
                chosen_cars.update({car:{"price":info["price"], "ID":info["ID"]}})
                CarNum +=1
                print("Thats your choice number", CarNum,"the option you have chosen is", CarsToDrive, car)
while True:
    additional_laps = input("Would you like additional laps? yes/no:")
    if additional_laps.lower() == "yes":   
     num_aditional_laps = validation((input("enter the amount of additional laps:")))
     lap_cost = 15
     calculation()
     print(f"Additional laps {lap_cost} £")
     result = CarCost + lap_cost
     break
    elif additional_laps.lower() == "no":
     calculation()
     result = CarCost
     break
    else:
     print("there is no such an option please try again")
print(f"Total cost {result}£")

