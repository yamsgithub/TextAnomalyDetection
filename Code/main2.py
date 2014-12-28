import os
from Article import Article
#from Topic import Topic
#import numpy

documents = []


'''
read in files from the Data directory (up one level)
os.walk returns the top directory, sub directories and files
'''
for top, sub, files in os.walk('..\Data2\\'):
    #loop through all the sub directories in the data folder
    '''
    for s in sub:
        #get all the files within the current subdirectory
        for t, ss, fil in os.walk( os.path.join(top, s)):
            #loop through each file in the subdir
            '''
    for f in files:
        #for each file, split the path by directory, the fulle file path is now an aray [directory, subdirectory, filename.extension]
        filePath = os.path.join(top, f).split('\\')

        #get the file name and split it from the extension
        #this is now an array [filename, extension]
        #the filename is also removed from the filePath array
        articleName = filePath.pop().split('.')
        
        #only work for the txt files, 
        if articleName[-1] == 'txt':
            
            fp = '/'.join(filePath) #recombine the 
            
            #create a new article and adds it to the documents array
            temp = Article()
            temp.load(fp, articleName[0])
            documents.append( temp )

                

print '======'

clusters = []

thresh = .3

for i in range(0,len(documents)):
    

    score = []
    maxS = 0
    inJ = -1;
    
    #loop through all existing clusters, and compare current document to it
    for j in range(0, len(clusters)):
        #score = Article.scoreDocumentClusters([i], clusters[j], documents)
        score = Article.scoreDoc2Cluster(i, clusters[j], documents)
        #print score
        if score > maxS:
            maxS = score
            inJ = j
            
    #print maxS
            
    if maxS > thresh:
        clusters[inJ].append(i)
        
    else:
        clusters.append([i])
    #print clusters
     
print clusters
        
      
for i in range(0, len(clusters)):
    for j in clusters[i]:
        print documents[j].articleName
    print ''

'''    
topics = []    

for c in clusters:
    topics.append(Topic(c, documents))
    
topics[0].clusterSentences()

print topics[0].clusters
'''


#print '\n'.join(topics[0].sentences)