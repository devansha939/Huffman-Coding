# First we import this library because we need sorrted list which is stored in sorted container
import sortedcontainers as sc
# Here initialising the sorted list which store the tuple of code as key and character as value in sorted order(and sort on bases of key that is code).
global code_char
code_char = sc.SortedList()
# Here intialising dictionary which store the chart of code that are assigned from encoding part
def dict_to_list(freq_dict):
        '''This function takes a dictionary 'freq_dict' which contains charcter and their corresponding codes.'''
        # Now we will travers over whole dictionary and add the tuple which contains huffman code and character to the sorted_list.
        for char in freq_dict:
                code_char.add((freq_dict[char],char))
        return code_char


# This is code for searching the codes of input string using binary search technique, we are able to use this since the list is in sorted order.
def binary_search(x, L):
        ''' This function return the tuple in which first element denote whether the the code is present or not, if present in tuple first value is 1 and second value is the character corresponding to that code.'''
        # NOw we will intiallise the boolean value which is 1 when we got code and 0 when we don't get . Let intitally starts with 0.
        flag =  0
        # This loop is for traversing in the whole list.
        while(len(L) != 0):
            # If middle element is greater than the element to be search, then we will remove second half list.
            if(L[(len(L)//2)][0]>x):       
                L = L[:(len(L)//2)]
            # If middle element is equal to the element to be search, then we will set flag as one and will break the loop. It should be noticed that if the element is 
            # present and size of list is 1 then that element should be equal to given number in order to meet requirements.
            elif(L[(len(L)//2)][0] == x): 
                flag = 1
                break
            # If middle element is smaller than the element to be search, then we will remove first half list.
            else:
                L = L[(len(L)//2)+1:]
        # Now if we don't get the code and flag's value is zero so return the tuple (0,0) in which first 0 represent we don't get  any code . 
        if flag == 0:
                return (0, 0)
        # Now if we get the code so it return a tuple in which first value is 1 which represent we get code and second value represent the char which represent that code. 
        else:
                return (1, L[(len(L)//2)][1])

#this is main function which decode our message to original message
def huffman_decoding(s_encoded, freq_dict):
        '''this function finally return the original message which user sent using the chart which contain information about the code assign to each char'''
        # Here we will initialise a string which store the decoded message and finally we will return this string
        s_decoded = ""
        # Here initialising the iterator which is use to traverse in the whole encoded string
        i = 0
        # Here initialising an empty string which is use to pass in binary search function which search for that string in list and if we got that string in the list we 
        # made this string empty.
        s = ""
        #here is the loop for traversing in the encoded string
        while(i < len(s_encoded)):
                # Here we start taking part of encoded string and store it in 's' so that whenever we get that code we have to return that char which represent that code
                s = s + s_encoded[i]
                # Now we will store all distinct characters and their corresponding Huffman codes in the sorted list L as tuple.
                L = dict_to_list(freq_dict)
                # Here we will store the tuple obtain from binary search function
                t = binary_search(s, L)
                # Now we have to check what is tuple first value, if it is 1 that means that s is a valid huffman code. If it is so we will add character corresponding to that code in 'encoded_string'. Also we will set 's' as empty string.
                if t[0] == 1:
                        # Here we will add that character corresponding to the code we get in string.
                        s_decoded = s_decoded + t[1]
                        # Now make the string s empty which store the code
                        s = ""
                # Here we will update the iterator
                i = i + 1
        # Here finally we will return the decoded string.
        return s_decoded