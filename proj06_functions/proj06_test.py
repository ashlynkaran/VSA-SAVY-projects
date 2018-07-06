from proj06_01 import *


# TESTS
# Feel free to add your own tests as needed!

print ("Divisors Tests")
# Test 1
if divisors(1) == [1]:
    print("Test 1: PASS")
else:
    print("Test 1: FAIL")

# Test 2
if divisors(8) == [1,2,4,8]:
    print("Test 2: PASS")
else:
    print("Test 2: FAIL")

# Test 3
if divisors(9) == [1,3,9]:
    print("Test 3: PASS\n")
else:
    print("Test 3: FAIL\n")

print("Prime Tests")
# Test 4
if prime(9):
    print("Test 4: FAIL")
else:
    print("Test 4: PASS")

# Test 5
if prime(7):
    print("Test 5: PASS\n")
else:
    print("Test 5: FAIL\n")

L1 = []
L2 = [3, 4]
L3 = [3, "a"]
L4 = [5, "b", 10, 7, "a"]
L5 = [5, 7, 11]


vowels = ['a', 'e', 'i', 'o', 'u', 'y']

print("Vowel Finder Tests")

# Test 6
if vowelFinder(['C', 'n', 's', 'n', 't', 's'], vowels) == []:
    print ("Test 6: PASS")
else:
    print ("Test 6: FAIL")

sentence_string = "Hello, my name is Monty Python."
sentence_list = []
for letter in sentence_string:
    sentence_list.append(letter)

# Test 7
if vowelFinder(sentence_list, vowels) == ['a', 'e', 'i', 'o', 'y']:
    print ("Test 7: PASS\n")
else:
    print ("Test 7: FAIL\n")


#Add your own tests here!!