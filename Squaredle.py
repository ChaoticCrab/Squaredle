# read letter-grid from png
# -> datastructure to represent the grid
# sq = [[('I', True), ('F', True)],
#       [('N', True), ('D', True)]]

sq = [[('H', True), ('I', True), ('B', True)],
       [('N', True), ('R', True), ('E', True)],
       [('A', True), ('T', True), ('E', True)]]

# cut picture
# recognize letter
# generate crid/table

# get a dictionary and break it down in letter-sections
# North American Scrabble Players word list (NWL 2020)
# time-check: entire dictionary vs letter-sectioned-dictionary

# pathfinding/word checking in the grid
# 8 possible diretions from letter
# recursion!!!
# recursive function that prints every possible word-combination

def on_board(coordinates):
    number_of_rows = len(sq)
    number_of_columns = len(sq[0])
    return coordinates[0] in range(number_of_rows) and coordinates[1] in range(number_of_columns)
def valid_step(position, coordinates):
    row_step_length = abs(coordinates[0] - position[0])
    column_step_length = abs(coordinates[1] - position[1])
    step = (row_step_length, column_step_length)
    return on_board(coordinates) and step[0] <= 1 and step[1] <= 1

# word_List["fi","if"]
def find_words(position, letters_so_far):
    turn_letters_into_words(letters_so_far)
    for row_number, row in enumerate(sq):
        # row_number = 0 / row = [('I',True),('F',True)]
        for column_number, letter in enumerate(row):
            # column_number = 0, letter = ('I',True)
            coordinates = (row_number, column_number)
            if not letter[1] or not valid_step(position, coordinates):
                continue
            new_letter = (letter[0], False)
            row[column_number] = new_letter
            letters_so_far.append(letter[0])
            find_words(coordinates, letters_so_far)
            row[column_number] = letter
            letters_so_far.pop()

letters_so_far = []
words_so_far = []
#print(words_so_far)
def turn_letters_into_words(letters_so_far):
    word = ""
    for letter in letters_so_far:
        char = "".join(letter)
        word += char
    if len(word) >= 4:
        words_so_far.append(word.lower())

# turn_letters_into_words(['f','o','x',"y"])

find_words((0, 0), letters_so_far)

dictionary = open("NASPA-Dictionary.txt","r")
dicts = dictionary.readlines()
the_dictionary_to_rule_them_all = []
for line in dicts:
    word = line.strip()
    if len(word) >= 4:
        the_dictionary_to_rule_them_all.append(line.strip())

class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def make_trie(*dictionary):
        root = dict()
        for word in dictionary:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[end_symbol] = end_symbol
        return root

    def add_to_trie(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def find_valid_words(self, words_so_far):
        valid_words = set()
        for i in range(len(words_so_far)):
            level = self.root
            for j in range(i, len(words_so_far)):
                ch = words_so_far[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    valid_words.add(words_so_far[i : j + 1])
        return valid_words

    def exists_in_trie(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return self.end_symbol in current

test = Trie()
for word in the_dictionary_to_rule_them_all:
   test.add_to_trie(word)

def valid_word(words_so_far):
   finds = []
   for word in words_so_far:
       if test.exists_in_trie(word) == True:
           finds.append(word)
   return finds

print(valid_word(words_so_far))
