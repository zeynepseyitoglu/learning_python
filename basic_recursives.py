#reverse string
def reverseString(str):

    if str == '':
        return ''
    
    return reverseString(str[1:]) + str[0]


print(reverseString('My first recursive algorithm'))

#Check whether a given string is a palindrome
def isPalindrome(str):
    if len(str) == 0 or len(str) == 1:
        return True
    if str[0] == str[len(str) - 1]:
        return isPalindrome(str[1:(len(str) - 1)])
    return False

print(isPalindrome('kayak'))

#Convert decimals into binary
def toBinary(dec, res=''):
    if dec == 0:
        return res
    res = str(dec % 2) + res
    return toBinary(dec // 2, res)

print(toBinary(233))