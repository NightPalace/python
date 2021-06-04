# 7-9
sandwich_orders = ['s1', 's2', 'pastrami', 's3', 's4', 'pastrami']
finished_sandwiches = []

str;
for sanwich in sandwich_orders:
	if sanwich != 'pastrami':
		finished_sandwiches.append(sanwich)
	else:
		del sanwich
print(finished_sandwiches)
print('熟食店的五香烟熏牛肉卖完了')

promt = '\nwhich kind of sanwich would you like to order ?'
answner = input(promt)
if answner in finished_sandwiches:
	print('your sanwich ' + answner + ' has finished.')
else:
	print('sorry, not supply.')