
import nltk.data
import nltk.stem
import string

#original text
#text = "The quick brown fox jumps over the lazy dog."

text = "Shoppers began- lining up to purchase Apple Inc.'s third-generation iPad on Friday, as the technology giant tries to widen its lead in the fast-growing tablet market. Crowds were expected at Apple retail stores from Australia to Switzerland to become one of the first to buy the new iPad.  The new tablet computer, priced starting at $499 in the U.S., has a higher-resolution screen and faster networking capabilities than its predecessor, which has dominated the market to date."

print "Original Text: \n", text, '\n'

if(len(text.split('.'))>1):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')  #used if more than one sentence
    
    sentences = tokenizer.tokenize(text.strip())
    
    print 'Tokenized by Sentences: \n[', ']['.join(sentences), ']\n'
    
    stemmedSentences = []
    stoppedSentences = []
    for i in range(0, len(sentences)):
        
        
        t2 = sentences[i].split(' ')
        
        t2 = [w for w in t2 if not w in nltk.corpus.stopwords.words('english')]  #remove stopwords
        t2 = ' '.join(t2)
        t2 = t2.translate(string.maketrans("",""), string.punctuation)
        
        stoppedSentences.append(t2)
        t2 = t2.split(' ')
        #eng_stopwords = nltk.corpus.stopwords.words('english')
        #t2 = [w for w in t2 if w not in string.punctuation and w.lower() not in eng_stopwords]
        stemmer = nltk.stem.LancasterStemmer()
        
        for j in range(0, len(t2)):
            t2[j] = stemmer.stem(t2[j])
            
        stemmedSentences.append( ' '.join(t2))
        
    print 'Stopwords and punctuation removed: \n[', '] ['.join(stoppedSentences), ']\n'
    print 'Stemmed: \n[', '] ['.join(stemmedSentences), ']\n'
else:

    #tokenize text
    
    
    tokens = text.split(' ') #split the text into tokens
    
    print 'Tokenized Text: \n[', ']['.join(tokens), ']\n'
    
    t2 = [w for w in tokens if not w in nltk.corpus.stopwords.words('english')]  #remove stopwords
    t2 = ' '.join(t2)
    t2 = t2.translate(string.maketrans("",""), string.punctuation)
    
    print 'Stopwords and punctuation removed: \n', t2, '\n'
    
    t2 = t2.split(' ')
    stemmer = nltk.stem.LancasterStemmer()
    stemmed = []
    for t in t2:
        stemmed.append(stemmer.stem(t))
        
    print 'Stemmed: \n', ' '.join(stemmed)