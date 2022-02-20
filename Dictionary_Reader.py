"""
Name: Jenny Tong
User ID: TPHU929
The Dictionary_Reader class takes a file name, two integers that specify the minimum and maximum word length. It reads the content
of the file and create a list of words from the file that meet the length requirement.
"""
class Dictionary_Reader:
    def __init__(self,file_name,min_word_length,max_word_length):
        self.file_name=file_name
        if min_word_length<5:
            print('The minimum word length should be 5 or more characters!'+'\n'+'It has been set to 5.',sep='')
            self.min_word_length=5
            if max_word_length<self.min_word_length:
                print('The maximum word length should be greater than or equal to the minumum word length!'+'\n'+'The maximum word length has been set to {}'.format(self.min_word_length),sep='')
                self.max_word_length=self.min_word_length
            else:
                self.max_word_length=max_word_length
        else:
            self.min_word_length=min_word_length
            if max_word_length<self.min_word_length:
                print('The maximum word length should be greater than or equal to the minumum word length!'+'\n'+'The maximum word length has been set to {}'.format(self.min_word_length),sep='')
                self.max_word_length=self.min_word_length
            else:
                self.max_word_length=max_word_length  
    def get_file_object(self):
        while self.file_name!='Q':
            try:
                self.input_file=open(self.file_name)
                return self.input_file
            except FileNotFoundError:
                print('{} cannot be found.'.format(self.file_name))
                self.file_name=input('Please enter a valid file name or Q to quit: ')
        if self.file_name=='Q':
            return None
    def get_valid_words(self, words_file):
        self.words_file=words_file
        self.words_list=[]
        if words_file==None:
            return []
        else:
            words=self.words_file.read().split()
            for word in words:
                if len(word) in range(self.min_word_length,self.max_word_length+1):
                    self.words_list.append(word)
            return self.words_list





