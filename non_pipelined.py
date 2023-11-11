#x=list(input().split("\n"))
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
   
    return instruction
    

def ID(instruction):
    global PC
    if(instruction != -1):
        opcode=instruction[0:6]
        b=[0]*7
        if(opcode in ["000000"]):   #slt
            b[0]='R'
            b[1]=opcode
            b[2]=Register_File[Register_dict[instruction[6:11]]]
            b[3]=Register_File[Register_dict[instruction[11:16]]]
            b[4]=Register_dict[instruction[16:21]]
            b[5]=0
            b[6]=instruction[26:]
        elif(opcode  in ["001000","100011"]):  #addi,lw,
            b[0]='I'
            b[1]=opcode
            b[2]=Register_File[Register_dict[instruction[6:11]]]
            b[3]=Register_dict[instruction[11:16]]
            b[4]=binary_string_to_decimal(instruction[16:])
        elif(opcode in ["101011","000100"]):        #sw,beq
            b[0]='I'
            b[1]=opcode
            b[2]=Register_File[Register_dict[instruction[6:11]]]
            b[3]=Register_File[Register_dict[instruction[11:16]]]
            b[4]=binary_string_to_decimal(instruction[16:])
        elif(opcode  in ["000010"]): #j
            b[0]='J'
            b[1]=opcode
            b[2]=instruction[6:]
        
    else:
        b=[]
    return b
    
def EX(b):
    global PC
    out_execute=[0]*2
    if(b[0]=='J'):
        if(b[1]=="000010"):
            PC = int(binary_string_to_decimal(b[2])*4-4)
            out_execute[0]=-1       #skip mem read and writeback
    elif(b[0]=='R'):
        if(b[6]=="101010"):
            out_execute[0]=0        #skip mem read ,writeback only
            if b[2]<b[3]:
                out_execute[1]=[b[4],1]
            else:
                out_execute[1]=[b[4],0]
    elif(b[0]=='I'):
        if(b[1]=="001000"):     #addi
            out_execute[0]=0
            
            out_execute[1]=[b[3],(b[2]+b[4])]
        elif(b[1]=="100011"):     #lw
            out_execute[0]=1    #have to do mem read and writeback
            
            out_execute[1]=[b[3],(b[2]+b[4])]
        elif(b[1]=="101011"): #sw
            out_execute[0]=2       #have to store in memory no  writeback
            out_execute[1]=[b[3],(b[2]+b[4])]
        elif(b[1]=="000100"):   #beq
            out_execute[0]=-1
            if(b[2]==b[3]):
                PC=int(PC+(b[4]*4))
    return out_execute

def MEM(out_execute):
    global PC
    Mem_out=[0]*2
    if(out_execute[0]==-1):
        Mem_out[0]=-1
    if(out_execute[0]==0):
        Mem_out[0]=1
        Mem_out[1]=out_execute[1]
    if(out_execute[0]==1):
        Mem_out[0]=1
        Mem_out[1]=[out_execute[1][0],main_memory[out_execute[1][1]]]
    if(out_execute[0]==2):
        Mem_out[0]=-1
        main_memory[out_execute[1][1]]=out_execute[1][0]
    return Mem_out

def WB(Mem_out):
    global PC
    if(Mem_out[0]==-1):
        return 
    elif(Mem_out[0]==1):   
        Register_File[Mem_out[1][0]]=Mem_out[1][1]
        return
        
def Cycle():
    global PC
    instruction=IF()
    b=ID(instruction)
    out_execute=EX(b)
    Mem_out=MEM(out_execute)
    WB(Mem_out)
    #print(PC)
    PC=PC+4
    #print(PC)
    
PC=4194380
while(PC<=4194492):
    Cycle()
    
for i in main_memory:
    print(main_memory[i])