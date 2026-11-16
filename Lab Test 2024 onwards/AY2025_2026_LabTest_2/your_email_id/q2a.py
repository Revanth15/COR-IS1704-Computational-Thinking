# Name:
# Email ID:

def decode_potter(filename):
    """
    Extract strings from a file of encoded text

    Args:
        filename (str): The name of the file to read.

    Returns:
        list: A list of strings extracted from each line of the file
    """
    # Modify the code below.
    sentences = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            sentence_length = line[:3]
            sentence = line[3:int(sentence_length)+3]
            sentences.append(sentence)
    return sentences
