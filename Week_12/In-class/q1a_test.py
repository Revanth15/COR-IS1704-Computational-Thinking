from q1a import retrieve_email

# Test Cases:
email_dict = {'Jack': 'jack@gmail.com', 'Peter': 'peter@smu.edu.sg'}

print("Test Case #1:")
print()
print("Expected:")
print("jack@gmail.com")
print("Actual  :")
print(retrieve_email(email_dict, 'Jack'))

print("\n==========\n")

print("Test Case #2:")
print()
print("Expected:")
print("None")
print("Actual  :")
print(retrieve_email(email_dict, 'John'))
