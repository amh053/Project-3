


class Sequence:
    def __init__(self , virus_name, DNA: str = '', RNA: str = '', protein: str = ''):
        self.virus_name = virus_name
        self.DNA = DNA
        self.RNA = RNA
        self.protein = protein

    def search_NCBI(self , accession_number , db = 'nucleotide', rettype = 'fasta'):
        url = (
            f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
            f"?db={db}&id={accession_number}&rettype={rettype}&retmode=text"
        )
        with urllib.request.urlopen(url) as response:
            fasta = response.read().decode("utf-8")

        if not fasta.startswith('>'):
            raise Exception('Sequence not found')

        lines = fasta.split('\n')
        self.DNA = ''.join(lines[1:]).strip()

    def get_RNA(self , file_name):
        if self.DNA == '':
            raise Exception('No DNA sequence to convert')

        self.RNA = ''

        for NT in self.DNA:
            if NT == 'A':
                self.RNA += 'U'
            elif NT == 'T' or NT == 'G' or NT == 'C':
                self.RNA += NT
            else:
                raise Exception('Invalid DNA sequence')



    def get_protein(self , file_name):
        pass

    def build_dict(self, file_names):
        """
        key: virus_name
        value: DNA sequence
        """


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





