#Q1

#input phase
num_shares = int(input("Enter number of shares: "))
price_per_share = float(input("Enter price per share: "))

#process phase
total_cost = num_shares * price_per_share

#output phase
display = "The total cost is: $" + str(total_cost)

#Q2
#input phase
last_name = input("Enter last name: ")
midterm_score = float(input("Enter midterm score: "))
final_score = float(input("Enter final score: "))

#Process phase
total_exam_points = midterm_score + final_score

#output phase
display = last_name + " has " + str(total_exam_points) + " exam points"

#Q3
#input phase
job_name= input("Enter job name: ")
total_paid = float(input("Enter total paid: "))

#process phase
amount_per_person = total_paid / 3

#output phase
display = "Each person should receive $" + str(amount_per_person) + " for " + job_name"

#Q4
#input phase
Make = input("Enter make: ") 
Model = input("Enter model: ")
Msrp = float(input("Enter MSRP: "))
Discount_percent = float(input("Enter discount percent: "))

#process phase
Discount_amount = Msrp * (Discount_percent / 100)
discount_price = Msrp - Discount_amount

#output phase
display = "The " + Make + " " + Model + " with an MSRP of $" + str(Msrp) + " has a discount of $" + str(Discount_amount) + " and a final price of $" + str(discount_price)

#Q5
#input phase
r= float(input("Enter radius: "))

#process phase
area = 3.14 * r * r
perimeter = 2 * 3.14 * r

#output phase
display = "The area is: " + str(area) + " and the perimeter is: " + str(perimeter)
