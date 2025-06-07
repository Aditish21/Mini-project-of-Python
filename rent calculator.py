# inputs we need from the user
#total rent 
# Total food ordered for snacking 
# electricity units spend 
# charge pr unit 
#persons living in room of hostel
#output 
#total amount you have to pay is

rent=int(input("enter your hostel rent= "))
food=int(input("enter the amount of food enter ="))
electricity_spend= int(input("enter the total of electricity spend="))
charge_per_unit= int(input("enter the charge per unit="))
person=int(input("enter the number of person living in room="))
total_bill= electricity_spend*charge_per_unit
output= (rent+food+ total_bill )//person
print("each peson will pay=",output)
