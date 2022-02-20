"""
Name: Jenny Tong
User ID: TPHU929
The Word class takes a string parameter of the word that the game player will guess. It takes in player's input (which is a letter) and
assess if the letter is in the word.
"""
class Word:
    def __init__(self,word_string):
        self.word_string=word_string.lower()
        self.already_guessed_letter=[]
        self.guessing_space='_ '*len(word_string)
    def already_guessed(self, letter):
        return letter in self.already_guessed_letter
    def update_current_status(self, letter):
        guessed_space=self.guessing_space.split()
        letter_list=[]
        for i in range(len(self.word_string)):
            if letter==self.word_string[i]:
                letter_list.append(i)
        for i in letter_list:
            guessed_space[i]=letter
        self.guessing_space=' '.join(guessed_space)
    def guess(self, letter):
        k=False
        if not letter in self.already_guessed_letter:
            self.already_guessed_letter.append(letter)
        if letter in self.word_string:
            k=True
        return k
    def guessed_correctly(self):
        return self.guessing_space.split()==list(self.word_string)
        
        
        









