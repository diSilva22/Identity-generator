# id number convert to bairth day - dinusha 
import datetime

# vlidation checkin func
def validity(NIC:str)-> bool:
    if not (len(NIC) == 8 or  len(NIC) == 12):
        return False
    elif not NIC.isdigit():
        return False
    else:
        return True

#born year calculator
def born_year(NIC:str) -> int:
    year = NIC[0:4]
    return int(year)

#gender checking
def gender(NIC):
    gen_digit = int(NIC[4:7])
    if gen_digit <= 500:
        return "Male"
    else:
        return "Female"

#date of birth calcultor
def date_of_birth(NIC: str):
    date_digit = int(NIC[4:7])
    if date_digit >= 500:
        date_digit-= 500

    start_date= datetime.date(born_year(NIC),1,1)
    born_date = start_date + datetime.timedelta(days=date_digit-2)
    return born_date

#find the day
def born_day(day: datetime.date)-> str:
    return day.strftime('%A')

#get id number
nic_num = input("Enter your NIC number(without letters) : ")

#validetion
if validity(nic_num)== False:
    print("Invalid entry.")
    exit()

#gender
Gender = gender(nic_num)

#year calculation
year = born_year(nic_num)

#born day calculation
date = (date_of_birth(nic_num))

#born date
day = date.strftime("%A")

#output
print("----------------------------------")
print(f"Your birthday : {date}" , day)
print("Your gender : ", Gender)
print("----------------------------------")