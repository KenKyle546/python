print()
print('Please provide the following information to obtain your ID Badge: ')
print()
first_name = input('First Name: ')
last_name = input('Last Name: ')
email_address = input('Email Address: ')
while '@' not in email_address:
    print('ERROR: Please enter a valid email address: ')
    email_address = input(' ')
phone_num = input('Phone Number: ')
job_title = input('Job Title: ')
id_num = input('ID Number: ')
hair_color = input('Hair Color: ')
eye_color = input('Eye Color: ')
start_month = input('Month Started: ')
start_year = input('Year Started: ')
adv_training = input('Have you completed your advanced training? (Y/N): ') 
    
while True:
    adv_training = input('ERROR: Please enter either "Y" or "N": ')
    if adv_training == 'Y':
        break
    if adv_training == 'y':
        break
    if adv_training == 'N':
        break
    if adv_training == 'n':
        break
    
print()
print()
print('Thank you, ' + first_name + '!  Here is your ID Badge:')
print()

# Here is where the ID badge will print --------------------------

print('---------------------------------------------')
print()
print(last_name.upper() + ', ' + first_name.capitalize())
print(job_title.title())
print('ID: ' + id_num)
print()
print(email_address.lower())
print(phone_num)
print()


print(f"{'Hair: ' + hair_color:<25} Eye Color: {eye_color}")
print(f"{'Start: ' + start_month.capitalize() + ', ' + start_year:<25} Training: {adv_training.capitalize()}")


print()
print('---------------------------------------------')

print()
print('Thank you')

