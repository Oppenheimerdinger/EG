'''
str1의 Divisor를 길이가 긴 것부터 찾는다.
찾은 Dividor가 str2의 Divisor 인지 체크해서 맞으면 바로 return 한다.
'''

def gcdOfStrings(str1, str2):
    i = len(str1)
    while (i >= 1):
        divisor = str1[:i]
        if (check_divisor(str1, divisor) == True):
            if(check_divisor(str2, divisor) == True):
                return divisor
        i -= 1
    return ""
        

def check_divisor(s, divisor):
    # 안 나누어 떨어지면 False
    if len(s) % len(divisor) != 0:
        return False
    # 약수가 맞는지 체크체크
    else:
        for i in range(len(s) // len(divisor)):
            if s[i * len(divisor): (i+1) * len(divisor)] != divisor:
                return False
    return True



if __name__ == '__main__':
    str1 = 'ABCABC'
    str2 = 'ABC'
    output = gcdOfStrings(str1, str2)
    ans = "ABC"
    print("Answer:\t" + ans)
    print("Output:\t" + output)
    
    str1 = 'ABABAB'
    str2 = 'ABAB'
    output = gcdOfStrings(str1, str2)
    ans = "AB"
    print("Answer:\t" + ans)
    print("Output:\t" + output)
    
    str1 = 'LEET'
    str2 = 'CODE'
    output = gcdOfStrings(str1, str2)
    ans = ""
    print("Answer:\t" + ans)
    print("Output:\t" + output)