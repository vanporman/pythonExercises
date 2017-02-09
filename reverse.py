
def reverse(x) :
    print x
    revStr = ''
    length = len(x)-1
    while length >= 0:
        #revStr += "%s"%x[length]
        revStr += x[length]
        #print revStr
        length -= 1
    print revStr

reverse("And#&/eas")
