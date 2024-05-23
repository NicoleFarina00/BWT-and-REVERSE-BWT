def bwt(input_string):
    #Add the terminator character "$" to the end of the string
    input_string += "$"

    #Build all rotations of the string with the terminator
    rotations =[input_string[i:] + input_string[:i] for i in range(len(input_string))]

    #Custom sort function to ignore case differences
    def case_insensitive_sort(rotation):
        return rotation.lower()

    #Sort the rotations in lexicographic order
    sorted_rotations = sorted(rotations, key=case_insensitive_sort)

    #Extract the last character of each rotation to form the BWT string
    bwt_string = ''.join(rotation[-1] for rotation in sorted_rotations)

    return bwt_string

def calc_lexicographic_order(bwt):
    #Determine the alphabet from the BWT string, ignoring case
    alphabet=sorted(set(bwt.lower())) #Ignore case differences
    #Create a mapping of characters to their lexicographic order
    lex_order = {char: idx for idx, char in enumerate(alphabet)}
    return lex_order

def calc_ranks(bwt):
    #Calculate the rank for each character in the BWT string
    ranks = []
    counts = {}

    for char in bwt:
        if char not in counts:
            counts[char] = 0
        ranks.append(counts[char])
        counts[char] += 1

    return ranks

def calc_positions(bwt):
    #Calculate the position of each character in the BWT string
    positions = {}
    for idx, char in enumerate(bwt):
        positions[char] = idx + 1 #Positions start from 1 instead of 0
    return positions

def calc_counting(lex_order, bwt):
    #Calculate the counting cof each character
    counts = {char: 0 for char in lex_order}
    sorted_bwt = sorted(bwt.lower())

    for char in sorted_bwt:
        counts[char] += 1

    counting = {}
    cumulative = 0

    for char in sorted(counts):
        counting[char] = cumulative
        cumulative += counts[char]

    return counting

def reverse_bwt(bwt):
    if '$' not in bwt:
        raise ValueError("The BWT string must contain the terminator character '$'.")
    lex_order = calc_lexicographic_order(bwt)
    ranks = calc_ranks(bwt)
    positions = calc_positions(bwt)
    counting = calc_counting(lex_order, bwt)

    #Find the index of the terminator character '$' in the BWT string
    idx = bwt.index('$')
    original = []

    for _ in range(len(bwt)):
        char = bwt[idx]
        original.append(char)
        rank = ranks[idx]
        #Calculate the next index using counting and rank
        idx = counting[char.lower()] + rank

    #Join and return the reversed string (excluding the terminator '$')
    return ''.join(original[::-1]).strip('$')

if __name__ == "__main__":
    sequence = "BANANA"
    transformed = bwt(sequence)
    print(transformed)
    reversed = reverse_bwt(transformed)
    print(reversed)