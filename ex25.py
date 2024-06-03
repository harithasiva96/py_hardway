def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Print the first word after popping it off."""
    word = words.pop(0)

def print_last_word(words):
    """Print the first word after popping it off."""
    word = words.pop(-1)

def sort_sentence(sentence):
    """Take in afull sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Print the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorets the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# Take terminal and import this file . Perform the operations given below.

# python3
# import ex25.py
# sentence = ex25.break_words(sentence)
# words 
# sorted_words = ex25.sort_words(words)
# sorted_words
# ex25.print_first_word(words)
# ex25.print_last_word(words)
# words 
# ex25.print_first_word(sorted_words)
# sorted_words
# sorted_words = ex25.sort_sentence(sentence)
# sorted_words
# ex25.print_first_and_last(sentence)
# sorted_words
# ex25.print_first_and_last_sorted(sentence)

