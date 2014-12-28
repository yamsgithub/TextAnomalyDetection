'''
Created on Apr 18, 2012

@author: meghana
'''
import os
from Article1 import Article1
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
                    temp = Article1()
                    temp.load(fp, articleName[0])
                    documents.append( temp )
                    print documents[documentIter]
                    documents[documentIter].process
                    print documents[documentIter].ngramsets
                   
                   
                    
                    documentIter = documentIter + 1