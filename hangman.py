import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

def random_word():
	idx = random.randint(0, len(WORDS)-1)
	return WORDS[idx]

def display_board(hidden_word, tries):
	print(IMAGES[tries])
	print('')
	print(hidden_word)
	print('---*---*---*---*---*---*---*---*---*---*---*')

def run():
	word = random_word()
	hidden_word = ['-'] * len(word)
	tries = 0

	while True:
		display_board(hidden_word, tries)
		current_letter = str(input('guess a character: '))

		letter_indexes = []

		for idx in range(len(word)):
			if word[idx] == current_letter:
				letter_indexes.append(idx)

		if len(letter_indexes) == 0:
			tries += 1

			if tries == 7:
				display_board(hidden_word, tries)
				print('')
				print("You Lose, the secret word was '{}'".format(word.upper()))
				break
		else:
			for idx in letter_indexes:
				hidden_word[idx] = current_letter

			letter_indexes = []

		try:
			hidden_word.index('-')
		except ValueError:
			print('')
			print("You won, the word was '{}'".format(word.upper()))
			break


if	__name__ == '__main__':
	print('''
	

 __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __. 
|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  | 
|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  | 
|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  | 
|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   | 
|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__| 
                                                                                


	''')
	run()