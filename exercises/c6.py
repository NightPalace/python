# 6-2
favorite_numbers = {
	'sara': 12,
	'holy': 45,
	'jim': 2,
	'zoe': 0,
	'sophia': 32,
}
for name, number in favorite_numbers.items():
	print(name.title() + "'s favorite number is " + str(number))

# 6-12
print("\n")
friends = {
	'sara': {
		'number': 12,
		'location': 'new york',
		'major': 'frech',
		'pet': ['cat', 'dog']
	},
	'holy': {
		'number': 45,
		'location': 'tokyo',
		'major': 'philosophy',
		'pet': ['cat']
	},
	'jim': {
		'number': 2,
		'location': 'tokyo',
		'major': 'philosophy',
		'pet': []
	},
	'zoe': {
		'number': 0,
		'major': 'Chinese language and Literature',
		'pet': ['snake']
	},
	'sophia': {
		'number': 32,
		'location': 'beijing',
		'major': 'math',
		'pet': ['pig']
	},
}
for name, info in friends.items():
	for k, v in info.items():
		if k == 'number':
			number_str = name.title() + "'s favorite number is " + str(v) + ", "
		elif k == 'location':
			loca_str = "and he lives in  " + v + ". "
		elif k == 'major':
			major_str = "His major is " + v + ".  "
		elif k == 'pet':
			length = len(v)
			if length == 0:
				pet_str = "Besides, he don't have any pets."
			elif length > 1:
				pet_str = "Besides, he has " + str(len(v)) + " pets: "
				while length > 0:
					pet_str += v[length - 1] + ", "
					length -= 1;
			else:
				pet_str = "Besides, he only have one pet: " + v[0] + "."
	print(number_str + loca_str + major_str + pet_str + "\n")