# 1. Write a python program to calculate total number of vowels and count of each individual vowels A,E,I,O,U in the string "Guvi Geeks Network Private limited"
vowels = ["a", "e", "i", "o", "u"]  # Only lowercase vowels
string = "Guvi Geeks Network Private limited"

# Convert the string to lowercase
string = string.lower()

# Initialize variables
total_number_of_vowels_including_duplicates = 0
vowel_dictionary = {}

# Iterate over the string to find vowels
for char in string:
    if char in vowels:
        total_number_of_vowels_including_duplicates += 1
        if char not in vowel_dictionary:
            vowel_dictionary[char] = 1
        else:
            vowel_dictionary[char] += 1

print("Total number of vowels:", total_number_of_vowels_including_duplicates)
print("Vowel count:")
for vowel, count in vowel_dictionary.items():
    print(vowel, ":", count)






# 2. Create of pyramid of numbers from 1 to 20.
num = 1 # Adopted Floyds pyramid
for i in range(1,7) : # 20 number takes 6 rows
    for j in range(1,i+1) :
        if num <=20:
            print(num , end=" ")
            num += 1
    print()
        







# 3. write a function that takes a string and return all the vowels removed

def str_wo_vowel():
    string = input("Enter the string: ")
    vowels = "AaEeIiOoUu"
    new_string = ""
    
    for char in string:
        if char not in vowels:
            new_string += char
    
    return new_string

print(str_wo_vowel())




#4. write a function that takes a string and returns number of  unique characters in it.
def number_of_unique_char(string) :
    unique_characters = set(string)
    return len(unique_characters)
string = input("Enter the string : ")
print(number_of_unique_char())


# 5. Write a function that takes astring that returns True if it is palindrome else return False 
def is_palindrome(string) :
    j = len(string) -1
    for i in range(len(string)//2):
        if string[i].lower() == string[j].lower() :
            j -=1
        else :
            return False
    return True
string = input("Enter the string : ")


if is_palindrome(string) :
    print("Given string {",string,"} is palindrome")
else :
    print("Given string {",string,"} is not palindrome")
 





# 6. Write a function that takes two strings and returns the longest common substring between them. 
def longest_substring(str_1,str_2) :
    long_common_str = ""
    for i in range(len(str_1)) :
        for j in range(len(str_2)) :
            common_str = ""
            k = 0
            while i + k < len(str_1) and j +k < len(str_2) and str_1[i+k] == str_2[j+k] :
                common_str += str_1[i+k]
                k += 1
            if len(common_str) > len(long_common_str) :
                long_common_str = common_str
    return long_common_str

str_1 = input(" Enter string 1 : ")
str_2 = input(" Enter string 2 : ")
print("longest common substring is : ", longest_substring(str_1,str_2))    
        





#7. Write a function that takes a string a return the most frequent character in the string.
def most_freq_char (str1):
    char_dict = {}
    for i in str1 :
        if i not in char_dict :
            char_dict[i] = 1
        else :
            char_dict[i] += 1
    most_frequent_char =[]
    max_count = 0
    for char,count in char_dict.items() :
         if max_count < count :
             max_count = count
    for char,count in char_dict.items():
        if count == max_count :
            most_frequent_char.append(char)
    return most_frequent_char
str1 = input("Enter the string : ")
print(" ".join(most_freq_char(str1)))



#8. Write a function that takes a string and return True if it is anagram with another string else return false.
def is_anagram(str1,str2) :
    if len(str1) == len(str2) :
        sorted_string_1 = sorted(str1)
        sorted_string_2 = sorted(str2)
        if sorted_string_1 == sorted_string_2 :
            return True
        else:
            return False
    else :
        return False
    

#9. Write a function that take a string and return number of words in it.
def num_of_words(Str) :
    words_list = str.split()
    return len(words_list)
str = input("Enter a string : ")
print(num_of_words(str))







