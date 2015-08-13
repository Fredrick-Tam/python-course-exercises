# function finds number of substrings in a string

def substr(string):
    j=1
    a=set()
    while True:
        for i in range(len(string)-j+1):
            a.add(string[i:i+j])
        if j==len(string):
            break
        j+=1
        #string=string[1:]
    print len(a)

substr('fredrick')
