import logging
import uuid
from collections import defaultdict
import re


class filerw:
    def __init__(self, filenm):
        self.filenm = filenm
        self.filehd = None
        self.filedata = ""
        logging.info("Initialised values")

    # open file and read content of file
    def read(self):
        self.filehd = open(self.filenm, "r")
        self.filedata = self.filehd.read()
        self.filehd.close()
        self.filehd = None
        logging.info("Read data from input data file")
        return self.filedata

    # write content to file
    def write(self, data_written):
        self.filehd = open("output.txt", "a+")
        self.filehd.write(data_written)
        self.filehd.close()
        self.filehd = None
        logging.info("Written to file")
        return "Done"


class fileoper(filerw):
    '''def __init__(self, filenm):
        super().__init__(filenm)'''

    def get_inputdata(self):
        print(self.read())

    # get list of words from content of file
    def getwords(self):
        try:
            words = list(self.read().split())
            return words
        except Exception:
            logging.info("Error while getting data from inputfile")

    # count of words startswith 'to'
    def prefix_to(self, l):
        c = 0
        for wd in l:
            if wd.startswith("to"):
                c += 1
        logging.info("getting words with prefix to ")
        return c

    # count of words endswith 'ing'
    def postfix_ing(self, l):
        c = 0
        for wd in l:
            if wd.endswith("ing"):
                c += 1
        logging.info("getting words with postfix ing")
        return c

    # most repeated word from data
    def most_repeated(self, l):
        tmp = defaultdict(int)
        for wd in l:
            tmp[wd] += 1
        logging.info("getting Most repeated word")
        return str(max(tmp, key=tmp.get))

    # get palidromic words from list of words
    def find_palindrome(self, l):
        tmp = []
        for wd in l:
            if (wd == wd[::-1] and len(wd) > 1):
                tmp.append(wd)
        logging.info("Getting palidromic words")
        return tmp

    ''' split words based on vowels, capitalize 3rd letter of word and 5th word in list
        replce \n with ';' and write these content to unique file'''

    def uniqfileoper(self, list_data):
        try:
            l = []
            for i in range(len(list_data)):
                l.extend(re.split('a|e|i|o|u|A|E|I|O|U', list_data[i]))
            for i in range(len(l)):
                if len(l[i]) >= 3:
                    l[i].replace(l[i][2], l[i][2].upper(), 1)
                if (i + 1) % 5 == 0:
                    l[i] = l[i].upper()
                l[i] = l[i].replace('\n', ';')
            l = " ".join(l).split()
            uniq_flname = str(uuid.uuid4())
            uniq_flname += '.txt'
            with open(uniq_flname, 'x') as fl:
                fl.write("-".join(l))
            logging.info("writing data to uniquefile after required operation")
        except Exception:
            logging.error("Error while getting data from inputfile")


if __name__ == '__main__':
    '''creted logger file and display output'''
    logging.basicConfig(filename="logger.txt",
                        filemode="a",
                        format='%(asctime)s %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logging.info("Started execution")
    obj = fileoper("input.txt")
    l = obj.getwords()
    print(l)
    print("A.Number of words having prefix with 'To' :", obj.prefix_to(l))
    print("B.Number of words having ending with 'ing' :", obj.postfix_ing(l))
    print("C.Word that was repeated most of times is: ", obj.most_repeated(l))
    print("D.The palindrome present in the file are: ", " ".join(obj.find_palindrome(l)))
    print("E. Unique words: ", set(l))
    print("F. Word dict with key as counter index and value as the word: ", dict(enumerate(l)))
    obj.uniqfileoper(l)
