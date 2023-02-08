def traverse(a):
    index = 0
    len_a = len(a) - 1
    while index <= len_a:
        print(a[len_a])
        len_a = len_a - 1

#traverse("I Lovee You")

def traverse2(a):
    for letter in a:
        print(letter)


#traverse2("I Love You")

def loops():
    prefixes = 'JKLMNP'
    pref = 'OQ'
    suffix = 'ack'
    suffix2 = 'uack'

    for letter in prefixes:
            print( letter + suffix)
    for letter in pref:
            print( letter + suffix2)

#loops()


def find(word, letter,num):
    """Checks if a letter exists in a word and returns its index
        num gives the starting point index
    """
    index = num
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

def counter(word,char):
    """Checks how many times a letter repeated.
    """
    count = 0
    for letter in word:
        if letter == char:
            count = count + 1
    print(count)

#counter("sSs", "s")

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2)-1
    while j >= 0:
        print(i,j)
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1

    return True
#print(is_reverse("Alireza","azerilA"))

#a = "there is a car in my door way and ali is gouing to take a ride on it"
#print(a[::-1])


def is_palindrome2(a):
    if a == a[::-1]:
        return True
    else:
        return False


# while True:
#     a = input("Let's check if your word is palindrome:")
#     if is_palindrome2(a):
#         print("Yeah, it's palindrome.")
#     elif a == "done":
#         print("\n         Well, you found the hack!")
#         break
#     else:
#         print("Nah! Try again!")

# def rotate_letter(word,number):
#     """Rotates a word's letters by the given number and returns the result
#     """
#     word = word.lower()
#     for letter in word:
#         if ord(letter) + number > 122:
#         a = ord(letter)
#         a = a + number
#         b = chr(a)
#         print(b)

#rotate_letter("Zli",2)
def ref(word,number):
    """
        This function in combination with repeat_word takes a word and a number and Rotates
        letters of that word each by that number
    """
    #check if number is negative
    num = number % 25
    if number < 0:
        num += 1
    for letter in word:
        o = ord(letter)
        ordinal = (o + num)
        if ordinal > 122:
            o2 = (o + num) % 122
            o3 = chr(o2+96)
            return o3
        else:
            o4 = chr(ordinal)
            return o4



def rotate_word(word,number):
    assigned = ""
    for letter in word:
        if letter.isupper():
            letter = letter.lower()
            assigned += ref(letter,number).upper()
        else:
            assigned += ref(letter,number)
    return assigned

print(rotate_word('jolly', -7))
print(rotate_word('melon', -10))
print(rotate_word('sleep', 9))
