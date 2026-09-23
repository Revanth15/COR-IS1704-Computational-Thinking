# Name: Revanth
# Email ID: revanth.rs.2026

def retrieve_numbers(str_input):
    # Replace the code below with your implementation.
    prev_ch = ""
    return_str = ""
    for ch in str_input:
        if ch.isdigit():
            prev_ch += ch
        else:
            if prev_ch != "":
                return_str += prev_ch + " "
            prev_ch = ""
        
    return_str += prev_ch
    return return_str  