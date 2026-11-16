# Name:
# Email ID:

def decode_potter_checksum(filename):
    """
    Extract strings from a file of encoded text and compare
    the computed checksum against the expected checksum to 
    detect data corruption.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list[tuple(str, int, bool)]: A list of tuples,
          with one tuple for each line of the file.  
        * str: the text extracted from the message
        * int: the calculated checksum for this message
        * bool: True if calculated checksum is equal to expected checksum
    """    
    # Modify the code below.
    sentences = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            sentence_length = line[:3]
            sentence = line[3:int(sentence_length)+3]
            checksum = int(sentence[-2:])
            num_vowels = 0
            for ch in sentence:
                if ch in "AaEeIiOoUu":
                    num_vowels +=1
            sentences.append((sentence[0:-2], num_vowels, True if num_vowels == checksum else False))
    return sentences
