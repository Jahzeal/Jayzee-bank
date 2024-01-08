# from twilio.rest import Client

# account_sid = ''
# auth_token = ''
# client = Client(account_sid, auth_token)

# message = client.messages \
#     .create(
#         body= ' how',
#         from_='hhg',
#         to='17325736616'
#     )
# import csv
# with open('story.txt', 'r') as file:
#     csvread = csv.reader(file)
#     for row in csvread:
#         print(row)




# with open("love.txt", "w", encoding='utf8') as file:
#     file.write("Writting files is great\n")
#     file.write("closing files is cool\n")
# from csv import reader
# with open ("account.csv", encoding='utf8') as file:
#     csv_reader = reader(file)
#     for row in csv_reader:
#         print(row)
# from csv import writer
# from csv import reader, DictWriter
# # with open("cats.csv", "w") as file:
# #     csv_writer = writer(file)
# #     csv_writer.writerow(["notes"])
# #     csv_writer.writerow(["i hate cats"])

# # with open("account.csv", encoding="utf8") as file:
# #     csv_reader = reader(file)
# #     acconts = [[s.upper() for s in row] for row in csv_reader]
# #     for row in acconts:
# #         print(row)

# # with open ("new.csv", "w") as file:
# #     csv_writer = writer(file)
# #     for accounted in acconts:
# #         csv_writer.writerow(accounted) 



# # with open("cat.csv", "w") as file:
# #     headers = ['name','breed','food']
# #     csv_write = DictWriter(file, fieldnames=headers)
# #     csv_write.writeheader()
# #     csv_write.writerow({
# #         "name": "garfield",
# #         "breed":"grey",
# #         "food":"beans"
# #     })
# import csv

# with open('account.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     name = input("Enter name: ")
#     amt = float(input("amount"))
#     found = False
#     rows = []

#     for i in reader:
#         if name == i['username']:
#             # i['balance'] += amt
#             i['balance'] = str(float(i['balance']) + amt)
            
#             found = True
#         rows.append(i)

# if found:
#     with open("account.csv", "w", newline='') as file:
#         headers = ['username', 'password', 'pin','account_number','balance']
#         csv_write = csv.DictWriter(file, fieldnames=headers)
#         csv_write.writeheader()
#         csv_write.writerows(rows)
#     print(f"Updated information for {name}.")
# else:
#     print(f"No cat with the name {name} found.")



# # Find the row with the bank balance
# header_row = rows[0]
# balance_index = header_row.index('balance')
# balance_row = rows[1]

# # Check if the deposited amount is above 10
# deposited_amount = 20 # Replace with the actual deposited amount
# if deposited_amount > 10:
#   # Update the balance with the deposited amount
#   balance_row[balance_index] = str(deposited_amount)
#   print("Deposit successful!")
# else:
#   print("Deposit amount must be above 10.")

# # Write the updated contents back to the CSV file
# with open('account.csv', 'w', newline='') as file:
#   writer = csv.writer(file)
#   writer.writerows(rows)







# with open ("account.csv", "r", encoding="utf-8") as file:
#     amount = int(input("Enter your deposit!"))
#     name = input("enter name: ")
#     reader = csv.reader(file)
#     # header = reader.pop(0)
#     for i in reader:
#         if i[0] == name:
#             with open("account.csv", "w", encoding="utf-8") as file:
#                 i[-1] += str(amount)
#                 writer = csv.writer(file)
#                 writer.writerow(reader)
#             break
#         elif i[0] != name:pass
#         else:
#             print("user not found")
    