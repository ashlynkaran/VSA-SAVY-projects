## proj11: Tests

from proj11 import *
from fractions import gcd

## Uncomment tests as you need them!

"""
########### sumList ############### 

def sumList_test(lst):
    if sumList(lst) == sum(lst):
        return True

sumList_pass = True

lists = [[], [1], [4,7], [13,2,53], [13,27,31,45], [21,26,37,94,5]]

for lst in lists:
    if not sumList_test(lst):
        print ("sumList failed on list of length " + str(len(lst)) + ".")
        sumList_pass = False

if sumList_pass:
    print "sumList PASS\n"

########### member ############### 

member_pass = True

true_sets = [[1], [1, 2], [2, 3, 4, 1, 2], [2, 1, 3, 4], [2, 1]]
false_sets = [[], [2], [3, 5], [3, 5, 6], [3, 5, 6, 8, 0]]

for set in true_sets:
    if not member(1, set):
        print("member failed on target: 1, set: "),
        print set
        member_pass = False
        break
for set in false_sets:
    if member(1, set):
        print("member failed on target: 1, set: "),
        print set
        member_pass = False
        break

if true_sets != [[1], [1, 2], [2, 3, 4, 1, 2], [2, 1, 3, 4], [2, 1]] or \
                false_sets != [[], [2], [3, 5], [3, 5, 6], [3, 5, 6, 8, 0]]:
    print("member failed by mutating sets")
    member_pass = False

if member_pass:
    print "member PASS\n"

########### addStar ############### 

# addStar("hello") --> "h*e*l*l*o"
# addStar("abc") --> "a*b*c"
# addStar("ab") --> "a*b"

strs = {"hello": "h*e*l*l*o", "abc": "a*b*c", "ab": "a*b", "danger": "d*a*n*g*e*r",
        "": "", "a": "a"}

strs_pass = True

for key in strs:
    if addStar(key) != strs[key]:
        print ("addStar failed on " + key + ". addStar(" + key + ") expected: "
               + strs[key])
        strs_pass = False
        break

if strs_pass:
    print "addStar PASS\n"


########### harmonicSum ############### 

hs_pass = True
val = 0
sum_set = []

for num in range (1,11):
    sum_set.append(val)
    val += (1/float(num))

for num in range (10):
    if harmonicSum(num) != sum_set[num]:
        print "Harmonic Sum Failed on n = ",
        print num
        hs_pass = False

if hs_pass:
    print "harmonicSum PASS\n"


########### isPalindrome ############### 

pal_pass = True

true_list = ["raceCaR", "aManaPlanaCanalPanama", "a Man a Plan a Canal Panama", "abccba"]
false_list = ["banana", "abcb", "abcbaa", "bcba"]

for word in true_list:
    if not isPalindrome(word):
        pal_pass = False
        print "isPalindrome failed on: ",
        print word

for word in false_list:
    if isPalindrome(word):
        pal_pass = False
        print "isPalindrome failed on: ",
        print word

if pal_pass:
    print "isPalindrome PASS\n"

########### replace ############### 

rep_pass = True

orig1 = [[0], [1], [0, 1], [1, 0], [1, 1, 0], [1, 0, 1], [1, 0, 1, 0], [0, 1, 1, 1]]
orig2 = [[0], [1], [0, 1], [1, 0], [1, 1, 0], [1, 0, 1], [1, 0, 1, 0], [0, 1, 1, 1]]
ans = [[0], [4], [0, 4], [4, 0], [4, 4, 0], [4, 0, 4], [4, 0, 4, 0], [0, 4, 4, 4]]

for num in range(len(orig1)):
    count = replace(1, 4, orig1[num], len(orig1[num]))
    if orig1[num] != ans[num]:
        print "replace failed on: ",
        print orig2[num]
        rep_pass = False
    elif count != ans[num].count(4):
        print "replace failed to return corrent count of replaced numbers"
        rep_pass = False

if rep_pass:
    print "replace PASS\n"


########### g_c_d ############### 

gcd_pass = True
gcd_pairs = [[1, 0], [2, 8], [9, 3], [54, 17], [12, 48], [18, 50], [19, 21]]

for pair in gcd_pairs:
    if g_c_d(pair[0], pair[1]) != gcd(pair[0], pair[1]):
        print "g_c_d failed on pair: ",
        print pair[0],
        print ", ",
        print pair[1]
        gcd_pass = False

if gcd_pass:
    print "g_c_d PASS\n"

########### reverseLst ############### 

reverse_pass = True
rev_lsts = [[], ['a'], ['a', 'b'], ['a', 'b', 'c'], ['a', 'b', 'c', 'd']]

for lst in rev_lsts:
    reverseLst(lst, 0, len(lst) - 1)
    ans = lst
    ans.reverse()
    if lst != ans:
        print "reverse failed on: ",
        print lst
        reverse_pass = False

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
reverseLst(lst, 0, 3)
if lst != ['d', 'c', 'b', 'a', 'e', 'f', 'g']:
    print "reverse failed on lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g'], first = 0, " \
          "last = 3",
    reverse_pass = False

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
reverseLst(lst, 3, 6)
if lst != ['a', 'b', 'c', 'g', 'f', 'e', 'd']:
    print "reverse failed on lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g'], first = 3, " \
          "last = 6",
    reverse_pass = False

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
reverseLst(lst, 2, 4)
if lst != ['a', 'b', 'e', 'd', 'c', 'f', 'g']:
    print "reverse failed on lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g'], first = 2, " \
          "last = 4",
    reverse_pass = False

if reverse_pass:
    print "reverseLst PASS\n"

########### convert2Binary ############### 

bin_pass = True

ans = [0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110,
       1111, 10000, 10001, 10010, 10011, 10100, 10101, 10110, 10111, 11000, 11001]
for num in range(26):
    if convert2Binary(num) != str(ans[num]):
        print "convert2Binary failed on ",
        print num
        bin_pass = False

if bin_pass:
    print "convert2Binary PASS\n"


########### printPattern ###############

print "Your pattern should match the exemplar.\n"

print "Exemplar:"
print "****"
print "***"
print "**"
print "*"
print "**"
print "***"
print "****\n"

print "Your pattern:"
printPattern(4)
print ""

########### lstInitialize ###############

initialize_pass = True

lsts = [["a"], [2, 3], [1, 4, 6], ["b", 1, "5", "7"]]

for lst in lsts:
    lstInitialize(lst, "ans", 0, len(lst) - 1)
    for item in lst:
        if item != "ans":
            initialize_pass = False
            print "lstInitialize failed"

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lstInitialize(lst1, "ans", 0, 2)
if lst1 != ["ans", "ans", "ans", 4, 5, 6, 7, 8, 9, 10]:
    initialize_pass = False
    print "lstInitialize failed on lst1"

lst2 = ["a", "b", "c", "d", "a", "b", "c", "d", "a", "b", "c", "d"]
lstInitialize(lst2, 2, 8, len(lst2) - 1)
if lst2 != ["a", "b", "c", "d", "a", "b", "c", "d", 2, 2, 2, 2]:
    initialize_pass = False
    print "lstInitialize failed on lst2"

lst3 = ["a", "b", "c", "d", "a", "b", "c", "d", "a", "b", "c", "d"]
lstInitialize(lst3, 7, 1, 5)
if lst3 != ["a", 7, 7, 7, 7, 7, "c", "d", "a", "b", "c", "d"]:
    initialize_pass = False
    print "lstInitialize failed on lst3"

if initialize_pass:
    print "lstInitialize PASS\n"

"""

## Add any tests you need for extension functions here!