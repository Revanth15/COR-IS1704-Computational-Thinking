def pad_message(msg, width):
    length_of_msg = len(msg)
    padding = width - length_of_msg
    if padding > 0:
        return " " * padding + msg
    else:
        return msg[0:width]

print(pad_message("COR-IS1704 Lab 4", 20))
print(pad_message("COR-IS1704 Lab 4", 8))
print(pad_message("hello", 20))
print(pad_message("python programming", 20)) 
print(pad_message("Hello World! I enjoy programming in Python.",20))