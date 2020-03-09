# Name: Manish Ladkat
# ID : 801167905

from struct import pack
from sys import argv

INIT_CHARS_LENGTH = 256
if len(argv) != 3:
    print("You should pass 2 arguments inputfilename and bit length to run the program")
    print("File not decoded!")
    exit(0)
input_file_name, N = argv[1:]  # Store the argument values
if not str(input_file_name).endswith(".txt"):
    print("The input file should be a .txt extension file")
    exit(0)
if int(N) <= 8 or int(N) > 16:
    print("The bit length should be usually in the range of 9 to 16 inclusive\n File not decoded!")
    exit(0)
max_table_size = 2 ** int(N)  # N is number of encoding bits
dictionary = {}

# Store the character and their corresponding ascii value in dictionary
for i in range(INIT_CHARS_LENGTH):
    dictionary[chr(i)] = i

dictionary_pointer = INIT_CHARS_LENGTH  # Initialize the dictionary pointer to 256
string = ""

# Open and read the input file
input_file = open(input_file_name)
data_read = input_file.read()

# Open the output file to store encoded data with .lzw extension in binary write mode
output_file_name = input_file_name.split(".")[0]
output_file = open(output_file_name + ".lzw", "wb")

# while loop to retrieve the data and write the output in encoded format to the output file
cnt = 0
symbol = ""
while cnt < len(data_read):  # the for loop will run until the data is present
    symbol = data_read[cnt]
    print("STRING: " + string + ", SYMBOL: " + symbol + ", STRING + SYMBOL: " + string + symbol, end=' ; ')
    if string + symbol in dictionary:
        print("STRING+SYMBOL in TABLE? : Y")
        string = string + symbol
    else:
        print("STRING+SYMBOL in TABLE? : N", end=' ; ')
        # Write the encoded unsigned short output in the big endian format to the output file
        output_file.write(pack('>H', int(dictionary[string])))
        print("OUTPUT: " + str(dictionary[string]), end=' ; ')
        if len(dictionary) < max_table_size:  # check if table is not full
            print("TABLE UPDATE: " + str(dictionary_pointer))
            # Store the value of the newly formed string to the dictionary
            dictionary[string + symbol] = dictionary_pointer
            dictionary_pointer += 1
        string = symbol
    cnt += 1
input_file.close()  # Close the input file
# Write the value of the last remaining string in the encoded format to the output file
if string in dictionary:
    print("STRING: " + string + ", SYMBOL: " + symbol + ", STRING + SYMBOL: " + string + symbol, end=' ; ')
    print("STRING+SYMBOL in TABLE? : Y", end=' ; ')
    print("OUTPUT: " + str(dictionary[string]))
    output_file.write(pack('>H', int(dictionary[string])))
output_file.close()  # Close the output file
