class Letter:
    def __init__(self, letter):
        self.letter = letter
        self.available = True

    def __repr__(self):
        return self.letter

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def adjacent(self, board_size):
        result = []
        for x_change in [-1, 0, 1]:
            new_x = self.x + x_change
            for y_change in [-1, 0, 1]:
                new_y = self.y + y_change
                adjacent_position = Position(new_x, new_y)
                if adjacent_position.is_onboard(board_size) and (new_x != self.x or new_y != self.y):
                    result.append(adjacent_position)
        return result

    def is_onboard(self, board_size):
        my_x = self.x
        my_y = self.y
        if my_x >= 0 and my_x < board_size and my_y >= 0 and my_y < board_size:
            return True
        else:
            return False

    def __repr__(self):
        return f"({self.x}, {self.y})"

#def turn_letters_into_words(letters_so_far):
#    word = ""
#    for letter in letters_so_far:
#        char = "".join(letter)
#        word += char
#    if len(word) >= 4:
#        words_so_far.append(word.lower())

def possible_words(dictionary, sq, position, letters_so_far = ""):
    debug=False
    if "hibernate".startswith(letters_so_far.lower()):
        debug=True
    current_letter = sq[position.x][position.y]
    if current_letter.available == False:
        if debug:
            print(f"REJECTED {position}")
        return []
    candidates = []
    current_word = (letters_so_far + current_letter.letter).lower()
    if len(current_word) >= 4 and current_word in dictionary:
        candidates.append(current_word)
    current_letter.available = False
    possible_directions = position.adjacent(len(sq))
    for next_position in possible_directions:
        if debug:
            print(current_word)
            print(f"going from {position} to {next_position}")
        candidates.extend(possible_words(dictionary, sq, next_position, current_word))
    current_letter.available = True
    return candidates

def main():
    dictionary = open("NASPA-Dictionary.txt", "r")
    dicts = dictionary.readlines()
    the_dictionary_to_rule_them_all = []
    for line in dicts:
        word = line.strip()
        if len(word) >= 4:
            the_dictionary_to_rule_them_all.append(line.strip())

    sq = [[Letter('H'), Letter('I'), Letter('B')],
          [Letter('N'), Letter('R'), Letter('E')],
          [Letter('A'), Letter('T'), Letter('E')]]
    board_size = len(sq)

    starting_point = Position(0, 0)
    #adjacent_points = starting_point.adjacent(board_size)
    #print(adjacent_points)
    #print(the_dictionary_to_rule_them_all)
    print(possible_words(the_dictionary_to_rule_them_all, sq, starting_point))


if __name__ == "__main__":
    main()