from q3 import extract_bold_texts

# Test Cases:
print("Test Case #1:")
print()
print("Expected:")
print("['ABC', 'def 123 ', '']")
print("Actual  :")
print(extract_bold_texts('<b>ABC</b> abc <b>def 123 </b><b></b>0000'))

print("\n==========\n")

print("Test Case #2:")
print()
print("Expected:")
print("[]")
print("Actual  :")
print(extract_bold_texts('A piece of text without tags.'))
