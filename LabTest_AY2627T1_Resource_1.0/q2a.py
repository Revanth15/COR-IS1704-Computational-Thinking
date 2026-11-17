# Name: Revanth
# Email ID: revanth.rs.2026

def classify_messages(messages):
    """
    Classifies a list of messages according to rules specified in the test paper.

    Args:
        messages (list[str]): a list of messages of type string.
    
    Returns:
        list[tuple]: A list of tuples. 
        Each tuple contains the message associated to a category:
        - 'E' : empty message
        - 'U' : urgent message
        - 'Q' : question
        - 'L' : long message
        - 'N' : normal message
    """
    r_list = []
    for msg in messages:
        append_character = "N"
        if msg == "":
            append_character = "E"
        elif msg.startswith("URGENT:"):
            append_character = "U"
        elif msg.endswith("?"):
            append_character = "Q"
        elif len(msg) > 25:
            append_character = "L"
        else:
            append_character = "N"
        r_list.append((msg, append_character))
    # Modify the code below.
    return r_list
