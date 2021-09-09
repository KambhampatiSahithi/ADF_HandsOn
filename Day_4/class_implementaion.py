"""module for usage of class concept for task along with testing"""
import logging
import uuid
from collections import defaultdict
import re


class FileReadWrite:
    ''' class for reading writing operations '''

    def __init__(self, filename):
        self.filename = filename
        self.filehd = None
        self.filedata = ""
        logging.info("Initialised values")

    def read_data(self):
        ''' open and read file '''
        try:
            logging.info("Trying to open and read file")
            with open(self.filename, encoding="UTF-8") as filehandle:
                data = filehandle.readlines()
        except IOError:
            logging.error("Failed to read or open file")
        return "".join(data)
    @staticmethod
    def write_data(data_written):
        ''' write data to the file '''
        try:
            with open("output.txt", "x", encoding="UTF-8") as filehandle:
                filehandle.write(data_written)
        except OSError:
            logging.info("Unexpected error")
        return "Done"

class FileOperations(FileReadWrite):
    '''class perform different methods (Inhetited)'''
    def get_inputdata(self):
        ''' get input data from input textfile'''
        print(self.read_data())

    def getwords(self):
        '''get list of words from content of file'''
        try:
            words = list(self.read_data().split())
        except IOError:
            logging.info("Error while getting data from inputfile")
        return words
    @staticmethod
    def prefix_to(list_words):
        ''' count of words startswith 'to' '''
        count = 0
        for word in list_words:
            if word.startswith("to"):
                count += 1
        logging.info("getting words with prefix to ")
        return count



    @staticmethod
    def postfix_ing(list_words):
        ''' count of words endswith 'ing' '''
        count = 0
        for word in list_words:
            if word.endswith("ing"):
                count += 1
        logging.info("getting words with postfix ing")
        return count



    @staticmethod
    def most_repeated(list_words):
        ''' most repeated word from data '''
        tmp = defaultdict(int)
        for word in list_words:
            tmp[word] += 1
        logging.info("getting Most repeated word")
        return str(max(tmp, key=tmp.get))

    # get palindromic words from list of words

    @staticmethod
    def find_palindrome(list_words):
        ''' palindromic words from list of words '''
        tmp = []
        for word in list_words:
            if word == word[::-1] and len(word) > 1:
                tmp.append(word)
        logging.info("Getting palidromic words")
        return tmp



    @staticmethod
    def uniqfileoper(list_data):
        ''' store data into unique file after operations performed
         split words based on vowels, capitalize 3rd letter of word and 5th word in list
        replce \n with ';' and write these content to unique file'''


        try:
            list_word = []
            length = len(list_data)
            for i in range(length):
                list_word.extend(re.split('[aeiouAEIOU]', list_data[i]))
            for i in range(length):
                if len(list_word[i]) >= 3:
                    list_word[i].replace(list_word[i][2], list_word[i][2].upper(), 1)
                if (i + 1) % 5 == 0:
                    list_word[i] = list_word[i].upper()
                list_word[i] = list_word[i].replace('\n', ';')
            list_word = " ".join(list_word).split()
            uniq_flname = str(uuid.uuid4())
            uniq_flname += '.txt'
            with open(uniq_flname, 'x', encoding="UTF-8") as filehandle:
                filehandle.write("-".join(list_word))
            logging.info("writing data to uniquefile after required operation")
        except IOError:
            logging.error("Error while getting data from inputfile")
        return "-".join(list_word)
    @staticmethod
    def index_key(list_words):
        ''' index as key and words as value'''
        dictionary = {}
        count = 0
        for i in list_words:
            dictionary[count] = i
            count += 1
        return dictionary

if __name__ == '__main__':
    logging.basicConfig(filename="logger.txt",
                        filemode="a",
                        format='%(asctime)s %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logging.info("Started execution")
    obj = FileOperations("input.txt")
    list_words = obj.getwords()
    print(list_words)
    print("A.Number of words having prefix with 'To' :", obj.prefix_to(list_words))
    print("B.Number of words having ending with 'ing' :", obj.postfix_ing(list_words))
    print("C.Word that was repeated most of times is: ", obj.most_repeated(list_words))
    print("D.The palindrome present in the file are: ", " ".join(obj.find_palindrome(list_words)))
    print("E. Unique words: ", set(list_words))
    print('F. Word dict with key as counter' \
          'index and value as the word: ', obj.index_key(list_words))
    obj.uniqfileoper(list_words)
