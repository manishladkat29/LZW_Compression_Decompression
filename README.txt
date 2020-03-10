Name: Manish Ladkat
Student Id: 801167905
Programming Project 1: LZW Compression and Decompression

Description: This is an implementation of the LZW algorithm in python to compress and decompress the data in the files.
The algorithm is split into two parts compression and decompression and written in the Compression.py and Decompression.py respectively.
The dictionary data structure of python has been used to store the data, and the pack and unpack function from the struct library is
used to convert the integer data to 16-bit or 2 bytes data and vice versa respectively.

Files break down:
1. Compression.py - The file takes an input from .txt file uses the dictionary data structure and then encodes it and writes it back to the .lzw file in the UTF-16BE encoding format.
2. Decompression.py - The file takes the input from a .lzw file which which is encoded converts it back to integer and then decodes it to get the orginal result and writes it back to the _decoded.txt file.

Summary:
The implementation works well for both the compression and decompression of the data and gets the desired output for the examples provided on canvas.
The compression works well for the data having repeating values, if the input data does not have repeating values the compressed/encoded file will have data similar as the input file.
The compression generates a inputfilename.lzw file which has the compressed data for the inputfilename.txt file which was passed as an argument along with the number of bits.
The decompression file takes the inputfilename.lzw file and number of bits as the input and decompresses to give the output same as that in inputfilename.txt file in the inputfilename_decoded.txt file.

Programming Language: Python

Compiler Version: Python 3.7

How to run the file:
1. Open the command prompt.
2. Set the current working directory to the location where the files are present.
3. Copy the input file to the current working directory.
4. To compress data type command on terminal => python Compression.py inputFileName.txt number_of_bits
e.g. : python Compression.py input1.txt 12
The compressed file will be stored as input1.lzw in the current working directory
Note: The inputfile should have .txt extension and the bit length should be in the range 9 to 16 inclusive
5. To decompress data type command on terminal => python Decompression.py inputFileName.lzw number_of_bits
e.g. : python Decompression.py input1.lzw 12
The decompressed file will be stored as input1_decoded.txt in the current working directory
Note: The inputfile should have .lzw extension and the bit length should be in the range 9 to 16 inclusive