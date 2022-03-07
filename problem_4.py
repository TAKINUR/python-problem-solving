#Define Reverse Function
def reverse(s):
    str = ""
    for i in range(len(s), 0, -1):
        str += s[i-1]
    return str


#User Input
string = input('Please Enter Text to Reverse: ')

print(reverse(string))