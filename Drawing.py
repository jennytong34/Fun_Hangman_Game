"""
Name: Jenny Tong
User ID: TPHU929
The Drawing class handles the printing of the gallows in each phase of the game.
"""
class Drawing:
    def __init__(self):
        self.phase=0
        self.max_phase=8
        self.gallows=['' , '-'*6 , ('|'+'\n')*4+'-'*6 , '-'*5+'\n'+('|'+'\n')*4+'-'*6 , '-'*5+'\n'+'|   |'+'\n'+('|'+'\n')*3+'-'*6 , '-'*5+'\n'+'|   |'+'\n'+'|   O'+'\n'+('|'+'\n')*2+'-'*6 , '-'*5+'\n'+'|   |'+'\n'+'|   O'+'\n'+'|  ---'+'\n'+('|'+'\n')*1+'-'*6 , '-'*5+'\n'+'|   |'+'\n'+'|   O'+'\n'+'|  ---'+'\n'+'|  / \\'+'\n'+'-'*6]
    def increment_phase(self):
        if self.phase<self.max_phase-1:
            self.phase+=1
    def draw(self):
        print(self.gallows[self.phase])
    def game_over(self):
        return self.phase==self.max_phase-1

