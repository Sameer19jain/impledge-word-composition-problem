import time

class Word:
    def __init__(self):
        self.children = {}
        self.end_word = False

class WordStructure:
    def __init__(self):
        self.root = Word()

    

    def suffixes(self, word):
        indices = []
        node = self.root
        for i, char in enumerate(word):
            if char in node.children:
                node = node.children[char]
                if node.end_word:
                    indices.append(i + 1)
            else:
                break
        return indices
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Word()
            node = node.children[char]
        node.end_word = True

def longest_word(file_name):
    word_structure = WordStructure()  
    queue = []
    compound_words = set()

    start_time = time.time()

    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                suffix_indices = word_structure.suffixes(word)  
                for i in suffix_indices:
                    if i >= len(word):
                        break
                    queue.append((word, word[i:]))

                word_structure.insert(word)  

    longest = ''
    sec_longest = ''
    max_length = 0

    while queue:
        word, remaining_suffix = queue.pop(0)
        suffix_indices = word_structure.suffixes(remaining_suffix)  

        if not suffix_indices:
            continue

        for i in suffix_indices:
            if i > len(remaining_suffix):
                break
            if i == len(remaining_suffix):
                if len(word) > max_length:
                    sec_longest = longest
                    longest = word
                    max_length = len(word)
                compound_words.add(word)
            else:
                queue.append((word, remaining_suffix[i:]))

    end_time = time.time()
    processing_time = ((end_time - start_time) *1000 )

    return (longest, sec_longest, processing_time)

file_name = "Input_01.txt"  
longest, sec_longest, processing_time = longest_word(file_name)

print("Longest Compound Word:", longest)
print("Second Longest Compound Word:", sec_longest)
print("Time taken to process input file:", processing_time, "milliseconds")
