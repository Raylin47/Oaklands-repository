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

ParcelType = {"small":{"size":95, "weight":2, "price":5,},
       "medium":{"size":150, "weight":15, "price":20,},
       "large":{"size":450, "weight"30:, "price":30,}}
count = 1
ParcelsInfo = {}
messages = {"name":"Greetings could you enter your name?:",
            "adress":"Please enter your adress:",
            "phone number":"Please enter your phone number:",
            "Parcel number":"Please enter the number of parcels to collect:",
            "Signature": "Do you want a signature on delivery? yes/no",
            "tracking": "Do you want a parcel tracking? yes/no"}

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
    height = digit_validation(f"Please enter height of the parcel number {count}:",input(f"Please enter height of the parcel number {count}:"))
    length = digit_validation(f"Please enter lenth of the parcel number {count}:",input(f"Please enter lenth of the parcel number {count}:"))
    width = digit_validation(f"Please enter width of the parcel number {count}:",input(f"Please enter width of the parcel number {count}:"))
    weight = digit_validation(f"Please enter the weight of your parcel number {count}:",Input = input(f"Please enter the weight of your parcel number {count}:"))
    EnsureData = yesNoCondition(Input = input(f"Are you sure that the following data for parcel number {count} is correct? yes/no:"), message  = "Are you sure that the following data for parcel number {count} is correct?yes/no:")
    if EnsureData == False:
        continue
    elif EnsureData == True:
        ParcelsInfo.update({f"parcel {count}":{"height":height, "length":length,"width":width,"weight":weight}})
        count = count + 1
