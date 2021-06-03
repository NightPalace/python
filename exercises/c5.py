# 5-8
logging_name = 'eric'
if logging_name == 'admin':
	print('Hello admin, would you like to see a status report ?')
else:
	print('Hello ' + logging_name + ', thank you for logging in again.')

# 5-10
current_users = ['john', 'zoe', 'sara', 'lucy', 'sam'] # all in lowercase
new_users = ['elize', 'ZOe', 'babara', 'huke', 'Sam']
for n in new_users:
	if n.lower() in current_users:
		print('name ' + n.title() +' already been used')
	else:
		print('beautiful name: ' + n.title())

# 5-11
numbers = list(range(1, 10))
for n in numbers:
	if n == 1:
		print('1st\n')
	elif n == 2:
		print('2nd\n')
	elif n == 3:
		print('3rd\n')
	else:
		print(str(n) + 'th\n')