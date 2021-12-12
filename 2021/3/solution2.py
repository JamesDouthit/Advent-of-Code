import re
import copy

# def findMostCommon(bit_strs,pos):
def findMostCommon(bit_strs):
    mcb = [0 for n in range(len(bit_strs[0]))]
    for line in bit_strs:
        for i in range(len(line)):
            if line[i] == "0":
                mcb[i] -=1
            elif line[i] == "1":
                mcb[i] +=1
            else:
                print("oops",line[i])
    mcs = ""
    lcs = ""
    for b in range(len(mcb)):
        if(mcb[b] == 0):
            mcb[b] = 1
            mcs+="1"
            lcs+="0"
        elif(mcb[b] > 0):
            mcb[b] = 1
            mcs+="1"
            lcs+="0"
        else:
            mcb[b] = 0
            mcs+="0"
            lcs+="1"
    return mcs, lcs

if __name__ == "__main__":
    with open("3input.txt") as f:
        data = f.read()
    diagnostic_list = data.split("\n")
    oxy_list = copy.deepcopy(diagnostic_list)
    co2_list = copy.deepcopy(diagnostic_list)
    considering_bit = 0
    while (len(oxy_list)>1 and considering_bit<len(oxy_list[0])):
        new_oxy_list = []
        most_common, least_common = findMostCommon(oxy_list)
        most_common_bit = most_common[considering_bit]
        for oxy_list_entry in oxy_list:
            if(oxy_list_entry[considering_bit]==most_common_bit):
                new_oxy_list.append(oxy_list_entry)
        oxy_list = new_oxy_list
        print(most_common[considering_bit],"was MOST common in pos",considering_bit,"so kept",new_oxy_list,"\n")
        considering_bit +=1
    considering_bit = 0
    while (len(co2_list)>1 and considering_bit<len(co2_list[0])):
        new_co2_list = []
        most_common, least_common = findMostCommon(co2_list)
        least_common_bit = least_common[considering_bit]
        for co2_list_entry in co2_list:
            if(co2_list_entry[considering_bit]==least_common_bit):
                new_co2_list.append(co2_list_entry)
        co2_list = new_co2_list
        print(least_common[considering_bit],"was LEAST common in pos",considering_bit,"so kept",new_co2_list,"\n")
        considering_bit +=1
    print(oxy_list)
    print(co2_list)
    oxy = int(oxy_list[0],2)
    co2 = int(co2_list[0],2)
    print("oxy:",oxy_list[0],"=",oxy,"epsilon:",co2_list[0],"=",co2)
    print(oxy*co2)

# t0 = time.time()
# for run in range(1000):
#     with open("3input.txt") as f:
#         data = f.read()
#     diagnostic_list = data.split("\n")
#     mcb = [0 for n in range(len(diagnostic_list[0]))]
#     for line in diagnostic_list:
#         for i in range(len(line)):
#             if line[i] == "0":
#                 mcb[i] -=1
#             elif line[i] == "1":
#                 mcb[i] +=1
#             else:
#                 print("oops",line[i])
#     mcs = ""
#     lcs = ""
#     for b in range(len(mcb)):
#         if(mcb[b] >= 0):
#             mcb[b] = 1
#             mcs+="1"
#             lcs+="0"
#         else:
#             mcb[b] = 0
#             mcs+="0"
#             lcs+="1"
#     gamma = int(mcs,2)
#     epsilon = int(lcs,2)
#     # print(int(mcs,2)*int(lcs,2))
# t1 = time.time()
# print(t1-t0)
