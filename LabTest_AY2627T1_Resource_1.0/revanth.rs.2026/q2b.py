# Name: Revanth
# Email ID: revanth.rs.2026
 
def verify_tags(tags):
    """
    Verify a list of warehouse tags.
 
    Each tag is a 9-character string in the format:
        <parcel_id><weight_code><parity_char>
    where:
        parcel_id   - 5 uppercase letters identifying the parcel
        weight_code - 3 digits representing the weight in grams
        parity_char - 'E' if the weight is even, 'O' if the weight is odd
 
    A tag is valid only if both conditions hold:
        1. parity_char correctly matches the parity of the weight.
        2. parcel_id contains at least 3 distinct letters.
 
    Args:
        tags (list[str]): A list of tag strings. May be empty.
    Returns:
        list[tuple(str, int, bool)]: A list of (parcel_id, weight, is_valid)
             tuples, one per tag, in the same order as tags.
    """
    # Modify the code below.
    compiled_lst = []
    for tag in tags:
        parcel_id = tag[:5]
        weight_code = tag[5:8]
        parity_char = tag[-1]
        weight_code = int(weight_code)

        distinct_lettrs = []
        for ch in parcel_id:
            if ch not in distinct_lettrs:
                distinct_lettrs.append(ch)

        is_valid = False
        if len(distinct_lettrs) >= 3:
            if parity_char == "E" and weight_code % 2 == 0:
                is_valid = True
            elif parity_char == "O" and weight_code % 2 != 0:
                is_valid = True

        compiled_lst.append((parcel_id,weight_code,is_valid))

    return compiled_lst
