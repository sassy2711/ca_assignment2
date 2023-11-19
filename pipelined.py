from collections import deque
main_memory={
    268501184:13,
    268501188:2,
    268501192:7,
    268501196:53,
    268501200:5,
    
    268501216:0,
    268501220:0,
    268501224:0,
    268501228:0,
    268501232:0,
}
Register_File=[0]*31
Register_File[9]=5
Register_File[10]=268501184
Register_File[11]=268501216
x={
4194380:"00100000000110000000000000000000",
4194384:"00100000000100110000000000000001",
4194388:"00010011000010010000000000010000",
4194392:"00100000000101110000000000000001",
4194396:"00100001010101000000000000000100",
4194400:"00010010111010010000000000001011",
4194404:"00100010100011011111111111111100",
4194408:"10001101101011000000000000000000",
4194412:"00100010100011100000000000000000",
4194416:"10001101110011110000000000000000",
4194420:"00000001100011111100100000101010",
4194424:"00010011001100110000000000000010",
4194428:"10101101110011000000000000000000",
4194432:"10101101101011110000000000000000",
4194436:"00100010111101110000000000000001",
4194440:"00100010100101000000000000000100",
4194444:"00001000000100000000000000011000",
4194448:"00100011000110000000000000000001",
4194452:"00001000000100000000000000010101",
4194456:"00100001010101000000000000000000",
4194460:"00100001011100110000000000000000",
4194464:"00100000000101110000000000000000",
4194468:"00010010111010010000000000001100",
4194472:"10001110100110000000000000000000",
4194476:"10101110011110000000000000000000",
4194480:"00100010111101110000000000000001",
4194484:"00100010100101000000000000000100",
4194488:"00100010011100110000000000000100",
4194492:"00001000000100000000000000101001"
}
#reg_dict stores 5 bit binary values for registers

#opcode_dict stores 6 bit binary values for the functions
opcode_dict = { "001000":"'addi'",  "000100": "'beq'",   "100011":"'lw'",  "101011":"'sw'" ,  "000000":"'slt'" ,  "000010":"'j'" }
#immediate_dict stores 16 bit binary values for all immediate values used in the program
immediate_dict = {"'loopOuterEnd'" : "0000000000010000", "'loopInnerEnd'" : "0000000000001011", "'loop2end'" : "0000000000001100", "'else'" : "0000000000000010", "'0'" : "0000000000000000", "'1'" : "0000000000000001", "'4'" : "0000000000000100", "'-4'" : "1111111111111100"}
#funct_dict stores 6 bit binary values for the funct field in R type instructions
funct_dict = {"'slt'" : "101010"}
#address_dict stores 32 bit binary values of the addresses of jump instructions
address_dict = {"'loopInner'" : "00000000010000000000000010001000", "'loopOuter'" : "00000000010000000000000001010100", "'loop2'" : "00000000010000000000000010100100"}



Register_dict={
"00000":0,
"00001":1,
"00010":2,
"00011":3,
"00100":4,
"00101":5,
"00110":6,
"00111":7,
"01000":8,
"01001":9,
"01010":10,
"01011":11,
"01100":12,
"01101":13,
"01110":14,
"01111":15,
"10000":16,
"10001":17,
"10010":18,
"10011":19,
"10100":20,
"10101":21,
"10110":22,
"10111":23,
"11000":24,
"11001":25,
"11010":26,
"11011":27,
"11100":28,
"11101":29,
"11110":30,
"11111":31
}

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

def jump_converter(a):
    x=0
    y=2**(len(a)-1)
    for i in a:
        x=x+(int(i)*(y))
        y=y/2
    return int(x)
    
def binary_string_to_decimal(a):
    x=0
    y=2**(len(a)-1)
    if(a[0]=="0"):
        for i in a:
            x=x+(int(i)*(y))
            y=y/2
        return int(x)
    else:
        for i in a:
            x=x+(abs(int(i)-1)*(y))
            y=y/2
        
        return -(int(x)+1)
    
def IF():
    global PC
    if(PC<=4194492 and PC>=4194380):
        instruction= x[PC]
    else:
        instruction= -1
    PC=PC+4
    return instruction
    

def ID(instruction):
    global PC
    if(instruction != -1):
        opcode=instruction[0:6]
        b={}
        b["flag"] = 0
        if(opcode in ["000000"]):   #slt
            b["instruction type"]='R'
            b["opcode"]=opcode
            b["rs value"]=Register_File[Register_dict[instruction[6:11]]]
            b["rt value"]=Register_File[Register_dict[instruction[11:16]]]
            b["rd"]=Register_dict[instruction[16:21]]
            b["shamt"]=0
            b["function"]=instruction[26:]
            b["rs"]=Register_dict[instruction[6:11]]
            b["rt"]=Register_dict[instruction[11:16]]
        elif(opcode  in ["001000","100011"]):  #addi,lw,
            b["instruction type"]='I'
            b["opcode"]=opcode
            b["rs value"]=Register_File[Register_dict[instruction[6:11]]]
            b["rt"]=Register_dict[instruction[11:16]]      #b[3]=rt
            b["immediate"]=binary_string_to_decimal(instruction[16:])
            b["rs"]=Register_dict[instruction[6:11]]       #b[7]=rs
        elif(opcode == "101011"):        #sw
            b["instruction type"]='I'
            b["opcode"]=opcode
            b["rs value"]=Register_File[Register_dict[instruction[6:11]]]
            b["rt value"]=Register_File[Register_dict[instruction[11:16]]]
            b["immediate"]=binary_string_to_decimal(instruction[16:])
            b["rs"]=Register_dict[instruction[6:11]]       #b[5]=rs
            b["rt"]=Register_dict[instruction[11:16]]      #b[7]=rt
        elif(opcode=="000100"):     #beq
            b["flag"] = 1
            b["instruction type"]='I'
            b["opcode"]=opcode
            b["rs"]=Register_dict[instruction[6:11]]   #b[2]=rs
            b["rt"]=Register_dict[instruction[11:16]]  #b[3]=rt
            #print(Register_File[Register_dict[instruction[6:11]]],Register_File[Register_dict[instruction[11:16]]])
            if(Register_File[Register_dict[instruction[6:11]]]==Register_File[Register_dict[instruction[11:16]]]):
                PC=int(PC+(binary_string_to_decimal(instruction[16:])*4))
        
        elif(opcode  in ["000010"]): #j
            b["flag"] = 1
            b["instruction type"]='J'
            b["opcode"]=opcode
            PC = int(binary_string_to_decimal(instruction[6:])*4)
        
    else:
        b={}
    return b
    
def EX(b):
    global PC
    out_execute={}
    out_execute["instruction type"]=b["instruction type"]
    out_execute["opcode"]=b["opcode"]
    
    if(b["instruction type"]=='J'):
        if(b["opcode"]=="000010"):
            out_execute["flag"]=-1       #skip mem read and writeback
    elif(b["instruction type"]=='R'):
        out_execute["rd"]=b["rd"]
        out_execute["rt"]=b["rt"]
        out_execute["rs"]=b["rs"]
        if(b["function"]=="101010"):
            out_execute["flag"]=0   #skip mem read ,do writeback only

            
            if b["rs value"]<b["rt value"]:
                out_execute["output"]=1
                
            else:
                out_execute["output"]=0
                
    elif(b["instruction type"]=='I'):
        out_execute["rt"]=b["rt"]
        out_execute["rs"]=b["rs"]
        if(b["opcode"]=="001000"):     #addi
            out_execute["flag"]=0
            
            out_execute["output"]=(b["rs value"]+b["immediate"])
            
        elif(b["opcode"]=="100011"):     #lw
            out_execute["flag"]=1    #have to do mem read and writeback both
            #print(b["rs value"],b["immediate"])
            out_execute["output"]=(b["rs value"]+b["immediate"])
        elif(b["opcode"]=="101011"): #sw
            out_execute["flag"]=2       #have to store in memory no  writeback
            out_execute["rt value"]=b["rt value"]
            out_execute["output"]=(b["rs value"]+b["immediate"])
        elif(b["opcode"]=="000100"):   #beq
            out_execute["flag"]=-1
            
    return out_execute

def MEM(out_execute):
    global PC
    Mem_out={}
    Mem_out["instruction type"]=out_execute["instruction type"]
    Mem_out["opcode"]=out_execute["opcode"]
    if(out_execute["instruction type"]=='I'):
        Mem_out["rs"]=out_execute["rs"]
        Mem_out["rt"]=out_execute["rt"]
    if(out_execute["instruction type"]=='R'):
        Mem_out["rd"]=out_execute["rd"]
        Mem_out["rs"]=out_execute["rs"]
        Mem_out["rt"]=out_execute["rt"]
    if(out_execute["flag"]==-1):    #no memory access,no writeback 
        Mem_out["flag"]=-1          #no writeback
    if(out_execute["flag"]==0):      #no memory access,do writeback
        Mem_out["flag"]=1           #do writeback
        Mem_out["output"]=out_execute["output"]
    if(out_execute["flag"]==1):  #lw         do memory access ,do writeback
        Mem_out["flag"]=1
        Mem_out["output"]=main_memory[out_execute["output"]]
    if(out_execute["flag"]==2):      #sw            do memory access,no writeback
        Mem_out["flag"]=-1
        main_memory[out_execute["output"]]=out_execute["rt value"]
    return Mem_out

def WB(Mem_out):
    global PC
    
    if(Mem_out["flag"]==-1):
        return 
    elif(Mem_out["flag"]==1): 
        if(Mem_out["instruction type"]=="R"):  
            Register_File[Mem_out["rd"]]=Mem_out["output"]
        else:
            Register_File[Mem_out["rt"]]=Mem_out["output"]
        return
        
# def Cycle():
#     global PC
#     instruction=IF()
#     b=ID(instruction)
#     out_execute=EX(b)
#     Mem_out=MEM(out_execute)
#     WB(Mem_out)
#     #print(PC)
#     #PC=PC+4
#     #print(PC)
    

# while(PC<=4194492):
#     Cycle()
    

# for i in range(268501216,268501233,4):
#     print(main_memory[i])

global PC
PC=4194380

def pipeline():
    global IF_ID
    global ID_EX
    global EX_MEM
    global MEM_WB
    global PC
    global instruction
    global b
    global out_execute
    global Mem_out
    global instructions_in_pipeline
    instructions_in_pipeline = deque()
    EX_MEM = None
    while(PC<=4194496):
        rs_flag = 0
        rt_flag = 0
        lw_flag = 0
        instructions_in_pipeline.appendleft(PC)
        for i in range(len(instructions_in_pipeline)):
            if(i == 0):
                IF_ID = IF()
            elif(i == 1):
                ID_EX = ID(IF_ID)
                if(EX_MEM != None):
                    #print(EX_MEM["flag"])
                    if(ID_EX["flag"] != 1):
                        if (EX_MEM["instruction type"] == "R"):
                            if(ID_EX["rs"] == EX_MEM["rd"]):
                                rs_flag = 1
                            elif(ID_EX["rt"] == EX_MEM["rd"]):
                                rt_flag = 1
                        elif (EX_MEM["instruction type"] == "I"):
                            if (opcode_dict_swapped[ID_EX["opcode"]] == "lw"):
                                lw_flag = 1
                            if(ID_EX["rs"] == EX_MEM["rt"]):
                                rs_flag = 1
                #print([rs_flag, rt_flag, lw_flag])
            elif(i == 2):
                EX_MEM = EX(ID_EX)
            elif(i == 3):
                #print(EX_MEM) 
                if (rs_flag == 1 and lw_flag == 0):
                    Register_File[ID_EX["rs"]] = EX_MEM["output"]
                elif (rt_flag == 1 and lw_flag == 0):
                    Register_File[ID_EX["rt"]] = EX_MEM["output"]
                MEM_WB = MEM(EX_MEM)
                if (rs_flag == 1 and lw_flag == 1):
                    Register_File[ID_EX["rs"]] = MEM_WB["output"]
                elif (rt_flag == 1 and lw_flag == 1):
                    Register_File[ID_EX["rt"]] = MEM_WB["output"]
            elif(i == 4):
                WB(MEM_WB)

        if(len(instructions_in_pipeline) == 5):
            instructions_in_pipeline.pop()
        if(len(instructions_in_pipeline) == 0):
            break
        
pipeline()
