def first_not_repeating_char(char_sequence):
	seen_letters = {}

	for idx, letter in enumerate(char_sequence):
		if letter not in seen_letters:
			seen_letters[letter] = (idx, 1)
		else:
			seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1]+1)

	final_letters = []
	for key, value in seen_letters.items():
		if value[1] == 1:
			final_letters.append((key, value[0]))
	
	not_repeated_letter = sorted(final_letters, key=lambda value: value[1])

	if not_repeated_letter:
		return not_repeated_letter[0][0]
	else:
		return '_'


if __name__ == "__main__":
	char_sequence = str(input('Put a sequence of characters: '))

	result = first_not_repeating_char(char_sequence)

	if result == '_':
		print('All the characters are repeated')
	else:
		print("The first character that doesn't repeat is {}".format(result))