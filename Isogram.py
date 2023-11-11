def is_isogram(str_):
	lower_case_word = str_.lower()
	word_letter_list = []

	for letter in lower_case_word:
		if letter.isalpha():
			if letter in word_letter_list:
				return f"{lower_case_word} is not isogram"
			word_letter_list.append(letter)
	return f"{lower_case_word} is  isogram"

if __name__ == '__main__':
	print(is_isogram("Vaishnavi"))



