fin = open("words.txt")


def is_palindrome3():
    count = 0
    for line in fin:
        word = line.strip()
        if word == word[::-1]:
            count += 1
            print(word)
    print(count)
#is_palindrome3()

def char_20():
    """prints only words with more than 20 characters on the text file
       word.txt
    """
    for line in fin:
        if len(line) > 20:
            print(line)

# char_20()

def has_no_e(word):
    w = word.find('e')
    if w == -1:
        return True
    else:
        return False

def printing():
    count = 0
    for word in fin:
        if has_no_e(word):
            print(word)
            count += 1
    print(count)

#printing()
#Exercise 9-4
def avoids(word,string):
    for s in string:
        if s in word:
            return False
    return True

def avoids2():
    string = input("Give me: ")
    for line in fin:
        word = line.strip()
        if avoids(word,string):
            print(word)

#avoids2()

def uses_all(word,string):
    for s in string:
        if word.find(s) == -1:
            return False
    return True



def uses_all2():
    """This function in combination with uses_all() checks if all characters
       of a string are used in the word list
    """
    string = input("Give me: ")
    for line in fin:
        word = line.strip()
        if uses_all(word,string):
            print(word)

#print(uses_all('Alireza Mohammadi',"imx"))
#uses_all2()

def is_abecedarian(word):
    """This function in combination with is_abecedarian_check() checks if
       characters of words in the list are in alphabetical order.
    """
    v = 0
    for letter in word:
        if ord(letter) < v:
            return False
        v = ord(letter)
    return True

def is_abecedarian2(word):
    """Writing is_abecedarian() with recursion!
    """
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])


def checking(f):
    for line in fin:
        word = line.strip()
        if f(word):
            print(word)


def is_triple_double(word):
    if len(word) < 6:
        return False
    b = 0
    while b < len(word)-1:
        if word[b] != word[b+1]:
            return False
        b += 2
    return True

#print(is_triple_double("aawwssiiccvvllddjjffoossmm"))
#checking(is_triple_double)


def is_triple_double(word):
    """Tests if a word contains three consecutive double letters.
    word: string
    returns: bool
    """
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            i = i + 1 - 2*count
            count = 0
    return False


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)

#find_triple_double()


if __name__ == '__main__':
    print(is_abecedarian('1243'))
    #checking(is_abecedarian)
