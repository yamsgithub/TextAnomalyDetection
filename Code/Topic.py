'''
Created on Apr 22, 2012

@author: Wil
'''

import numpy

class Topic:
    
    
    def __init__(self, cluster, documents):
        self.documents = []
        self.sentences = []
        self.sd = []
        documentIter = 0
        
        for c in cluster:
            self.documents.append(documents[c])
            
            sentenceIter = 0
            for s in self.documents[documentIter].stemmedSentences:
                self.sentences.append(s)
                self.sd.append((documentIter, sentenceIter))
                sentenceIter = sentenceIter + 1
            
            documentIter = documentIter + 1
                
            
    def clusterSentences(self):
        
        clusters = []
        activeClusters = []
        
        for i in range(0, len(self.sentences)):
            clusters.append(i)
            clusters[i] = []
            clusters[i].append(i)
            activeClusters.append(i)
        
            
        #calculate simularity matrix
        
        for x in range(0,len(self.documents)):
            simu = numpy.zeros((len(activeClusters), len(activeClusters)))
            maxVal = 0
            iIndex = -1;
            jIndex = -1;
            for i in range(0, len(activeClusters)):
                for j in range(0, len(activeClusters)):
                    if i != j: 
                        #simu[i][j] = documents[i].getScore(documents[j])
                        #simu[i][j] = documents[activeClusters[i]].getScore(documents[activeClusters[j]])
                        #print clusters[activeClusters[i]], ' : ', clusters[activeClusters[j]]
                        
                        simu[i][j] = self.scoreSentence(self.sentences[activeClusters[i]],self.sentences[activeClusters[j]])
                        if simu[i][j] > maxVal:
                            maxVal = simu[i][j]
                            iIndex = activeClusters[i]
                            jIndex = activeClusters[j]   
                                  

        
            clusters.append(clusters[iIndex] + clusters[jIndex])
            
            
            activeClusters.remove(iIndex)
            activeClusters.remove(jIndex)
            activeClusters.append(len(clusters)-1) 
            
            self.clusters = clusters
            self.aClusters = activeClusters
            
    def scoreSentence(self, sentenceA, sentenceB):
        sentenceA = set(sentenceA.split(' '))
        sentenceB = set(sentenceB.split(' '))
        
        return len(sentenceA & sentenceB)