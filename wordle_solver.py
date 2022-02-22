from trie import Trie

word_dict = open("cleaned_word_list.txt").readlines()
trie = Trie()

for word in word_dict:
    word = word.strip()
    trie.insert(word)


banned_chars = ""
while True:
    guess = input("Enter guess: ")
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
