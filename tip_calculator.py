#This software is designed to calculate how much each person will pay, this includes both the final bill and a tip. 

print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What tip percentage would you like to give? 10, 12, or 15? "))
people = int(input("How many people will be splitting the bill?"))

#Firstly it converts the number from above to a percentage
tip_as_percent = tip / 100
#It will then check agaasint the total bill to see the actual percent amount
total_tip_amount = bill * tip_as_percent
#It will then add the percent to the bill
total_bill = bill + total_tip_amount
#And lastly it will split the total bill between the people
bill_per_person = total_bill / people
#It will then round this number to 2 decimal places
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")