import Chapter10


fin = open("words.txt")
#word_list = Chapter10.word_list()

dic = {}
def dic_word_list(a_list):
    for n in a_list:
        if n in dic:
            return dic[n]
        dic[n] = dic.get(n,0)
        #dic[n] += 1
    return dic

def invert_dict(dict):
    inverse = {}
    for key in dict:
        value = dict[key]
        inverse[value] = inverse.setdefault(value,[]).append(key)

    return inverse

cache = {}
def ackermann(m, n):
    """Computes the Ackermann function A(m, n)
    See http://en.wikipedia.org/wiki/Ackermann_function
    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)

    if (m, n) in cache:
        return cache[m, n]
    else:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0)
        d[c] += 1
    return d

known = {}
def has_duplicates2(list_parameters):
    """takes a list and returns True if there is any element
       that appears more than once. It is faster than first function
       due to the usage of dictionaries
    """
    joined = ''.join(list_parameters)
    b = 0
    while b < len(joined):
        a = joined[b]
        known[a] = known.get(a,0)
        known[a] += 1
        b += 1
        if known[a] > 1:
            return True
    return False

def word_list():
    """reads the file words.txt and builds a list with one
       element per word (fast version)
    """
    list_of_words = []
    for line in fin:
        word = line.strip()
        list_of_words.append(word)
    return list_of_words

def in_bisect(word_list,b):
    """takes a sorted list and a target value and returns
       the index of the value in the list if it’s there,
       or None if it’s not.
    """
    if b == word_list[0]:
        return True

    i = len(word_list)
    while i != 1:
        i = len(word_list) // 2
        if word_list[i] == b or word_list[i-1] == b:
            return True

        elif b < word_list[i]:
            word_list = word_list[:i]

        elif b > word_list[i]:
            word_list = word_list[i:]
    return False

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


def rotate_word2(word_list):
    dict = dic_word_list(word_list)
    dic = {}
    for number in range(1,25):
        for word in word_list:
            a = rotate_word(word,number)
            if a in dict:
                dic[word] = [a,number]
    return dic

def rotate_word3(word):
    rotated = ""
    for char in word:
        rotated = char + rotated
        print(rotated)
    return rotated

def homophone(word_list):
    dict = dic_word_list(word_list[1:10])
    for key,val in dict.items():
        print(key,val)





if __name__ == '__main__':
    #print(nested_sum([1,2,3,[4,5]]))
    #print(cumsum([1,2,3,4,5,4,534,2343]))
    #print(middle([1,2,3,3235,435,658,234,9879,4,5]))
    #print(middle([1,2,3,3235,435,658,234,9879,4,5]))
    #print(is_sorted(['1','234789','ABCD','abzx']))
    #print(has_duplicates2(['abc','wskjhgfdddddD']))
    # print(word_list[-10:-1])
    #print(approval_bisect())
    #print(word_list())
    #print(dic_word_list(word_list))
    #print(invert_dict(histogram('parrot')))
    #print(histogram('pattpprrot'))
    #print(ackermann(3,4))
    #print(rotate_word('jolly', 25))
    word_list = word_list()
    #print(rotate_word2(word_list))
    #print(rotate_word3('Alieza'))
    pass
