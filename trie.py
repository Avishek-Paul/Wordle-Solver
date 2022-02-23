class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        curr_node.isEnd = True

    def search(self, word: str) -> bool:
        matching_words = []

        def dfs(node, s, curr_word):
            curr = node
            for idx, char in enumerate(s):
                if char == ".":
                    for letter, child in curr.children.items():
                        if dfs(child, s[idx + 1 :], curr_word + letter):
                            continue
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr_word += char
                    curr = curr.children[char]

            if curr.isEnd:
                matching_words.append(curr_word)
            return curr.isEnd

        dfs(self.root, word, "")
        return matching_words

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for char in prefix:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return True
