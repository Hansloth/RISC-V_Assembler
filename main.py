import re
import os

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
        # return string
    return str1

def register_to_machinecode(register, digits):
    a = "000000000000000"
    register_num = register.lstrip("x")
    register_bin_num = decimalToBinary(int(register_num))
    extent_zeros_count = digits - len(register_bin_num)
    register_bin_num = a[0:extent_zeros_count] + register_bin_num
    return register_bin_num

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

def get_machine_code(first_line_code):
    machine_code_result = ""
    first_line_code = re.sub("[^\w]", " ", first_line_code).split()  # first_line_code變list型式
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

#在input_data_dir輸入input.txt的位置
input_data_dir = "C:/Users/Hans/PycharmProjects/AS&OA_HW1/input.txt"

al_code = get_input(input_data_dir)
first_line_code = ""
print("Input Code => ")
for i in range(len(al_code)):
    print(al_code[i], end='')

print("\nOutput Code => ")
for i in range(len(al_code)):
    first_line_code = al_code[i]
    print(get_machine_code(first_line_code))

    #檢查用
    # print(len(get_machine_code(first_line_code)), end='')nt
    # print(" bits")
    # 輸出machine code bits count rint(get_machine_code(first_line_code))