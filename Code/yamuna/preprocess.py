import sys

sys.path.append('/usr/local/lib/python2.7/site-packages/')

import nltk.data
import nltk.stem
from nltk import corpus

class TextPreprocess:
    def __init__(self,display=False):
        self.display=display
        
    def preprocess(self,text):
        text = nltk.word_tokenize(text)
        if self.display:
            print "After Tokenizing"
            print text
            print "\n\n"

        text=[w.lower() for w in text]
        if self.display:
            print "Convert to lower case"
            print text
            print "\n\n"

        text=[w for w in text if not w in corpus.stopwords.words('english')]
        if self.display:
            print "After removing stop words"
            print text
            print "\n\n"

        stemmer=nltk.stem.PorterStemmer()
        text=[stemmer.stem(w) for w in text]
        if self.display:
            print "After stemming"
            print text
            print "\n\n"
        
        text=[w for w in text if len(w)>2]
        if self.display:
            print "After filtering very small words"
            print text
            
        return text
