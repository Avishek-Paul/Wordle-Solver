from trie import Trie

word_dict = open("word_list.txt").readlines()
trie = Trie()

num_letters = input("How many letters is the wordl?: ")
num_letters = int(num_letters) if num_letters else 5

for word in word_dict:
    word = word.strip()
    if len(word) == num_letters:
        trie.insert(word)


banned_chars = ""
while True:
    guess = input("Enter guess: ")
    if not guess:
        guess = "." * num_letters
    required_chars = input("Enter required chars: ")
    banned_chars += input("Enter banned characters: ").strip()
    potential_words = trie.search(guess)
    valid_words = []
    for word in potential_words:
        valid = True
        for char in required_chars:
            if not char in word:
                valid = False
                break
        if not valid:
            continue
        for char in banned_chars:
            if char in word:
                valid = False
                break
        if valid:
            valid_words.append(word)
    print(valid_words)
