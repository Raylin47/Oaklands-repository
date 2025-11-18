def calculation():
    price = { "small": 3.25, "medium": 5.50, "large":7.15}
    

name = input()
adress = input()
while True:
 try:
   phone_number = int(input("+"))
   break
 except ValueError:
  print("type phone number in integers")

print("enter the quantity of pizza being ordered")

while True:
  try:
   quantity = int(input())
   while quantity<=0 or quantity >=6:
       print("You can only enter from 1 to 6 pizzas")
       quantity = int(input())
   break
  except ValueError:
   print("quantity accepts only integer values (numbers type from 1 up to 6)")

print("please enter the size of the pizza")
size = input()
while size.lower() not in ("small","big","medium"):
    print("please try again")
    size = input()





  
