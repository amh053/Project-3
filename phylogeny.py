


class Sequence:
    def __init__(self , virus_name, DNA , RNA ,protein ):
        pass

    def search_NCBI(self , accession_number , db = 'nucleotide', rettype = 'fasta'):
        pass

    def get_RNA(self , file_name):
        pass

    def get_protein(self , file_name):
        pass

    def build_dict(self, file_names):
        pass

class DistanceMatrix:
    def __init__(self , matrix , dict_sequences):
        pass

    def build_matrix(self):
        pass

    def global_alignment(self , seq1 , seq2 , sigma , indel):
        pass


class Node:
    def __init__(self, left , right , virus_name , data):
        pass

    def is_leaf(self):
        pass

    def add_children(self):
        pass

class PhyloTree:
    def __init__(self, matrix , dict_sequence, root):
        pass

    def build_nodes(self):
        pass

    def print_tree(self):
        pass

    def neighbor_joining(self):
        pass




