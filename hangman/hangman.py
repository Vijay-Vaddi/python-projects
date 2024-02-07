import random
words = ['Please', 'chose', 'your', 'move']

def get_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice[word]
    
    return word

def hangman():
    word = get_word(words)
    