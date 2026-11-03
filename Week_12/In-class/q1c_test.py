from q1c import add_new_email

# Test Cases:
print("Test Case #1:")
print()
my_dict = {'Jack': 'jack@gmail.com', 'Peter': 'peter@smu.edu.sg'}
pair = ('Peter', 'peter@sis.smu.edu.sg')
print("Expected returned value:")
print("peter@smu.edu.sg")
print("Actual returned value:")
print(add_new_email(my_dict, pair))
print("Expected dictionary:")
print("{'Jack': 'jack@gmail.com', 'Peter': 'peter@sis.smu.edu.sg'}")
print("Actual dictionary:")
print(my_dict)

print("\n==========\n")

print("Test Case #2:")
print()
my_dict = {'Jack': 'jack@gmail.com', 'Peter': 'peter@smu.edu.sg'}
pair = ('Mary', 'mary@sis.smu.edu.sg')
print("Expected returned value:")
print("None")
print("Actual returned value:")
print(add_new_email(my_dict, pair))
print("Expected dictionary:")
print("{'Jack': 'jack@gmail.com', 'Peter': 'peter@smu.edu.sg', 'Mary': 'mary@sis.smu.edu.sg'}")
print("Actual dictionary:")
print(my_dict)
