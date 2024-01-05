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




with open("love.txt", "w", encoding='utf8') as file:
    file.write("Writting files is great\n")
    file.write("closing files is cool\n")

