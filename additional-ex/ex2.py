# Exercise 2: from an exam paper.
    # Write you code in the file textanalysis.py to answer this question. Write a
    # function get_words_starting_with(text, letter) that returns the list of
    # words starting with letter in the string text. The result should not be case
    # sensitive, e.g. ’about’ should be returned if the letter ’a’ or ’A’ is given as
    # parameter. For simplicity, we assume for exercises 2,3, and 4 that the text does
    # not have any punctuations, and words are separated by at least one blank space.
    # For example, using the variable sample_text we should obtain:
        # >>> get_words_starting_with (sample_text, ’a’)
        # [’As’, ’a’, ’about’, ’adding’, ’a’, ’ago’, ’a’,
        # ’around’, ’Amsterdam’, ’a’, ’and’, ’an’, ’about’,
        # ’a’, ’ABC’, ’appeal’, ’as’, ’a’, ’a’, ’a’]
        # >>> get_words_starting_with(sample_text, ’z’)
        # []
    # Hint: You may want to use the method split() from the str type.

# Content from textanalysis.py:

sample_text = (" As Python s creator I d like to say a few words about its "+
              "origins adding a bit of personal philosophy "+
              "Over six years ago in December I was looking for a "+
              "hobby programming project that would keep me occupied "+
              "during the week around Christmas My office "+
              "a government run research lab in Amsterdam would be closed "+
              "but I had a home computer and not much else on my hands "+
              " I decided to write an interpreter for the new scripting "+
              "language  I had been thinking about lately a descendant of ABC "+
              "that would appeal to UnixC hackers I chose Python as a "+
              "working title for   the project being in a slightly irreverent "+
              "mood and a big fan of Monty Python s Flying Circus")

# Solution:

def get_words_starting_with(text:str, letter:str) -> list[str]:
    res = []
    for word in text.split():
        if word.lower().startswith(letter.lower()):
            res.append(word)
    return res

print(get_words_starting_with(sample_text, 'a'))