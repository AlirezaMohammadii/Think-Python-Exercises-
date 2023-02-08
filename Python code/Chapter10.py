import Chapter9
import Chapter11

#Exercise 10-1
def nested_sum(nested_list):
    """takes a list of lists of integers and adds up the
       elements from all of the nested lists.
    """
    nest = []
    for digit in nested_list:
        if str(digit).isdigit():
            nest.append(digit)
        else:
            for i in digit:
                nest.append(i)
    return sum(nest)

#Exercise 10-2
def cumsum(numbers_list):
    """akes a list of numbers and returns the cumulative sum;
    """
    cum = 0
    cum_list = []
    for number in range(len(numbers_list)):
        cum += numbers_list[number]
        cum_list.append(cum)
    return cum_list

#Exercise 10-3
def middle(numbers_list):
    """takes a list and returns a new list that contains all
       but the first and last elements.
    """
    n = numbers_list[1:]
    n = n[:-1]
    return n

#Exercise 10-4
def chop(numbers_list):
    """takes a list and returns a new list that contains all
       but the first and last elements.
    """
    numbers_list.pop(0)
    numbers_list.pop()
    return numbers_list

#Exercise 10-5
def is_sorted(list_parameters):
    """takes a list as a parameter and returns True if
       the list is sorted in ascending order and False otherwise.
    """
    joined = ''.join(list_parameters)
    return Chapter9.is_abecedarian(joined)
    #return Chapter9.is_abecedarian(list_parameters)

def has_duplicates(list_parameters):
    """takes a list and returns True if there is any element
       that appears more than once
    """
    joined = ''.join(list_parameters)
    b = 0
    while b < len(joined):
        a = joined[b]
        if joined[b+1:].find(a) != -1:
            return True
        else:
            b += 1
    return False

fin = open("words.txt")

def word_list():
    """reads the file words.txt and builds a list with one
       element per word (fast version)
    """
    list_of_words = []
    for line in fin:
        word = line.strip()
        list_of_words.append(word)
    return list_of_words

def word_list2():
    """reads the file words.txt and builds a list with one
       element per word (slow version)
    """
    list_of_words = []
    for word in fin:
        list_of_words = list_of_words + [word]
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
        if word_list[i] == b:
            return True

        elif b < word_list[i]:
            word_list = word_list[:i]

        elif b > word_list[i]:
            word_list = word_list[i:]
    return False


word_list = word_list()

def approval_bisect():
        for i in word_list:
            return in_bisect(word_list,i)


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0)
        d[c] += 1
    return d



if __name__ == '__main__':
    #print(nested_sum([1,2,3,[4,5]]))
    #print(cumsum([1,2,3,4,5,4,534,2343]))
    #print(middle([1,2,3,3235,435,658,234,9879,4,5]))
    #print(middle([1,2,3,3235,435,658,234,9879,4,5]))
    #print(is_sorted(['1','234789','ABCD','abzx']))
    #print(has_duplicates(['abc','wxpytdszqASDFGHJKLy']))
    # print(word_list[-10:-1])
    print(approval_bisect())
    #print(in_bisect(word_list,'ti'))
    #print(word_list())
    #print(Chapter11.dic_word_list(word_list))
    pass
