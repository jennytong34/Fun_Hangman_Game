"""
Name: Jenny Tong
User ID: TPHU929
The Hangman.py code runs the game by coordinating the Dictionary_Reader class, the Word class and the Drawing class.
"""
from Dictionary_Reader import Dictionary_Reader
from Word import Word
from Drawing import Drawing
import random
def get_word(dict_reader,dict_file):
    word_list=dict_reader.get_valid_words(dict_file)
    if len(word_list)==0:
        print('No valid words available. The game will end.')
        return None
    else:
        index=random.randrange(len(word_list))
        word=Word(word_list[index])
        return word

def run_game(word):
    a_draw=Drawing()
    while a_draw.game_over()==False and '_' in word.guessing_space:
        letter=input('Please guess a letter: ').lower()
        while word.already_guessed(letter)==True:
            print('You have already used {} as a guess.'.format(letter))
            letter=input('Guess another letter: ').lower()
        if word.already_guessed(letter)==False:
            if word.guess(letter)==True:
                print('The word contains the letter: {}'.format(letter),'\n')
                word.update_current_status(letter)
                print('Word: {}'.format(word.guessing_space),'\n')
                print('Guessed letters:')
                print('',word.already_guessed_letter,'\n')
                print('Gallows:','\n')
                a_draw.draw()
                print()
            elif word.guess(letter)==False:
                a_draw.increment_phase()
                print('The word does not contain the letter: {}'.format(letter),'\n')
                print('Word: {}'.format(word.guessing_space),'\n')
                print('Guessed letters:')
                print('',word.already_guessed_letter,'\n')
                print('Gallows:','\n')
                a_draw.draw()
                print()
    if '_' not in word.guessing_space:
        return print('Congratulations! You have won!')
    else:
        return print('You have lost!')

def main():
    x='CS130 Assignment - Hangman'
    random.seed(30)
    print(x)
    print('='*len(x))
    print()
    dict_reader=Dictionary_Reader("123.txt",3, 4)
    dict_file=dict_reader.get_file_object()
    if dict_file!=None:
        word=get_word(dict_reader,dict_file)
        if word!=None:
            print('Word: {}'.format(word.guessing_space))
            print()
            run_game(word)

main()
