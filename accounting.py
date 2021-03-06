"""
melon_cost = 1.00

customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00

customer1_expected = customer1_melons * melon_cost
if customer1_expected != customer1_paid:
    print(f"{customer1_name} paid ${customer1_paid:.2f},",
          f"expected ${customer1_expected:.2f}"
          )

customer2_expected = customer2_melons * melon_cost
if customer2_expected != customer2_paid:
    print(f"{customer2_name} paid ${customer2_paid:.2f},",
          f"expected ${customer2_expected:.2f}"
          )

customer3_expected = customer3_melons * melon_cost
if customer3_expected != customer3_paid:
    print(f"{customer3_name} paid ${customer3_paid:.2f},",
          f"expected ${customer3_expected:.2f}"
          )

customer4_expected = customer4_melons * melon_cost
if customer4_expected != customer4_paid:
    print(f"{customer4_name} paid ${customer4_paid:.2f},",
          f"expected ${customer4_expected:.2f}"
          )

customer5_expected = customer5_melons * melon_cost
if customer5_expected != customer5_paid:
    print(f"{customer5_name} paid ${customer5_paid:.2f},",
          f"expected ${customer5_expected:.2f}"
          )

customer6_expected = customer6_melons * melon_cost
if customer6_expected != customer6_paid:
    print(f"{customer6_name} paid ${customer6_paid:.2f},",
          f"expected ${customer6_expected:.2f}"
          )
"""
# Function check every order for overpayment or underpayment and terurns
# human readable info
import math
def payment_status(file_name):
    current_report = open(file_name) 
    for line in current_report:
        line = line.strip() # het rid of white spaces on the left and right
        order = line.split("|") # create a list with enfo for each individual order
        order_num = order[0]
        customer = order[1]
        customer = customer.split(" ")
        first_name = customer[0]
        last_name = customer[1]
        expected = float(order[2])
        paid = float(order[3])
        status = "paid in full"
        due = round(abs(paid - expected), 2)
        
        if expected < paid:
            status = "overpaid"
        elif expected > paid:
            status = "underpaid"
        print(f"{first_name} {last_name} {status}, expected {expected}. Due ${due}")

payment_status("customer-orders.txt")