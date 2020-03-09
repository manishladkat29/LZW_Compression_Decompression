# Name: Manish Ladkat
# ID : 801167905

from struct import unpack
from sys import argv

INIT_CHARS_LENGTH = 256
if len(argv) != 3:
    print("You should pass 2 arguments inputfilename and bit length to run the program")
    print("File not decoded!")
    exit(0)
input_file_name, N = argv[1:]  # Store the argument values
if not str(input_file_name).endswith(".lzw"):
    print("The input file should be a .lzw extension file")
    exit(0)
if int(N) <= 8 or int(N) > 16:
    print("The bit length should be usually in the range of 9 to 16 inclusive\n File not decoded!")
    exit(0)
max_table_size = 2 ** int(N)  # N is number of encoding bits
dictionary_codes = {}

# Store the characters to its corresponding ascii values in the dictionary
for i in range(INIT_CHARS_LENGTH):
    dictionary_codes[i] = chr(i)

dictionary_pointer = INIT_CHARS_LENGTH  # Set the dictionary pointer to 256

# Open the input file in read binary mode and output file in write mode
output_file_name = input_file_name.split(".")[0]
output_file = open(output_file_name + "_decoded.txt", "w")
input_file = open(input_file_name, 'rb')

# Read and decode the first 16 bit value and write the character to the output file
data = input_file.read(2)
(code,) = unpack('>H', data)  # Decode the the data read and store it to code variable
print("CODE: " + str(code), end=' ; ')
string = dictionary_codes[code]
output_file.write(string)
print("OUTPUT: " + string, end=' ; ')
print("STRING: " + string)

# While loop to read 16 bit value and write the decoded data to the output file
while True:
    data = input_file.read(2)
    if len(data) == 2:
        (code,) = unpack('>H', data)
        print("CODE: " + str(code), end=' ; ')
        if code not in dictionary_codes:  # If the code is not in dictionary then form a new_string
            print("TABLE CODE DEFINED: N", end=' ; ')
            new_string = string + string[0]
        else:  # Else assign the value to the corresponding code to the new string
            print("TABLE CODE DEFINED: Y", end=' ; ')
            new_string = dictionary_codes[code]
        print("NEW_STRING: " + new_string, end=' ; ')
        if len(dictionary_codes) < max_table_size:  # check if table is not full
            dictionary_codes[dictionary_pointer] = string + new_string[0]
            print("TABLE UPDATE: " + str(dictionary_pointer) + " : " + dictionary_codes[dictionary_pointer],
                  end=' ; ')
            dictionary_pointer += 1
        output_file.write(new_string)  # write the new string to the output file
        print("OUTPUT: " + new_string, end=' ; ')
        string = new_string
        print("STRING: " + string)
    else:
        break

# Close the opened files
input_file.close()
output_file.close()
