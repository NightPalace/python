# 4-3
for i in range(1, 21):
	print(i)
# 4-5
numbers = list(range(1, 100001))
print(numbers)
print('min number is in first ? ' + str(min(numbers) == numbers[0]))
print('max number is in last ? ' + str(max(numbers) == numbers[-1]))
print(sum(numbers))
# 4-6
old_numbers = list(range(1, 21, 2))
print(old_numbers)
# 4-7
three_numbers = list(range(3, 31, 3))
print(three_numbers)
# 4-8, 4-9
cubes = [value ** 3 for value in range(1, 11)]
for i in cubes:
	print(i)