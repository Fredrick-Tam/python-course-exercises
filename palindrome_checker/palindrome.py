import string

def palindrome(x):
    x = str(x)
    x = x.lower()
    x = x.strip(" ")
    
    for c in string.punctuation:
     x= x.replace(c,"")
    x = ''.join(x.split())
    
    if x == x[::-1]:
        print True
    else:
        print False


palindrome('put your word here')
