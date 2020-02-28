from lamp import Lamp

def run():
	lamp = Lamp(is_turned_on=False)

	while True:
		command = str(input(
			'''
			What do you want to do?
			[o]On
			[f]Off
			[e]Exit
			'''
		))

		if command == 'o':
			lamp.turn_on()
		elif command == 'f':
			lamp.turn_off()
		else:
			quit()


if __name__ == "__main__":
	run()