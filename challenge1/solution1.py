# Capture information
name = input('Please tell me your name: ')
age = input('Please tell me your age: ')
reddit_username = input('Please tell me your Reddit Username: ')

# Print the information in requested format
print('Your name is ' + name + ', You are ' + age + ' years old, \
and your username is ' + reddit_username)

# Extra Credit: Save information to file for use later
user_info = (name, age, reddit_username)
save_user_info = str(user_info)
file = open('userinfo.txt', 'w')
file.write(save_user_info)
