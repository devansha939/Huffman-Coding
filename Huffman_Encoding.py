import sortedcontainers as sc

def letter_distribution(original_string):
        '''This function takes a string. Then it count the number of occurrences of each letter and returns a dictionary.'''
        # First we will create a dictionary 'letter_occurrence' in which we will store character and their corresponding frequecies in 'original_string'.
        letter_occurrence = {}
        # Now we will traverse over whole string and will increase occurence of character in 'letter_occurrence' as we will find it.
        for char in original_string:     
            # Here checking the condition whether letter appear befor or not, if not appear we have to assign its value as 1 and if already appear we have to increase its value by 1, so finally we got frequency of all letter present in string.
            # Here as per first condition we will increase the frequnecy by one if the character is already present in the 
            # dictionary                                            
            if char in letter_occurrence:
                letter_occurrence[char] = letter_occurrence[char] + 1
            # Here condition if letter is seen first time
            else:
                letter_occurrence[char] = 1
        # Here finally return the dictionary which contain all letter with their freequency as key,value pair (letter as key and frequency as value)
        return letter_occurrence
        

# Here letter occurence is the dictionary which we passed as obtained from letter_distribution which contain all letter with their freequency as key value pair.
def node_reducer(letter_occurrence_dictionary):                   
        '''This function takes a dictionary which contains character as key and their freuquency in original_string as value and returns a nested list which represents huffmann tree.'''
        # Here we use sorted list since in huffman tree we need value in sorted order and this sorted list store value in non decreasing order.
        node_list = sc.SortedList()
        # First we will add all letter and their frequencies as tuples in sorted list i.e. node_list.
        for char in letter_occurrence_dictionary:                  
                node_list.add((letter_occurrence_dictionary[char], char ,char))
        
        # Now we will start reducing number of nodes , basically by merging the two nodes with smallest freequency , then next two with smallest frequency and so on
        # till all merges or basically we reach to parent node. So we will end the loop when we left with only one node i.e the parent node.
        # Here we start loop that start merging, since we already have sorted list so we have to just pick the first two tuples, merge them and then pop the two 
        # tuple we have taken and so on till the length of node_list reduces to 1, i.e., when we left with only one node in huffman tree.
        while len(node_list) != 1:
                # Here we will store first two tuple in a and b respectively
                a = node_list[0]
                b = node_list[1]
                # Now we will remove both these tuple from the list which have least freequency
                node_list.pop(0)
                node_list.pop(0)
                # Here we will add frequencies of two nodes and also insert the new frequency and their elements in a tuple. Then we will insert that tuple as a node in # 'node_list'. We have already removed the two nodes that we have used.
                node_list.add((a[0]+b[0], a[1], [a[2],b[2]]))
        # Finally we return the nested list which represent the huffman tree.
        return node_list[0][2]


# Now we will make a dictionary 'code_dict' in which we will store characters and their huffman code.
global code_dict
code_dict = {}
def code_assigner(nested_list, index):
        '''This function takes a nested list 'nested_list' as input and assign each character in it a huffman code. As we have taken nodes in non decreasing order frequency, it will assign smaller code to the character having more frequency which results in reduction of size of string.'''
        # If there is only one type of character present in a string then simply we will assign it any 1 unit bit, i.e., 0 or 1. In this case we have assigned it as 1.
        if len(nested_list) == 1:
                return {nested_list[0] : '1'}
        # If it is not so, then we will use recursion in the following manner to assign characters their huffman codes.
        else:
                # First we will check for first element of a nested list.
                # If first element is list we will again apply recursion on it.
                if type(nested_list[0]) == list:
                        code_assigner(nested_list[0], index + '0')
                # If it is not a list then we will insert that character in 'code_dict' and assign that character a huffman code, i.e., its index in nested list.
                else:
                        code_dict[nested_list[0]] = index + '0'

                # Now we will check for seocnd element of a nested list.
                # If first element is list we have to send this list again by recursion but this time we start assigning from 1 since we are checking first index list
                # in nested list
                if type(nested_list[1]) == list:
                        code_assigner(nested_list[1], index + '1')
                # If it is not a list then we will take that character and assign that a huffman code, i.e., its index in nested list.
                else:
                        code_dict[nested_list[1]] = index + '1'
                # Here finally we will return the dictionary containing character and their corresponding huffman code, i.e., there index in nested list.
                return code_dict


def huffman_code(original_string):
        '''In this function we will merge all above functions to which takes a string 'original_string' as a input and returns a dictionary wihch contains character present in the 'original_string' and their huffman codes.'''
        # Here first creating dictionary with the string given as input by calling function letter_distribution
        letter_occurrence_dictionary = letter_distribution(original_string)
        # Now we will create a list named as 'node_reduced_list' containing one node which is obtained by the algo described above, which represent the tree . Then we will use that obtained nested list to assign code to characters in 'original_string'.
        node_reduced_list = node_reducer(letter_occurrence_dictionary)
        # Initially we will assign no value to index.
        index = ""
        # Now finally we will create dictionary with letter and their corresponding huffman code.
        char_code = code_assigner(node_reduced_list, index)
        # Here finally we will return a dictionary which is basically a chart which will be used for decoding and also for encoding.
        return char_code


def huffman_encoding(original_string):
        '''This function returns encoded string of 'original_string' as per obtained huffman codes.'''
        # Here we will first initialize the 'encoded_string' which represent the output string .
        encoded_string = ""
        # This is the dictionary containing huffman code of characters in 'original_string'.
        char_code = huffman_code(original_string)
        # Here we will replace characters in 'original_string' with their corresponding huffman codes.
        for char in original_string:
                encoded_string = encoded_string + char_code[char]
        # Here finally we will return the encoded string.
        return encoded_string


def bits_without_encoding(original_string):
        '''This function returns how many number of bits input string will take.'''
        # As each character takes 8 bits or 1 byte, total size taken by the string will be 8 times of its length. (Here we have assumed that string contains character whose UTF-8 encoding uses less than 8 bits)
        return f"{len(original_string)*8} bits"


def bits_after_encoding(original_string):
        '''This function returns how many number of bits a string will take after encoding it using huffman coding.'''
        # Here we will create a variable 'count' where we will store sum of length of huufman codes assign to the characters. First we will initialize count as 0.
        count = 0
        # We will traverse over whole dictionary and add length of values i.e., huffman codes to count.
        for char in huffman_code(original_string):
                count = count + len(huffman_code(original_string)[char])
        # Total size of file(in bits) will be given by 8 times number of distinct character in string + count + length of encoded string.
        return f"{len(huffman_code(original_string))*8 + count + len(huffman_encoding(original_string))} bits"

#Time complexity of huffman coding is NlogN which can be clearly seen from this program also.

f = open("input.txt", 'r')
s = f.read()
f.close()

f = open('output.txt', 'r+')
f.truncate(0)
f.close()

f = open("output.txt", 'a')
f.write("huffman code for all distinct characters in string is " + str(code_assigner(node_reducer(letter_distribution(s)), "")) + "\n" + "\n")
f.write("encoded string is " + str(huffman_encoding(s)) + "\n" + "\n")
f.write("bits without encoding " + str(bits_without_encoding(s)) + "\n" + "\n")
f.write("bits after encoding " +str(bits_after_encoding(s)) + "\n" + "\n")
f.close()

