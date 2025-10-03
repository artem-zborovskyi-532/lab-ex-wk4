# Exercise 3: from an exam paper.
    # As you can see in question 2, there are many repetitions of the word ’a’ in the list.
    # Improve your solution so no repetition of the same word occurs in the list.
        # >>> get_words_starting_with(sample_text, ’a’)
        # [’As’, ’a’, ’about’, ’adding’, ’ago’, ’around’,
        # ’Amsterdam’, ’and’, ’an’, ’ABC’, ’appeal’, ’as’]

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

def get_unique_words_starting_with(text:str, letter:str) -> list[str]:
    res = []
    for word in text.split():
        if word.lower().startswith(letter.lower()) and res.count(word) == 0:
            res.append(word)
    return res

print(get_unique_words_starting_with(sample_text, 'a'))