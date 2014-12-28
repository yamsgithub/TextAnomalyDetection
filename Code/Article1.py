'''
Created on Apr 18, 2012

@author: meghana
'''
class Article1:
    '''
    classdocs
    '''

    def __init__(self):
        self.articleName = ''

    def load(self, filePath, articleName):
        '''
        Constructor
        '''
        self.articleName = articleName
        #read in the file (combine filepath, articlename and the .pt extension
        f = open(filePath + '/' + articleName + '.ng', 'r')
        self.rawData = f.read().split(' ')  #f.read() returns a string, split(' ') breaks the string into an array
        # self.rawData is an array of all the stemmed words from the input files
        self.process()
        
        
    def process(self):
        self.rawdata = dict()

        self.ngramsets = []

        numNGs = 5
        for i in range(0, len(rawData) / numNGs):               #for each set of ngrams
            temp = []
        for j in range(0, numNGs):                      #for each ngram in set
            temp.append(self.rawData.pop(0))     #self.rawData.popleft() removes leftmost item in array, adds it to temp array

            self.ngramsets.append(temp[j])
        
        