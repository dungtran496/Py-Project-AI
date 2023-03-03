import textwrap

def wrap(string, max_width):
    new_string=""
    for i in range(len(string)//max_width+1):
        new_string+=string[i*max_width:(i+1)*max_width]+'\n'
    return new_string
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
#Input:
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ