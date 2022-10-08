# .isalnum() - check if all characters are alphanumeric
# indexing and slicing
# AHJSS 5088 C

#panNum = "AHJSS5088C"
# print(panNum[0:5])
# print(panNum[9:])
# print(panNum[5:9])

panNum = input("Enter a pan number: ")

if len(panNum) == 10 and panNum[0:5].isalpha() and panNum[5:9].isdigit() and panNum[9:].isalpha():
    print(f"{panNum} Valid PAN Number.")
else:
    print("Invalid PAN Number.")


