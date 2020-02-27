
def run():
	counter = 0
	with open('test.txt') as f:
		for line in f:
			counter += line.count('audiobook')
	print('The word "audiobook" is {} times in the file'.format(counter))


if __name__ == "__main__":
	run()