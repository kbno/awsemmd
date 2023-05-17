import sys


charges_dict = {"G": 0.0, "A": 0.0, "L": 0.0, "I": 0.0,
                "R": 1.0, "K": 1.0, "M": 0.0, "C": 0.0,
                "Y": 0.0, "T": 0.0, "P": 0.0, "S": 0.0,
                "W": 0.0, "D": -1.0, "E": -1.0, "N":0.0,
                "Q": 0.0,"F": 0.0, "H": 0.0, "V": 0.0}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'{sys,argv[0]} seq_file')
        sys.exit()
    
    seq_file = sys.argv[1]
    with open(seq_file, 'r') as input_file:
        line = input_file.readlines()[0]
    line_lst = list(line)
    with open('charge_on_residues.dat', 'w') as outfile:
        outfile.write(f'{len(line_lst)}\n')
        for i, residue in enumerate(line_lst): 
            if residue != '\n':
                outfile.write(f'{i+1} {charges_dict[residue]}\n')
            
