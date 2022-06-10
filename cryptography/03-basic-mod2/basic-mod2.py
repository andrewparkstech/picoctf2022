# variables
alphanum = []
decode = []
final = ''

# build required character lists

# add capital letters
for i in range(65,91):
    alphanum.append(chr(i))

# add numbers 0 to 9
for i in range(10):
    alphanum.append(str(i))

# add underscore
alphanum.append('_')

# # debug: print alphanum
# print('alphanum[]')
# print(alphanum)
# print(len(alphanum))


# read message.txt into a list
numlist = open('message.txt','r').read().split()

# # debug: print number list
# print('numlist[]')
# print(numlist)

# loop thru each number and perform required operation
for num in numlist:
    decode.append(pow(int(num),-1,41))

# # debug: print decode
# print('decode[]')
# print(decode)


# loop thru numbers and pull corresponding char from alphanum list
for num in decode:
    # subtracting 1 because our alpha list is zero-based, whereas the requirements for decoding is one-based
    final += alphanum[num - 1]

print('picoCTF{'+final+'}')
