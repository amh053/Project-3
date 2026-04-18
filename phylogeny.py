

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
    def __init__(self , dict_sequences):
        self.matrix = Array()
        self.dict_sequences = dict_sequences
        self.virus_names = list(dict_sequences.keys())

    def build_matrix(self,sigma,indel):
        n = len(self.virus_names)

        for i in range(n + 1):
            temp = Array()
            for j in range(n + 1):
                temp.append(0)
            self.matrix.append(temp)

        for i in range(n):
            for j in range(i,n):
                seq1 = self.dict_sequences[self.virus_names[i]]
                seq2 = self.dict_sequences[self.virus_names[j]]

                align_score = DistanceMatrix.global_alignment(seq1,seq2,sigma,indel)

                distance = -align_score

                self.matrix[i][j] = distance
                self.matrix[j][i] = distance



    def global_alignment(self , seq1 , seq2 , sigma , indel):
        m = len(seq1)
        n = len(seq2)
        matrix = Array()

        for i in range(m + 1):
            temp = Array()
            for j in range(n + 1):
                temp.append(0)
            matrix.append(temp)

        for i in range(1, m + 1):
            matrix[i][0] = matrix[i - 1][0] + indel

        for j in range(1, n + 1):
            matrix[0][j] = matrix[0][j - 1] + indel

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                match = matrix[i - 1][j - 1] + sigma[(seq1[i - 1], seq2[j - 1])]
                delete = matrix[i - 1][j] + indel
                insert = matrix[i][j - 1] + indel

                matrix[i][j] = max(match, delete, insert)

        return matrix[m][n]


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





