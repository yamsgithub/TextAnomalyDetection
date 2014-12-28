
import nltk.data

import nltk.stem

sD = nltk.data.load('tokenizers/punkt/english.pickle')

f= open('../Data/Malkin Scoring Title/malkin_sews_up_art_ross.txt')

rawString = f.read()

rawString = rawString.split('\n')

title = rawString.pop(0)


rawString = ' '.join(rawString)

toks = sD.tokenize(rawString.strip())

#print '\n'.join(toks)

#st = nltk.stem.PorterStemmer()
st = nltk.stem.LancasterStemmer()
for i in range(0, len(toks)):
    t2 = toks[i].split(' ')
    
    t2 = [w for w in t2 if not w in nltk.corpus.stopwords.words('english')]  #remove stopwords


    
    for j in range(0, len(t2)):
        t2[j] = st.stem(t2[j])
        
    toks[i] = ' '.join(t2)
    
#print '\n'.join(toks)
print rawString

    
    
    
