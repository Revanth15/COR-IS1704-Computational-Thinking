def get_longest_subsequence(input_str):
    longest_seq = ""
    current_seq = ""
    for ch in input_str:
        if str(ch).isalpha():
            current_seq += ch
        else:
            if len(longest_seq) < len (current_seq):
                longest_seq = current_seq

            current_seq = ""

    print(longest_seq)

get_longest_subsequence("ab24[AaBbCDExy0longest$] ")
get_longest_subsequence("a a a1234b | c | d ")
get_longest_subsequence("12345 ")
