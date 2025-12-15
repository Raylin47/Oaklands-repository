# parcel program
def digit_validation(message, Input):
 try:
    return int(Input)
 except:
    print("wrong datatype try again")
 while True:
     try:
       Input = int(input(message))
       return int(Input)
     except:
         print("wrong datatype try again")
def float_validation(message, Input):
   try:
    return float(Input)
   except:
    print("wrong datatype try again")
   while True:
     try:
       Input = float(input(message))
       return float(Input)
     except:
         print("wrong datatype try again")  
def yesNoCondition(message, Input, boolean = None):
 while True:
    if Input.lower() == "yes":
        print("your choice saved as yes")
        boolean = True
        return boolean
    elif Input.lower() == "no":
        print("your choice saved as no")
        boolean = False
        return boolean
    else:
        print("input is incorrect, please type yes or no")
        Input = input(message)
        continue
result = 0
count = 1
ParcelsInfo = {}
messages = {"name":"Greetings could you enter your name?:",
            "adress":"Please enter your adress:",
            "phone number":"Please enter your phone number:",
            "Parcel number":"Please enter the number of parcels to collect:",
            "Signature": "Do you want a signature on delivery for each parcel? yes/no:",
            "tracking": "Do you want a parcel tracking for each parcel? yes/no:"}

name = input(messages["name"])
adress = input(messages["adress"])
while True:
    phone_num = digit_validation(messages["phone number"],input(messages["phone number"]))
    if len(str(phone_num))== 10:
        break
    else:
        print("Length of your number doesnt match, please re-enter it, length of your number should be consisting of 10 digits")
while True:
    parcels_num = digit_validation(messages["Parcel number"],input(messages["Parcel number"]))
    if parcels_num >= 7 or 0 >= parcels_num:
        print("you can't enter more than 6 and less than 1 parcel")
    else:
        break

while parcels_num >= count:
    height = float_validation(f"Please enter height in centimeters of the parcel number {count}:",input(f"Please enter height in centimeters of the parcel number {count}:"))
    length = float_validation(f"Please enter length in centimeters of the parcel number {count}:",input(f"Please enter length in centimeters of the parcel number {count}:"))
    width = float_validation(f"Please enter width in centimeters of the parcel number {count}:",input(f"Please enter width in centimeters of the parcel number {count}:"))
    weight = float_validation(f"Please enter the weight in killograms of your parcel number {count}:",Input = input(f"Please enter the weight in killograms of your parcel number {count}:"))
    EnsureData = yesNoCondition(Input = input(f"Are you sure that the following data for parcel number {count} is correct? yes/no:"), message  = f"Are you sure that the following data for parcel number {count} is correct?yes/no:")
    if EnsureData == False:
        continue
    elif EnsureData == True:
        size = width + length + height
        if size <= 95 and weight <= 2 :
          ParcelsInfo.update({f"parcel {count}":{"height":height, "length":length,"width":width,"weight":weight, "type":"small", "price":5.00}})
        elif size <= 150 and weight <= 15:
            ParcelsInfo.update({f"parcel {count}":{"height":height, "length":length,"width":width,"weight":weight, "type":"medium", "price":20.00}})
        elif size <= 450 and weight <= 30:
            ParcelsInfo.update({f"parcel {count}":{"height":height, "length":length,"width":width,"weight":weight, "type":"large", "price":30.00}})
        else:
            print("sorry the data you have entered for the parcel is not acceptable")
            continue
        count = count + 1
Signature = yesNoCondition(messages["Signature"], input(messages["Signature"]))
tracking = yesNoCondition(messages["tracking"], input(messages["tracking"]))
print(f"Name:{name}")
print(f"Adress:{adress}")
print(f"Phone number:{phone_num}")
for keys, value in ParcelsInfo.items():
    result += value["price"]
    print(keys,"individual price: " + str(value["price"]) + "£,","weight of parcel: " + str(value["weight"]) + "kg,","height of parcel: " +  str(value["height"]) + "cm,","length of parcel: " +  str(value["length"]) + "cm,","width of parcel: " +  str(value["width"]) + "cm,", "Parcel type: " + value["type"])
    if Signature == True:
       result = result + 2.00
       print(f"additional signature price for {keys}: +2£")
    if tracking == True:
      result = result + 5.00
      print(f"additional tracking price for {keys}: +5£")
print(f"Overall cost: {result}£")
