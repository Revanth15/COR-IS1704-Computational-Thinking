from q1b import create_email_dict

# Test Cases:
people = [
    'Jack', 'jack@gmail.com',
    'Mary', 'mary.loh@smu.edu.sg',
    'John', 'john.smith@microsoft.com',
]

print("Test Case #1:")
print()
print("Expected:")
print("{'Jack': 'jack@gmail.com', 'Mary': 'mary.loh@smu.edu.sg', 'John': 'john.smith@microsoft.com'}")
print("Actual  :")
print(create_email_dict(people))

print("\n==========\n")

print("Test Case #2:")
print()
print("Expected:")
print("{}")
print("Actual  :")
print(create_email_dict([]))
