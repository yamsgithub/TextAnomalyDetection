# in1_fn='update_graph.txt'
# in1_f=open(in1_fn,'r')
# in2_fn='update2_graph.txt'
# in2_f=open(in2_fn,'r')
# in1_line=in1_f.readlines()
# in2_line=in2_f.readlines()

# in1_nodes=in1_line[0].split(';')
# in2_nodes=in2_line[0].split(';')

class Compare:

    def execute(self,doc1,doc2):
        print '\n\n\n\n'
        novel=[]
        for doc2_node in doc2:
            i=0;found=0;

            while (len(doc1)>0) & (i < len(doc1)):
                if doc2_node == doc1[i]:
                    #doc1.remove(doc2_node)
                    found=1
                    break;
                i= i + 1;

            if found==0:
                print doc2_node
                novel.append(doc2_node);

        return novel
        


        
