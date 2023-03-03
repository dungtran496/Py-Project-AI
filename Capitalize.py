def solve(s):
    sss = ''
    for i,ss in enumerate(s):
        if i==0:
            sss += ss.capitalize()
        elif s[i-1]==' ' and ss!=' ':
            sss += ss.capitalize()
        else:
            sss += ss
    return sss
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#Sample: chris alan => Chris Alan