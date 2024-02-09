Question 1 
What data type is each of the following?
#finding the data types of different inputs
import math

print(type(5))  #  <class 'int'>
print(type(5.0))  # <class 'float'>
print(type(5 > 1))  # <class 'bool'>
print(type('5'))  # <class 'str'>
print(type(5 * 2))  # <class 'int'>
print(type('5' * 2))  # <class 'str'>
print(type('5' + '2'))  # <class 'str'>
print(type(5 / 2))  # <class 'float'>
print(type({5, 2, 1}))  # <class 'set'>
print(type(5 == 3))  # <class 'bool'>
print(type(3.14)) # <class 'float'>


Question 2 
Write (and evaluate) Python expressions that answer these questions:
a. How many letters are there in 'Supercalifragilisticexpialidocious'?

element = 'Supercalifragilisticexpialidocious'
num = len(element)
print("Number of letters:", num)

#OUTPUT = Number of letters: 34


b. Does 'Supercalifragilisticexpialidocious' contain 'ice' as a substring?

element = 'Supercalifragilisticexpialidocious'
contains_ice = 'ice' in element
print("Contains 'ice' as a substring:", contains_ice)

#OUTPUT = Contains 'ice' as a substring: True


c. Which of the following words is the longest: Supercalifragilisticexpialidocious, Honorificabilitudinitatibus, or Bababadalgharaghtakamminarronnkonn?

letters = ['Supercalifragilisticexpialidocious', 'Honorificabilitudinitatibus', 'Bababadalgharaghtakamminarronnkonn']
longest_word = max(letters, key=len)
print("Longest word:", longest_word)

#OUTPUT = Longest word: Supercalifragilisticexpialidocious


d. Which composer comes first in the dictionary: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'. Which one comes last?

composers = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
first_composer = min(composers)
last_composer = max(composers)
print("First composer in dictionary order:", first_composer)
print("Last composer in dictionary order:", last_composer)

#OUTPUT = First composer in dictionary order: Bartok ; Last composer in dictionary order: Buxtehude

3.Implement function triangleArea(a,b,c) that takes as input the lengths of the 3
sides of a triangle and returns the area of the triangle. By Heron's formula, the area
of a triangle with side lengths a, b, and c is
s(s - a)(s -b)(s -c), where
s = (a +b + c) /2.

def triangleArea(a, b, c):
    # Calculate the semi-perimeter of the triangle
    s = (a + b + c) / 2
    # Calculate the area of the triangle using Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

# Test the function with the given input
triangleArea(2, 2, 2)

#Output
#1.73205080756887723

4.Write a program in python to separate odd and even integers in separate arrays. Go
to the editor
Test Data :
Input the number of elements to be stored in the array :5
Input 5 elements in the array :
element - 0 : 25
element - 1 : 47
element - 2 : 42
element - 3 : 56
element - 4 : 32


def separate_odd_even(numbers):
    # Initialize empty lists for odd and even integers
    odd_numbers = []
    even_numbers = []
    
    # Iterate through the numbers and separate them into odd and even
    for number in numbers:
        if number % 2 == 0:  # If the number is even
            even_numbers.append(number)
        else:  # If the number is odd
            odd_numbers.append(number)
    
    return odd_numbers, even_numbers

# Test data
numbers = [25, 47, 42, 56, 32]

odd_numbers, even_numbers = separate_odd_even(numbers)

print("\n The even elements: ", even_numbers)
print("\n The odd elements: ", odd_numbers)

#OUTPUT
#The even elements:  [42, 56, 32]
#The odd elements:  [25, 47]


Question 5
a. Write a function inside(x,y,x1,y1,x2,y2) that returns True or False depending on whether the point (x,y) lies in the rectangle with lower left corner (x1,y1) and upper right corner (x2,y2).
>>> inside(1,1,0,0,2,3)
True
>>> inside(-1,-1,0,0,2,3)
False

def inside(x,y,x1,x2,y1,y2):
    if(x>x1 and y<y1):
        if(x>x2 and y<y2):
            print("true")
    else:
        print("false")


inside(1, 1, 0, 0, 2, 3)
inside(-1,-1,0,0,2,3)

#OUTPUT
#true
#false


b. Use function inside() from part a. to write an expression that tests whether the point (1,1) lies in both of the following rectangles: one with lower left corner (0.3, 0.5) and upper right corner (1.1, 0.7) and the other with lower left corner (0.5, 0.2) and upper right corner (1.1, 2).

Point = (1,1)
upper_right = (0.5,0.2)
lower_left = (1.1,0.2)

def inside(pt,r,l):
    if(pt[0] > l[0] and pt[0] < r[0] and pt[1] > l[1] and pt[1] < r[1]):
        return True
    else:
        return False
print(inside(Point, upper_right, lower_left))

#OUTPUT
#False

Question 6
You can turn a word into pig-Latin using the following two rules (simplified):
• If the word starts with a consonant, move that letter to the end and append 'ay'. For example, 'happy' becomes 'appyhay' and 'pencil' becomes 'encilpay'.
• If the word starts with a vowel, simply append 'way' to the end of the word. For example, 'enter' becomes 'enterway' and 'other' becomes 'otherway' . For our purposes, there are 5 vowels: a, e, i, o, u (so we count y as a consonant).
Write a function pig() that takes a word (i.e., a words) as input and returns its pig-Latin form. Your function should still work if the input word contains upper case characters. Your output should always be lower case however.>>> pig('happy')
'appyhay'>>> pig('Enter')
'enterway'
def pig(words):
    # convert into lower case
    words = words.lower()
    
    vowel = "aeiou"
    
    if words[0] not in vowel:
        # Move  the first letter to the end and append 'ay'
        return words[1:] + words[0] + 'ay'
    else:
       # append 'way'
        return words + 'way'


print(pig('happy')) 
print(pig('Enter'))  

#OUTPUT
#appyhay
#enterway

Question 7
File bloodtype1.txt records blood-types of patients (A, B, AB, O or OO) at a clinic. Write a function bldcount() that reads the file with name name and reports (i.e., prints) how many patients there are in each bloodtype.>>> bldcount('bloodtype.txt')
There are 10 patients of blood type A.
There is one patient of blood type B.
There are 10 patients of blood type AB.
There are 12 patients of blood type O.
There are no patients of blood type OO.

def bldcount(filename):
    # A dictionary is created with a key value pair of blood type and its count
    blood_type_count = {'A': 0, 'B': 0, 'AB': 0, 'O': 0, 'OO': 0}
    
    try:
        
        with open(filename, 'r') as file:
            #file contents are stored into data
            data = file.read()
            
           
            blood_types = data.split()
            
            # Count the occurrence of each blood type
            for blood in blood_types:# for each bloodtype found in the file, the blood count is incread by 1 in the dictionary
                if blood in blood_type_count:
                    blood_type_count[blood] += 1
    
        # Print the count of each blood type
        for bloo, count in blood_type_count.items():
            print(f"Blood type {bloo}: {count} patients")
    
    except notFoundError:
        print("file not found.")

# Calling the function on the file saved in my local
bldcount('C:\Users\rahul\OneDrive\Desktop\problem set-1\bloodtype.txt')

#OUTPUT
#Blood type A: 15 patients
#Blood type B: 1 patients
#Blood type AB: 13 patients
#Blood type O: 15 patients
#Blood type OO: 0 patients


Question 8
Write a function curconv() that takes as input:
1. a currency represented using a words (e.g., 'JPY' for the Japanese Yen or 'EUR' for the Euro)
2. an amount
and then converts and returns the amount in US dollars.>>> curconv('EUR', 100)
122.96544>>> curconv('JPY', 100) 1.241401
The currency rates you will need are stored in file currencies.txt:
#I have used pandas library to access the file and create data frame
import pandas as pd

def curconv(currency, amount):
    
        # Read the currency exchange rates from the file into a DataFrame f. split into columns and
        #later make currency column index of this dataframe
        f = pd.read_csv('C:\Users\rahul\OneDrive\Desktop\problem set-1\currency.txt', sep='\t', header=None,
                         names=['Currency', 'Rate', 'Name'], decimal=',')

        f.set_index('Currency', inplace=True)
        
        # Check if the provided currency code is in the dataframe
        if currency in f.index:
            
            rate = float(f.loc[currency, 'Rate'])#locate the rate for that currency
            # Perform the conversion to USD
            usd_amount = amount * rate
            
            return usd_amount
        
        else:
            return f"'{currency}' not found."

print(curconv('EUR', 100))  
print(curconv('JPY', 100)) 

#Output
#122.96544
#1.241401


Question 9
Each of the following will cause an exception (an error). Identify what type of exception each will cause.
Trying to add incompatible variables, as in adding 6 + ‘a’--->TypeError : unsupported operand type(s) for +: 'int' and 'str'
Referring to the 12th item of a list that has only 10 items-->IndexError :list index out of range
Using a value that is out of range for a function’s input, such as calling math.sqrt( 1.0)-->ValueError: math domain error
Using an undeclared variable, such as p rint(x) when x has not been defined-->NameError: name 'x' is not defined
Trying to open a file that does not exist, such as mistyping the file name or looking in the wrong directory.-->FileNotFoundError


Question 10 
Encryption is the process of hiding the meaning of a text by substituting letters in the message with other letters, according to some system. If the process is successful, no one but the intended recipient can understand the encrypted message. Cryptanalysis refers to attempts to undo the encryption, even if some details of the encryption are unknown (for example, if an encrypted message has been intercepted). The first step of cryptanalysis is often to build up a table of letter frequencies in the encrypted text. Assume that the words letters is already defined as 'abcdefghijklmnopqrstuvwxyz'. Write a function called frequencies() that takes a words as its only parameter, and returns a list of integers, showing the number of times each character appears in the text. Your function may ignore any characters that are not in letters.>>> frequencies('The quick red fox got bored and went home.')
[1, 1, 1, 3, 5, 1, 1, 2, 1, 0, 1, 0, 1, 2, 4, 0, 1, 2, 0, 2, 1, 0, 1, 1, 0, 0] >>> frequencies('apple')
def frequencies(texts):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    # list with frequencies for the 26 letters
    frequency = [0] * 26
    
    #case conversion
    texts = texts.lower()
    for char in texts:
        if char in letters:
            
            index = letters.index(char)
            frequency[index] += 1
    
    return frequency


print(frequencies('The quick red fox got bored and went home.'))
print(frequencies('apple'))

#OUTPUT
#[1, 1, 1, 3, 5, 1, 1, 2, 1, 0, 1, 0, 1, 2, 4, 0, 1, 2, 0, 3, 1, 0, 1, 1, 0, 0]
#[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

