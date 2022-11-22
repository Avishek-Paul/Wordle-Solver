from trie import Trie


class WordleSolver:
    def __init__(self, word_list, num_letters=5) -> None:
        self.trie = Trie()
        self.num_letters = num_letters
        for word in word_list:
            word = word.strip()
            if len(word) == num_letters:
                self.trie.insert(word)
        self.reset()

    def reset(self):
        self.banned_chars = set()
        self.required_chars = set()
        self.guess = self.set_guess()

    def get_options(self):
        if not self.guess:
            self.set_guess()
        potential_words = self.trie.search("".join(self.guess))
        valid_words = []
        for word in potential_words:
            if not all(char in word for char in self.required_chars):
                continue
            if any(char in self.banned_chars for char in word):
                continue
            valid_words.append(word)
        return valid_words

    def set_guess(self, guess=[]):
        if len(guess) == self.num_letters:
            self.guess = guess
        else:
            self.guess = guess + ["."] * (self.num_letters - len(guess))

    def add_required_char(self, char):
        self.required_chars.add(char)

    def remove_required_char(self, char):
        if char in self.required_chars:
            self.required_chars.remove(char)

    def add_banned_char(self, char):
        if char not in self.required_chars or char not in self.guess:
            self.banned_chars.add(char)

    def remove_banned_char(self, char):
        if char in self.banned_chars:
            self.banned_chars.remove(char)


# word_list = open("word_list.txt").readlines()
# solver = WordleSolver(word_list=word_list, num_letters=5)
# solver.guess = ".a..."
# solver.required_chars.add("t")
# solver.required_chars.add("p")
# solver.required_chars.add("r")
# solver.banned_chars.add("e")
# print(solver.get_options())
