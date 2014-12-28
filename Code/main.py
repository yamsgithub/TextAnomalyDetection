import os
from Article import Article
import numpy

documents = []
documentIter = 0


'''
read in files from the Data directory (up one level)
os.walk returns the top directory, sub directories and files
'''
for top, sub, files in os.walk('..\Data\\'):
    #loop through all the sub directories in the data folder
    for s in sub:
        #get all the files within the current subdirectory
        for t, ss, fil in os.walk( os.path.join(top, s)):
            #loop through each file in the subdir
            for f in fil:
                #for each file, split the path by directory, the fulle file path is now an aray [directory, subdirectory, filename.extension]
                filePath = os.path.join(t, f).split('\\')

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

                    
                    #print documents[documentIter].sortedData2
                    
                    documentIter = documentIter + 1
                    

print '======'

#create a numpy array (similar to arrays in matlab)


clusters = []
activeClusters = []

for i in range(0, len(documents)):
    clusters.append(i)
    clusters[i] = []
    clusters[i].append(i)
    activeClusters.append(i)

    
#calculate simularity matrix

for i in range(0,9):
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
                
                simu[i][j] = Article.scoreDocumentClusters(clusters[activeClusters[i]], clusters[activeClusters[j]], documents)
                if simu[i][j] > maxVal:
                    maxVal = simu[i][j]
                    iIndex = activeClusters[i]
                    jIndex = activeClusters[j]   
                
    #print simu  
    #print maxVal
    
    newDocument = Article()
    newDocument.rawData = documents[iIndex].rawData + documents[jIndex].rawData
    newDocument.process()
    
    #newDocument.sortedData
    
    documents.append(newDocument)
    clusters.append(clusters[iIndex] + clusters[jIndex])
    
    
    activeClusters.remove(iIndex)
    activeClusters.remove(jIndex)
    activeClusters.append(len(clusters)-1) 
    
    print clusters
    #print activeClusters
    #print simu.max()
    #print simu[iIndex][jIndex]
    
    #print documents[iIndex].articleName
    #print documents[jIndex].articleName
#'''
print 'first cluster:'

for q in clusters[-1]:
    print documents[q].articleName
 
print '\n second cluster:' 
    
for q in clusters[-2]:
    print documents[q].articleName
    
print simu


print documents[1].sortedData
#'''
