import random

# list from /usr/share/dict/words

WORD_LIST = "/usr/share/dict/words"

MATCHES = {"🟨", "🟩", "⬛️"}

def get_word(min_len=5, max_len=5):
    with open(WORD_LIST, 'r') as wl:
        words = [w.strip() for w in wl if min_len <= len(w.strip()) <= max_len]
    #print(random.choice(words))
    return random.choice(words)

def get_feedback(guess, word):
	result = ["⬛️"] * len(guess)
	word_rem = []


	for i,c in enumerate(guess):
		if c == word[i]:
			result[i]="🟩"
		else:
			word_rem.append(word[i])

	for i, c in enumerate(guess):
		if result[i] == "🟩":
			continue
		if c in word_rem:
			result[i] = "🟨"
			word_rem.remove(c)

	return " ".join(result)

def play_wordle(word, guesses):
    board = []

    for guess in guesses:
        feedback = get_feedback(guess.lower(), word.lower())
        board.append(f"{feedback}")
        if guess.lower() == word.lower():
            break

    print("\n".join(board))


def main():
	MAX_ATTEMPTS = 6
	ATTEMPT = 0
	guesses = []
	word = get_word()
	
	#print(word)


	while ATTEMPT < MAX_ATTEMPTS:
		print(f"Attempt: {ATTEMPT}")
		print("Enter Word")
		guess = input()
		
		if len(guess) != len(word):
			print(f"Word must be {len(word)} letters long")
			continue

		guesses.append(guess)
		print(get_feedback(guess, word))
		ATTEMPT +=1

		if guess == word.lower():
			print(f"\n{guess.upper()} is correct!")
			play_wordle(word, guesses)
			return

	print("Out of attempts!\n")
	play_wordle(word, guesses)
	print(f"The word was: {word.upper()}")

if __name__ == '__main__':
	main()