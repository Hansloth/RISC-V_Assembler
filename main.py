import re
from bitstring import BitArray

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def listToString(s):
    """
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
        # return string
    return str1
    """
    my_list = s
    my_string = " "
    for a in my_list:
        my_string = my_string + ' ' + a
    return my_string

def stringToList(s):
    #s = re.sub("[^\w]", " ", s).split()
    s = re.sub(r",", " ", s)
    s = s.replace("(", " ")
    s = s.replace(")", " ")
    s = s.replace(":", " ")
    s = s.lstrip().rstrip()
    return s.split()

def register_to_machinecode(register, digits):
    a = "0000000000000000000000000000000000000000000000000000000000000000000000"
    register_num = register.lstrip("x")
    register_num = int(register_num.rstrip(","))
    if register_num >= 0:
        register_bin_num = decimalToBinary(int(register_num))
        extent_zeros_count = digits - len(register_bin_num)
        register_bin_num = a[0:extent_zeros_count] + register_bin_num
        return register_bin_num

    if register_num < 0:
        s = bin(register_num & int("1" * digits, 2))[2:]
        return ("{0:0>%s}" % (digits)).format(s)

def get_input(input_data_dir):
    #取得input code

    input = [[] for i in range(30)]
    count = 0
    with open(input_data_dir, 'r') as f:
        for line in f:
            input[count].append(line)
            count += 1
    input_code = [0 for i in range(count)]
    input_code = input[0:count]
    del input

    for j in range(len(input_code)):
        #clear the blank in front of the code
        input_code[j] = listToString(input_code[j]).lstrip()
    return input_code

def find_branch_offset(all_line_code, line_of_code, first_line_code_4):
    for i in range(len(all_line_code)):
        check_label_code = stringToList(all_line_code[i])
        if check_label_code[0] == first_line_code_4:
            if line_of_code > i:
                return str(4 * (i - line_of_code + 1))
            elif i > line_of_code:
                return str(4 * (i - line_of_code - 1))

def r_type(first_line_code, first_line_code_1):
    # add, sub, sll, slt, sltu, xor, srl, sra, or, and
    if first_line_code_1 == "add" or first_line_code_1 == "ADD":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs1 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        rs2 = register_to_machinecode(first_line_code_4, 5)

        machine_code_result = "0000000" + rs2 + rs1 + "000" + rd + "0110011"
        return machine_code_result
    elif first_line_code_1 == "sub" or first_line_code_1 == "SUB":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs1 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        rs2 = register_to_machinecode(first_line_code_4, 5)

        machine_code_result = "0100000" + rs2 + rs1 + "000" + rd + "0110011"
        return machine_code_result
    elif first_line_code_1 == "sll" or first_line_code_1 == "SLL":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs1 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        rs2 = register_to_machinecode(first_line_code_4, 5)

        machine_code_result = "0000000" + rs2 + rs1 + "001" + rd + "0110011"
        return machine_code_result
    elif first_line_code_1 == "slt" or first_line_code_1 == "SLT":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs1 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        rs2 = register_to_machinecode(first_line_code_4, 5)

        machine_code_result = "0000000" + rs2 + rs1 + "010" + rd + "0110011"
        return machine_code_result
    elif first_line_code_1 == "sltu" or first_line_code_1 == "SLTU":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs1 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        rs2 = register_to_machinecode(first_line_code_4, 5)

        machine_code_result = "0000000" + rs2 + rs1 + "011" + rd + "0110011"
        return machine_code_result
    elif first_line_code_1 == "xor" or first_line_code_1 == "XOR":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs1 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        rs2 = register_to_machinecode(first_line_code_4, 5)

        machine_code_result = "0000000" + rs2 + rs1 + "100" + rd + "0110011"
        return machine_code_result
    elif first_line_code_1 == "srl" or first_line_code_1 == "SRL":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs1 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        rs2 = register_to_machinecode(first_line_code_4, 5)

        machine_code_result = "0000000" + rs2 + rs1 + "101" + rd + "0110011"
        return machine_code_result
    elif first_line_code_1 == "sra" or first_line_code_1 == "SRA":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs1 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        rs2 = register_to_machinecode(first_line_code_4, 5)

        machine_code_result = "0000000" + rs2 + rs1 + "101" + rd + "0110011"
        return machine_code_result
    elif first_line_code_1 == "or" or first_line_code_1 == "OR":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs1 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        rs2 = register_to_machinecode(first_line_code_4, 5)

        machine_code_result = "0000000" + rs2 + rs1 + "110" + rd + "0110011"
        return machine_code_result
    elif first_line_code_1 == "and" or first_line_code_1 == "ADD":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs1 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        rs2 = register_to_machinecode(first_line_code_4, 5)

        machine_code_result = "0000000" + rs2 + rs1 + "111" + rd + "0110011"
        return machine_code_result

def i_type(first_line_code, first_line_code_1):
    # addi, slti, sltiu, xori, ori, andi, lb, lh, lw, lbu, lhu, jalr
    if first_line_code_1 == "addi" or first_line_code_1 == "ADDI":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs1 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        simm = register_to_machinecode(first_line_code_4, 12)

        machine_code_result = simm + rs1 + "000" + rd + "0010011"
        return machine_code_result
    elif first_line_code_1 == "slti" or first_line_code_1 == "SLTI":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs1 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        simm = register_to_machinecode(first_line_code_4, 12)

        machine_code_result = simm + rs1 + "010" + rd + "0010011"
        return machine_code_result
    elif first_line_code_1 == "sltiu" or first_line_code_1 == "SLTIU":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs1 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        simm = register_to_machinecode(first_line_code_4, 12)

        machine_code_result = simm + rs1 + "011" + rd + "0010011"
        return machine_code_result
    elif first_line_code_1 == "xori" or first_line_code_1 == "XORI":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs1 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        simm = register_to_machinecode(first_line_code_4, 12)

        machine_code_result = simm + rs1 + "100" + rd + "0010011"
        return machine_code_result
    elif first_line_code_1 == "ori" or first_line_code_1 == "ORI":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs1 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        simm = register_to_machinecode(first_line_code_4, 12)

        machine_code_result = simm + rs1 + "110" + rd + "0010011"
        return machine_code_result
    elif first_line_code_1 == "andi" or first_line_code_1 == "ANDI":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs1 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        simm = register_to_machinecode(first_line_code_4, 12)

        machine_code_result = simm + rs1 + "111" + rd + "0010011"
        return machine_code_result
    elif first_line_code_1 == "lb" or first_line_code_1 == "LB":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        simm = register_to_machinecode(first_line_code_3, 12)

        first_line_code_4 = first_line_code[3]
        rs1 = register_to_machinecode(first_line_code_4, 5)

        machine_code_result = simm + rs1 + "000" + rd + "0010011"
        return machine_code_result
    elif first_line_code_1 == "lh" or first_line_code_1 == "LH":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        simm = register_to_machinecode(first_line_code_3, 12)

        first_line_code_4 = first_line_code[3]
        rs1 = register_to_machinecode(first_line_code_4, 5)

        machine_code_result = simm + rs1 + "001" + rd + "0000011"
        return machine_code_result
    elif first_line_code_1 == "lw" or first_line_code_1 == "LW":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        simm = register_to_machinecode(first_line_code_3, 12)

        first_line_code_4 = first_line_code[3]
        rs1 = register_to_machinecode(first_line_code_4, 5)

        machine_code_result = simm + rs1 + "010" + rd + "0000011"
        return machine_code_result
    elif first_line_code_1 == "lbu" or first_line_code_1 == "LBU":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        simm = register_to_machinecode(first_line_code_3, 12)

        first_line_code_4 = first_line_code[3]
        rs1 = register_to_machinecode(first_line_code_4, 5)

        machine_code_result = simm + rs1 + "100" + rd + "0000011"
        return machine_code_result
    elif first_line_code_1 == "lhu" or first_line_code_1 == "LHU":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        simm = register_to_machinecode(first_line_code_3, 12)

        first_line_code_4 = first_line_code[3]
        rs1 = register_to_machinecode(first_line_code_4, 5)

        machine_code_result = simm + rs1 + "101" + rd + "0000011"
        return machine_code_result
    elif first_line_code_1 == "jalr" or first_line_code_1 == "JALR":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs1 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        simm = register_to_machinecode(first_line_code_4, 12)

        machine_code_result = simm + rs1 + "000" + rd + "1100111"
        return machine_code_result

def s_type(first_line_code, first_line_code_1):
    # sb, sh, sw
    if first_line_code_1 == "sb" or first_line_code_1 == "SB":
        first_line_code_2 = first_line_code[1]
        rs2 = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        simm = register_to_machinecode(first_line_code_3, 12)

        first_line_code_4 = first_line_code[3]
        rs1 = register_to_machinecode(first_line_code_4, 5)

        machine_code_result = simm[0:7] + rs2 + rs1 + "000" + simm[7:13] + "0100011"
        return machine_code_result

    if first_line_code_1 == "sh" or first_line_code_1 == "SH":
        first_line_code_2 = first_line_code[1]
        rs2 = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        simm = register_to_machinecode(first_line_code_3, 12)

        first_line_code_4 = first_line_code[3]
        rs1 = register_to_machinecode(first_line_code_4, 5)

        machine_code_result = simm[0:7] + rs2 + rs1 + "001" + simm[7:13] + "0100011"
        return machine_code_result

    if first_line_code_1 == "sw" or first_line_code_1 == "SW":
        first_line_code_2 = first_line_code[1]
        rs2 = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        simm = register_to_machinecode(first_line_code_3, 12)

        first_line_code_4 = first_line_code[3]
        rs1 = register_to_machinecode(first_line_code_4, 5)

        machine_code_result = simm[0:7] + rs2 + rs1 + "010" + simm[7:13] + "0100011"
        return machine_code_result

def sb_type(first_line_code, first_line_code_1, all_line_code, line_of_code):
    # beq , bne, blt, bge, bltu, bgeu
    if first_line_code_1 == "beq" or first_line_code_1 == "BEQ":
        first_line_code_2 = first_line_code[1]
        rs1 = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs2 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        simm = register_to_machinecode(find_branch_offset(all_line_code, line_of_code, first_line_code_4), 13)

        machine_code_result = simm[0] + simm[2:8] + rs2 + rs1 + "000" + simm[8:12] + simm[1] + "1100011"
        return machine_code_result

    if first_line_code_1 == "bne" or first_line_code_1 == "BNE":
        first_line_code_2 = first_line_code[1]
        rs1 = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs2 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        simm = register_to_machinecode(find_branch_offset(all_line_code, line_of_code, first_line_code_4), 13)

        machine_code_result = simm[0] + simm[2:8] + rs2 + rs1 + "001" + simm[8:12] + simm[1] + "1100011"
        return machine_code_result

    if first_line_code_1 == "blt" or first_line_code_1 == "BLT":
        first_line_code_2 = first_line_code[1]
        rs1 = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs2 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        simm = register_to_machinecode(find_branch_offset(all_line_code, line_of_code, first_line_code_4), 13)

        machine_code_result = simm[0] + simm[2:8] + rs2 + rs1 + "100" + simm[8:12] + simm[1] + "1100011"
        return machine_code_result

    if first_line_code_1 == "bge" or first_line_code_1 == "BGE":
        first_line_code_2 = first_line_code[1]
        rs1 = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs2 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        simm = register_to_machinecode(find_branch_offset(all_line_code, line_of_code, first_line_code_4), 13)

        machine_code_result = simm[0] + simm[2:8] + rs2 + rs1 + "101" + simm[8:12] + simm[1] + "1100011"
        return machine_code_result

    if first_line_code_1 == "bltu" or first_line_code_1 == "BLTU":
        first_line_code_2 = first_line_code[1]
        rs1 = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs2 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        simm = register_to_machinecode(find_branch_offset(all_line_code, line_of_code, first_line_code_4), 13)

        machine_code_result = simm[0] + simm[2:8] + rs2 + rs1 + "110" + simm[8:12] + simm[1] + "1100011"
        return machine_code_result

    if first_line_code_1 == "BGEU" or first_line_code_1 == "bgeu":
        first_line_code_2 = first_line_code[1]
        rs1 = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        rs2 = register_to_machinecode(first_line_code_3, 5)

        first_line_code_4 = first_line_code[3]
        simm = register_to_machinecode(find_branch_offset(all_line_code, line_of_code, first_line_code_4), 13)

        machine_code_result = simm[0] + simm[2:8] + rs2 + rs1 + "111" + simm[8:12] + simm[1] + "1100011"
        return machine_code_result

def u_type(first_line_code, first_line_code_1):
    # lui, auipc
    if first_line_code_1 == "lui" or first_line_code_1 == "LUI":
       first_line_code_2 = first_line_code[1]
       rd = register_to_machinecode(first_line_code_2, 5)

       first_line_code_3 = first_line_code[2]
       simm = register_to_machinecode(first_line_code_3, 32)

       machine_code_result = simm[0:20] + rd + "0110111"
       return machine_code_result

    if first_line_code_1 == "auipc" or first_line_code_1 == "AUIPC":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        simm = register_to_machinecode(first_line_code_3, 32)

        machine_code_result = simm[0:20] + rd + "0010111"
        return machine_code_result

def uj_type(first_line_code, first_line_code_1):
    #jal
    if first_line_code_1 == "jal" or first_line_code_1 == "JAL":
        first_line_code_2 = first_line_code[1]
        rd = register_to_machinecode(first_line_code_2, 5)

        first_line_code_3 = first_line_code[2]
        simm = register_to_machinecode(first_line_code_3, 21)

        machine_code_result = simm[0] + simm[10:20] + simm[9] + simm[1:9] + rd + "1101111"
        return machine_code_result

def get_machine_code(first_line_code, all_line_code, line_of_code):
    machine_code_result = ""
    first_line_code = first_line_code.rstrip("\n")
    #first_line_code = first_line_code.split()  # first_line_code變list型式
    first_line_code = stringToList(first_line_code) # first_line_code變list型式
    first_line_code_1 = first_line_code[0]

    # add, sub, sll, slt, sltu, xor, srl, sra, or, and
    if first_line_code_1 == "add" or first_line_code_1 == "sub" or first_line_code_1 == "sll"\
        or first_line_code_1 == "slt" or first_line_code_1 == "sltu" or first_line_code_1 == "xor" \
        or first_line_code_1 == "srl" or first_line_code_1 == "sra" or first_line_code_1 == "or"\
        or first_line_code_1 == "and" or first_line_code_1 == "ADD" or first_line_code_1 == "SUB"\
        or first_line_code_1 == "SLL"or first_line_code_1 == "SLT" or first_line_code_1 == "SLTU"\
        or first_line_code_1 == "SRL" or first_line_code_1 == "SRA" or first_line_code_1 == "OR"\
        or first_line_code_1 == "AND":
        machine_code = r_type(first_line_code, first_line_code_1)
        return machine_code

    # addi, slti, sltiu, xori, ori, andi, lb, lh, lw, lbu, lhu
    elif first_line_code_1 == "addi" or first_line_code_1 == "slti" or first_line_code_1 == "sltiu"\
        or first_line_code_1 == "xori" or first_line_code_1 == "ori" or first_line_code_1 == "andi"\
        or first_line_code_1 == "ADDI" or first_line_code_1 == "SLTI" or first_line_code_1 == "SLTIU"\
        or first_line_code_1 == "XORI" or first_line_code_1 == "ORI" or first_line_code_1 == "ANDI" \
        or first_line_code_1 == "lb" or first_line_code_1 == "lh" or first_line_code_1 == "lw" \
        or first_line_code_1 == "lbu" or first_line_code_1 == "lhu" or first_line_code_1 == "LB" \
        or first_line_code_1 == "LH" or first_line_code_1 == "LW" or first_line_code_1 == "LBU" \
        or first_line_code_1 == "LHU" or first_line_code_1 == "jalr" or first_line_code_1 == "JALR":
        machine_code = i_type(first_line_code, first_line_code_1)
        return machine_code

    # sb, sh, sw
    elif first_line_code_1 == "sb" or first_line_code_1 == "sh" or first_line_code_1 == "sw"\
        or first_line_code_1 == "SB" or first_line_code_1 == "SH" or first_line_code_1 == "SW":
        machine_code = s_type(first_line_code, first_line_code_1)
        return machine_code

    #beq, bne , blt, bge, bltu, bgeu
    elif first_line_code_1 == "beq" or first_line_code_1 == "bne" or first_line_code_1 == "blt" \
         or first_line_code_1 == "bge" or first_line_code_1 == "bltu" or first_line_code_1 == "bgeu" \
         or first_line_code_1 == "BEQ" or first_line_code_1 == "BNE" or first_line_code_1 == "BLT" \
         or first_line_code_1 == "BGE" or first_line_code_1 == "BLTU" or first_line_code_1 == "BGEU":
         machine_code = sb_type(first_line_code, first_line_code_1, all_line_code, line_of_code)
         return machine_code
                 #在input_data_dir輸入input.txt的位置

    elif first_line_code_1 == "lui" or first_line_code_1 == "auipc" or first_line_code_1 == "LUI"\
        or first_line_code_1 == "AUIPC":
        machine_code = u_type(first_line_code, first_line_code_1)
        return machine_code

    elif first_line_code_1 == "jal" or first_line_code_1 == "JAL":
        machine_code = uj_type(first_line_code, first_line_code_1)
        return machine_code

    else:
        del first_line_code[0]
        new_first_line_code = ""
        for i in range(len(first_line_code)):
            new_first_line_code = new_first_line_code + first_line_code[i] + " "
        return get_machine_code(new_first_line_code, all_line_code, line_of_code)




input_data_dir = "C:/Users/Hans/PycharmProjects/AS&OA_HW1/input.txt"

al_code = get_input(input_data_dir)
first_line_code = ""
print("Input Code => ")
for i in range(len(al_code)):
    print(al_code[i], end='')

print("\nOutput Code => ")
for i in range(len(al_code)):
    first_line_code = al_code[i]
    all_line_code = al_code
    print(get_machine_code(first_line_code, all_line_code, i))

    #檢查用
    print(len(get_machine_code(first_line_code, all_line_code, i)), end="")
    print(" bits")
    #print("12345678901234567890123456789012")
    # 輸出machine code bits count rint(get_machine_code(first_line_code))