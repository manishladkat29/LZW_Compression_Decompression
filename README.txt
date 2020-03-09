Name: Manish Ladkat
Student Id: 801167905
Programming Project 1: LZW Compression

Description: This is an implementation of the LZW algorithm in python to compress and decompress the data in the files.
The algorithm is split into two parts compression and decompression and written in the Compression.py and Decompression.py respectively.
The dictionary data structure of python has been used to store the data, and the pack and unpack function from the struct library is
used to convert the integer data to 16-bit or 2 bytes data and vice versa respectively.

Files break down:
1. Compression.py : The file implements the LZW compression algorithm in python where the input is read from the text file the data is compressed using the algorithm and stored in a binary .lzw file in 16 bit UTF-16BE format.
2. Decompression.py : The file implements the LZW decompression algorithm in python where the input is a compressed data which is read from the .lzw file and the algrotihm converts it to the decompressed/original file again.
3. README.txt

Summary:
The implementation works well for both the compression and decompression of the data and gets the desired output for the examples provided on canvas.
The compression generates a inputfilename.lzw file which has the compressed data for the inputfilename.txt file which was passed as an argument along with the number of bits.
The decompression file takes the inputfilename.lzw file and number of bits as the input and decompresses to give the output same as that in inputfilename.txt file in the inputfilename_decoded.txt file.
The compression works well for the data having repeating values, if the input data does not have repeating values the compressed/encoded file will have data similar as the input file.

Programming Language: Python

Compiler Version: Python 3.7

How to run the file:
1. Open the command prompt.
2. Set the current working directory to the location where the files are present.
3. Copy the input file to the current working directory.
4. To compress data type command on terminal => python Compression.py inputFileName.txt number_of_bits
   e.g. : python Compression.py input1.txt 12
   The compressed file will be stored as input1.lzw in the current working directory
5. To decompress data type command on terminal => python Decompression.py inputFileName.lzw number_of_bits
   e.g. : python Decompression.py input1.lzw 12
   The decompressed file will be stored as input1_decoded.txt in the current working directory