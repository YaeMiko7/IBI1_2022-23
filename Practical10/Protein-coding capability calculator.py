def analyze_dna_sequence(sequence):
    sequence = sequence.upper()
    start_codon = 'ATG'
    stop_codon = 'TGA'

    if start_codon in sequence and stop_codon in sequence:
        start_index = sequence.index(start_codon) + 3
        stop_index = sequence.index(stop_codon)

        coding_length = stop_index - start_index
        total_length = len(sequence)

        coding_percentage = (coding_length / total_length) * 100

        if coding_percentage > 50:
            return coding_percentage, 'protein-coding'
        elif coding_percentage < 10:
            return coding_percentage, 'non-coding'
        else:
            return coding_percentage, 'unclear'
    else:
        return 0, 'unclear'
sequence = 'ATGCTAGTGCATGACTGA'
coding_percentage, coding_label = analyze_dna_sequence(sequence)
print(f"Percentage of coding sequence: {coding_percentage:.2f}%")
print(f"Label: {coding_label}")
#Percentage of coding sequence: 44.44%
#Label: unclear
