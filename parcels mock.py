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
         
messages = {"name":"Greetings could you enter your name?:",
            "adress":"Please enter your adress:",
            "phone number":"Please enter your phone number:",
            "Parcel number":"Please enter the number of parcels to collect:",
            "Parcel height": "Please enter height of the parcel:",
            "Parcel length": "Please enter lenth of the parcel",
            "Parcel width": "Please enter width of the parcel",
            "Parcel weight":"Please enter the weight of your parcel",
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
count = 1
while parcels_num >= count:
    
    
    
