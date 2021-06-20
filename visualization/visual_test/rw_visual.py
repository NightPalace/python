import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
	rw = RandomWalk(50000)
	rw.fill_walk()
	# set window size
	plt.figure(dpi=128, figsize=(10,6))
	# add some color to points
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s = 1)
	# highlight the start point and end point
	plt.scatter(0,0,c='green', edgecolor='none', s=10)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=10)
	# # hide axis
	# plt.axes().get_xaxis().set_visible(False)
	# plt.axes().get_yaxis().set_visible(False)
	plt.show()
	keep_running = input("make another walk ? (y/n)")
	if keep_running == 'n':
		break