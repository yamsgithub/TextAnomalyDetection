import sys

#sys.path.append('/usr/local/lib/python2.7/site-packages/')
#sys.path.append('/home/yamuna/Downloads/epd-7.2-2-rh5-x86_64/lib/python2.7/site-packages')

import nltk.cluster

from sets import Set
from TextRank import TextRank
from Compare import Compare
from nltk.text import TextCollection
from preprocess import TextPreprocess

file1='test1.txt'
file2='test2.txt'

tr=TextRank()

doc1_gr=tr.process(file1)
doc2_gr=tr.process(file2)

doc1=tr.graph_to_txt(doc1_gr)
doc2=tr.graph_to_txt(doc2_gr)

# tr.draw_graph(doc1_gr,file1+'.png')
# tr.draw_graph(doc2_gr,file2+'.png')

c=Compare()

novel=c.execute(doc1,doc2)

orig_fn=file2
orig_f=open(orig_fn,'r')
orig_lines=orig_f.readlines()
orig_f.close()

sentences=Set()

index=0
for in_node in novel:
    i=0;
    words=((in_node.split('('))[1].split(')'))[0].split(',')
    while (len(orig_lines) > 0) & (i<len(orig_lines)) & (len(words)==2):
        if (len(words[0]) > 2) & (len(words[1]) > 2):
            s_parts = orig_lines[i].split(words[0])
            if (len(s_parts) == 2):
                if s_parts[1].find(words[1]) >= 0:
                    print words
                    print orig_lines[i]
                    sentences.add(i);
                    break
        i=i+1
    index=index+1

differences=[orig_lines[int(i)] for i in sentences]
out_fn='different_sentences.txt'
out_f=open(out_fn,'w')
[out_f.write(line+'\n') for line in differences]
out_f.close()

orig_fn=file1
orig_f=open(orig_fn,'r')
orig_lines=orig_f.readlines()
orig_f.close()

filtered_diff=[]
tp=TextPreprocess()
for i in range(0,len(differences)):
    line=differences[i]
    td=tp.preprocess(line.strip())
    found=0
    for orig_line in orig_lines:
        to=tp.preprocess(orig_line.strip())
        terms=Set(td)
        [terms.add(term) for term in to]
        tc=TextCollection([td, to])
        vd=[tc.tf(term,td) for term in terms]
        vo=[tc.tf(term,to) for term in terms]
        if (sum(vd) != 0) & (sum(vo)!=0):
            cs=nltk.cluster.cosine_distance(vd,vo)
            if cs > 0.5:
                found=1
                break
    if found==0:
        filtered_diff.append(differences[i])
            
out_fn='output.txt'
out_f=open(out_fn,'w')
[out_f.write(line+'\n') for line in filtered_diff]
out_f.close()
