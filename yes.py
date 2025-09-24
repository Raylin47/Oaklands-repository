def start():
 print("hello choose options between 1 to 3")
 global choice
 global availability
 availability = [ "0","2","3","1"]
 while True:
  try:
   choice = int(input())
   break 
  except ValueError:
   print("Error occured")
   
 if choice in (1, 2, 3):
         validation()
 while choice not in (1,2,3):
         print("error there is no such an option")
         start()
    
def validation():
    
    print("are you sure youd like number",choice,"?")
    print("Please type yes or no")   
    
    response = input()
    if response.lower() == ("yes"):
        purchase()
    elif response.lower() == ("no"):
          print("please select desired option")
          start()
          
    else:
        print("Sorry error occured we are bringing you back to the main menu")
        start()
def purchase():
    value = ["0", "12", "15.5", "20"]
    print("that will cost", value[choice],"£")
    print("please enter amount in integer or float values")
    while True:
     try:
       payment = float(input())
       break
     except:
         print("Incorrect datatype please type integers or float numbers")
         print("that will cost", value[choice],"£")
    if payment < float(value[choice]):
        print("insufficient balance")
        validation()
     
    elif payment>=float(value[choice]):
       result = payment - float(value[choice])
       print("your change is",round(result, 3), "£")
       print("product have been disposed have a nice day")
       availability[choice]=int(availability[choice]) - 1
       print(availability[choice],"products left") 
start()



          

    
          
             





     
