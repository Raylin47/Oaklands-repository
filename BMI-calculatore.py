#bmi
#assigning variables

#validation of input
def loop():
 
 while True:
     try:
        weight = float(input("Enter your weight in killograms:"))
        height = float(input("please enter your height in meters:"))
        break
     except ValueError:
        print("wrong input")
 result = weight/(height**2)
 choise = input("would you like to continue? yes/no:")
 if choise.lower() == "yes":
    print(count,result)
    loop()
 elif choise.lower() =="no":
    print(count,result)
 else:
    loop()
loop()
   



 
