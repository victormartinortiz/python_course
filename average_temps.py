def average_temps(temps):
	sum_of_temps = 0

	for temp in temps:
		sum_of_temps += float(temp)
	return sum_of_temps / len(temps)




if __name__ == "__main__":
	temps = [22,22,24,23,25,21]

	average = average_temps(temps)

	print('The average temp is: {}'.format(average))