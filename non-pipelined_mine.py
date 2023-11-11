machine_code = [
    "00100000000110000000000000000000",
    "00100000000100110000000000000001",
    "00010011000010010000000000010000",
    "00100000000101110000000000000001",
    "00100001010101000000000000000100",
    "00010010111010010000000000001011",
    "00100010100011011111111111111100",
    "10001101101011000000000000000000",
    "00100010100011100000000000000000",
    "10001101110011110000000000000000",
    "00000001100011111100100000101010",
    "00010011001100110000000000000010",
    "10101101110011000000000000000000",
    "10101101101011110000000000000000",
    "00100010111101110000000000000001",
    "00100010100101000000000000000100",
    "00001000000100000000000000100010",
    "00100011000110000000000000000001",
    "00001000000100000000000000010101",
    "00100001010101000000000000000000",
    "00100001011100110000000000000000",
    "00100000000101110000000000000000",
    "00010010111010010000000000001100",
    "10001110100110000000000000000000",
    "10101110011110000000000000000000",
    "00100010111101110000000000000001",
    "00100010100101000000000000000100",
    "00100010011100110000000000000100",
    "00001000000100000000000000101001"
]

#reg_dict stores 5 bit binary values for registers
reg_dict = {"'$s3'": "10011", "'$s4'" : "10100", "'$s7'": "10111", "'$t1'": "01001", "'$t2'" : "01010", "'$t3'" : "01011", "'$t4'" : "01100", "'$t5'" : "01101", "'$t6'" : "01110", "'$t7'" : "01111", "'$t8'" : "11000", "'$t9'" : "11001", "'$zero'" : "00000"}
#opcode_dict stores 6 bit binary values for the functions
opcode_dict = {"'addi'" : "001000", "'beq'" : "000100", "'lw'" : "100011", "'sw'" : "101011", "'slt'" : "000000", "'j'" : "000010"}
#immediate_dict stores 16 bit binary values for all immediate values used in the program
immediate_dict = {"'loopOuterEnd'" : "0000000000010000", "'loopInnerEnd'" : "0000000000001011", "'loop2end'" : "0000000000001100", "'else'" : "0000000000000010", "'0'" : "0000000000000000", "'1'" : "0000000000000001", "'4'" : "0000000000000100", "'-4'" : "1111111111111100"}
#funct_dict stores 6 bit binary values for the funct field in R type instructions
funct_dict = {"'slt'" : "101010"}
#address_dict stores 32 bit binary values of the addresses of jump instructions
address_dict = {"'loopInner'" : "00000000010000000000000010001000", "'loopOuter'" : "00000000010000000000000001010100", "'loop2'" : "00000000010000000000000010100100"}

word_list = []	#this will contain lists of each word of an instruction(wont include commas and spaces)(word_list[i] = ith instruction as a list with its elements as word strings)

# Create a new dictionary with swapped keys and values for reg_dict
reg_dict_swapped = {value: key for key, value in reg_dict.items()}

# Create a new dictionary with swapped keys and values for opcode_dict
opcode_dict_swapped = {value: key for key, value in opcode_dict.items()}

# Create a new dictionary with swapped keys and values for immediate_dict
immediate_dict_swapped = {value: key for key, value in immediate_dict.items()}

# Create a new dictionary with swapped keys and values for funct_dict
funct_dict_swapped = {value: key for key, value in funct_dict.items()}

# Create a new dictionary with swapped keys and values for address_dict
address_dict_swapped = {value: key for key, value in address_dict.items()}

# print("reg_dict_swapped:")
# print(reg_dict_swapped)
# print("\nopcode_dict_swapped:")
# print(opcode_dict_swapped)
# print("\nimmediate_dict_swapped:")
# print(immediate_dict_swapped)
# print("\nfunct_dict_swapped:")
# print(funct_dict_swapped)
# print("\naddress_dict_swapped:")
# print(address_dict_swapped)

reg_dict = {"'$s3'": 0b00000000000000000000000000000000, "'$s4'" : 0b00000000000000000000000000000000, "'$s7'": 0b00000000000000000000000000000000, "'$t1'": 0b00000000000000000000000000000000, "'$t2'" : 0b00010000000000010000000011000000, "'$t3'" : 0b00000000000000000000000000000000, "'$zero'" : 0b00000000000000000000000000000000}

def IF(PC):
    return machine_code[PC]

def ID(instruction):
    return opcode_dict_swapped[f"'{instruction[0:6]}'"]

def EX():

