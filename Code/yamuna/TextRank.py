import sys

sys.path.append('/usr/local/lib/python2.7/site-packages/')

import nltk
import itertools
from operator import itemgetter

from pygraph.classes.digraph import digraph
from pygraph.algorithms.pagerank import pagerank
from pygraph.classes.exceptions import AdditionError
import pygraphviz as pgv
    
class TextRank:

    def filter_for_tags(self,tagged, tags=['NN','NNS', 'JJ', 'NNP','VBD','VB','VBZ','VBN','CD']):
        return [item for item in tagged if item[1] in tags]


    def normalize(self,tagged):
        return [(item[0].replace('.', ''), item[1]) for item in tagged]


    def unique_everseen(self,iterable, key=None):
        "List unique elements, preserving order. Remember all elements ever seen."
        # unique_everseen('AAAABBBCCDAABBB') --> A B C D
        # unique_everseen('ABBCcAD', str.lower) --> A B C D
        seen = set()
        seen_add = seen.add
        if key is None:
            for element in itertools.ifilterfalse(seen.__contains__, iterable):
                seen_add(element)
                yield element
        else:
            for element in iterable:
                k = key(element)
                if k not in seen:
                    seen_add(k)
                    yield element

    def process(self,filename):

        in_f=open(filename,'r')
        lines=in_f.readlines();
    
        #text='"""';
        text=''
        for line in lines:
            text=text+line
        
        #text=text+'"""';
        
        text = nltk.word_tokenize(text)
    
        tagged = nltk.pos_tag(text)
        print tagged
        tagged = self.filter_for_tags(tagged)
        
        tagged = self.normalize(tagged)
        
        unique_word_set = self.unique_everseen([x[0] for x in tagged])
        
        gr = digraph()
        gr.add_nodes(list(unique_word_set))
    
        window_start = 0
        window_end = 2
        
        while 1:

            window_words = tagged[window_start:window_end]
            if len(window_words) == 2:
                #print window_words
                try:
                    gr.add_edge((window_words[0][0], window_words[1][0]))
                except AdditionError, e:
                    print 'already added %s, %s' % ((window_words[0][0], window_words[1][0]))
            else:
                break

            window_start += 1
            window_end += 1

        # calculated_page_rank = pagerank(gr)

        # di = sorted(calculated_page_rank.iteritems(), key=itemgetter(1),reverse=True)
        # for k, g in itertools.groupby(di, key=itemgetter(1)):
        #     print k, map(itemgetter(0), g)
        
        in_f.close()
        return gr

    def graph_to_txt(self,gr):
        groups=[]
        for node in gr.nodes():
            neighbors=gr.neighbors(node);
            for neighbor in neighbors:
                edge = '(' + node + ',' + neighbor + ')';
                groups.append(edge);

        return groups

    def draw_graph(self,gr,filename):
        pgr = pgv.AGraph(bgcolor='white')
        for node in gr.nodes():
            neighbors=gr.neighbors(node);
            for neighbor in neighbors:
                pgr.add_edge((node,neighbor))
                
        pgr.layout(prog='dot')
        pgr.draw(filename)

    

