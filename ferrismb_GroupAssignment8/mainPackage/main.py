#main.py
#Name: Morgan Ferris, Max Schiller, Riley Kinkade
# Email: schillmx@mail.uc.edu, ferrismb@mail.uc.edu, kinkadrj@mail.uc.edu
# Assignment 08
# Due Date: March 28
#Course: IS4010
# Semester/Year: Spring 2024
# Brief Description of this assignment: This assignment shows our ability to connect to SQL server and implement the information into our own code
# Brief description of this module: This module shows all the code we created to demonstrate our knowledge of the SQl server
# Citations: Bill. Nicholson's brain
# Anything else thats relevant: Go Reds








import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=GroceryStoreSimulator;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')

cursor = conn.cursor()

cursor.execute("SELECT o.OrderID, o.LoyaltyID, o.DateTimeCreated, o.StoreID, o.OrderStatusID, o.DeliveryCharge, o.Notes, o.DeliveryAddress, o.DateTimeDelivered, MAX(CAST(o.AllOrNone AS INT)) AS AllOrNone, od.OrderDetailID, od.ProductID, od.Quantity, od.TotalAmountChargedToCustomer, od.Comment, od.CouponDetailID, od.UnavailableWhenOrderWasFilled FROM tOrder o JOIN tOrderDetail od ON o.OrderID = od.OrderID WHERE o.DateTimeCreated >= '2024-01-01' GROUP BY o.OrderID, o.LoyaltyID, o.DateTimeCreated, o.StoreID, o.OrderStatusID, o.DeliveryCharge, o.Notes, o.DeliveryAddress, o.DateTimeDelivered, od.OrderDetailID, od.ProductID, od.Quantity, od.TotalAmountChargedToCustomer, od.Comment, od.CouponDetailID, od.UnavailableWhenOrderWasFilled")

rows = cursor.fetchall()

total_orders = len(rows)
total_products_ordered = sum(row.Quantity for row in rows)
total_amount_charged = sum(row.TotalAmountChargedToCustomer for row in rows)

summary_sentence = f"In the analyzed data, there were {total_orders} orders placed, involving a total of {total_products_ordered} products, with a total amount charged of ${total_amount_charged}."


print(summary_sentence)

conn.close()
