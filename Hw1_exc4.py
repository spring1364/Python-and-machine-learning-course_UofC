# Author: Sara Ghandehari

def find_scrabble_score(word):
    """
    find_scrabble_score() for a score for the input word based on the dictionary of scores

    """
    dict_scores = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2,
                   'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1,
                   'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
                   'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
    upper_word = word.upper()
    score = 0
    for char in upper_word.strip():
        if char not in dict_scores.keys():
            return 'The entered word containes non alphabetic character'
        score += dict_scores[char]
    return score

# Author: Nikoo Sabzevar

points = {"1": ["A", "E", "I", "L", "N", "O", "R", "S", "T", "U"],
          "2": ["D", "G"],
          "3": ["B", "C", "M", "P"],
          "4": ["F", "H", "V", "W", "Y"],
          "5": ["K"],
          "8": ["J", "X"],
          "10": ["Q", "Z"]}


def find_scrabble_score0(word):
    upper_word = word.upper()
    score = 0
    all_chars = [x for v in points.values() for x in v]
    for char in upper_word.strip():
        if char not in all_chars:
            return 'The entered word contains non alphabetic character!'
        for key in points.keys():
            if char in points[key]:
                score += int(key)
    return score


word = "Programming"
print("The scrabble score of " + word + " is: " + str(find_scrabble_score(word)))
