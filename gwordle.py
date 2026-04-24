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
	result = []

	for i,c in enumerate(guess):
		if c == word[i]:
			result.append("🟩")
		elif c in word:
			result.append("🟨")
		else:
			result.append("⬛️")
	return " ".join(result)


def main():
	MAX_ATTEMPTS = 6
	ATTEMPT = 0
	word = get_word()


	while ATTEMPT < MAX_ATTEMPTS:
		print(f"Attempt: {ATTEMPT}")
		print("Enter Word")
		guess = input()
		
		if len(guess) != len(word):
			print(f"Word must be {len(word)} letters long")
			continue

		print(get_feedback(guess, word))

		if guess == word:
			print(f"{guess} is correct")
			return

		ATTEMPT +=1
	print("Out of attempts\n")	
	print(word)

if __name__ == '__main__':
	main()