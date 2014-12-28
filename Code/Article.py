'''
Created on Apr 12, 2012

@author: Wil
'''

import nltk.data
import nltk.stem
import math
import string
import nltk.text
from numpy import *
import nltk.cluster

class Article:
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
        f = open(filePath + '/' + articleName + '.txt', 'r')
        self.rawData = f.read().split('\n')  
        #self.title = self.rawData.pop(0)
        self.rawData = ' '.join(self.rawData)
        self.process()
        self.process2()
    #''' 
    #original process function   
    def process2(self):
        self.sortedData = dict();
        self.numWords = 0
        
        #loop through all the raw data and combine it into a dictionary
        for a in self.stemmedData:
            if a not in self.sortedData:
                self.sortedData[a] = self.stemmedData.count(a)
                self.numWords = self.stemmedData.count(a) +self.numWords
                
        #self.sortedData is a dictionary (associative array) where ['word'] = numberOfWordOccurences
                
        self.sortedData2 = sorted(self.sortedData) #this is an alphabetical list of all the words in the document
    #'''
       
    def process(self):
        #set up tokenizer
        self.tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        
        #tokenize the data into sentences
        self.sentences = self.tokenizer.tokenize(self.rawData.strip())
        
        #set up stemmer
        self.stemmer = nltk.stem.LancasterStemmer() 
        #self.stemmer = nltk.stem.PorterStemmer()
        
        self.stemmedSentences = []
        
        for i in range(0, len(self.sentences)):
            
            
            t2 = self.sentences[i].split(' ')
            
            t2 = [w for w in t2 if not w in nltk.corpus.stopwords.words('english')]  #remove stopwords
            t2 = ' '.join(t2)
            t2 = t2.translate(string.maketrans("",""), string.punctuation)
            
            t2 = t2.split(' ')
            #eng_stopwords = nltk.corpus.stopwords.words('english')
            #t2 = [w for w in t2 if w not in string.punctuation and w.lower() not in eng_stopwords]
            
            for j in range(0, len(t2)):
                t2[j] = self.stemmer.stem(t2[j])
                
            self.stemmedSentences.append( ' '.join(t2))
            
        self.stemmedData = ' '.join(self.stemmedSentences).split(' ')
        
    '''
    returns the score (overlap) between two articles
    
    '''    
    def getScore(self, newArticle):
        
        mult = 1.7
        
        sharedKeys = self.sortedData.viewkeys() & newArticle.sortedData.viewkeys()
        
        if(len(sharedKeys) *mult > len(self.sortedData.viewkeys()) or len(sharedKeys) *mult> len(newArticle.sortedData.viewkeys())):
            return len(sharedKeys)*10
        
        return len(sharedKeys)
    
        '''
        score = 0
        
        for sk in sharedKeys:
            score = score + self.sortedData[sk]+newArticle.sortedData[sk]
            
        return score
        '''
        
    
    @staticmethod
    def scoreDocumentClusters(clusterA, clusterB, documents):
        score = []

        
        for i in range(0, len(clusterA)):
            for j in range(0, len(clusterB)):
                
                #print clusterA[i], ' | ', clusterB[j]
                
                score.append(documents[clusterA[i]].getScore(documents[clusterB[j]]))
               
                
        #print score, ' | ', len(score) 
        score = sum(score) / len(score)
        #score = max(score)
        
        return score
       
    @staticmethod
    def scoreDoc2Cluster(doc, clusterB, documents):
        '''
        score = 0
        
        keys = documents[doc].sortedData.viewkeys()
        
        for k in keys:
            
            tf = documents[doc].sortedData[k]# / documents[doc].numWords
            
            idf = 0
            for c in clusterB:
                
                if k in documents[c].sortedData:
                    idf = idf + 1
                
            print tf, ' ', idf, ' ', tf*idf    
            if idf != 0:
                idf = math.log(len(clusterB)/idf)
            
            score = score +tf*idf
        
        return score
        '''
        #'''
   
        #generate a list of all the words
        uKeys = documents[doc].sortedData.viewkeys() #start with the words in the new document
        
        for i in range(0, len(clusterB)):       #add all of the words from documents in the cluster to the list
            uKeys = uKeys | documents[clusterB[i]].sortedData.viewkeys()
        
        #v vector contains all of the word vectors for each document (both new document and documents in cluster)
        v = []
        
        
        new = []
        new.append(doc)
        [new.append(b) for b in clusterB]
        
        
        for d in new:
            temp = []
            for k in uKeys:
                if k in documents[d].sortedData:
                    temp.append(documents[d].sortedData[k])
                else:
                    temp.append(0)
            a = array(temp)
            v.append(a)
        
        score = []  
        for i in range(1, len(v)):
            score.append(nltk.cluster.cosine_distance(v[i], v[0]))
        
        return sum(score)/len(score)
        
        #'''
        '''
        txt = []
        
        for c in clusterB:
            temp = nltk.Text(documents[c].rawData)
            txt.append(temp)
        
        temp = nltk.Text(documents[doc].rawData)
        txt.append(temp)
            
        mytxt = nltk.text.TextCollection(txt)
        
        sum = 0
        for k in documents[doc].sortedData.viewkeys():
            sum = sum + mytxt.tf_idf(k, txt[-1])
            
        print sum
        return sum    
        '''
        
        
        
        