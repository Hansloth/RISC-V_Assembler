# RISC-V_Assembler
Implementing RISC-V Assembler in Python

## To run the code:
>* STEP1 make an input.txt   
>* STEP2 copy to the directory of the input.txt to the interger input_data_dir in the code  
>* STEP2 RUN!

#Limitations:  
>* Please only input decimal to I type instructions  
>* Only work on R,S,I type instructions  
 
## Sample Input and Outputs:   
### Example 1 (R Type Instructions):    
>add x5, x0, x12    
>xor x21, x11, x10  
>srl x14, x19, x1  
>or x12, x3, x3   
>
>Output Code =>  
>00000000110000000000001010110011   
>00000000101001011100101010110011   
>00000000000110011101011100110011   
>00000000001100011110011000110011   

### Example 2 (I Type Instructions):  
>addi x5, x0, 100  
>slti x21, x11, 121  
>sltiu x11, x6, 0  
>ori x12, x3, 69  
>  
>Output Code =>   
>00000110010000000000001010010011  
>00000111100101011010101010010011  
>00000000000000110011010110010011  
>00000100010100011110011000010011  
  
### Example 3 (S Type Instructions):  
>sb x10, 10(x6)  
>sh x18, 8(x11)  
>sh x18, 8(x11)  
>  
>Output Code =>   
>00000000101000110000010100100011  
>00000001001001011001010000100011  
>00000000010110001010000100100011  












