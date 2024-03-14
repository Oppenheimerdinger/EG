'''
str1의 divisor 를 큰 것부터 찾기
이게 str2의 divisor이면 그것이 GCD

divisor인지 체크하는 법
1. 길이가 나누어 떨어지는지 체크
2. 나누어 떨어지면, divisor를 적절히 반복했을 때, 원본이 나오는지를 체크
'''
def is_divisor(s, divisor):
    if len(s) % len(divisor) != 0:
        return False
    
    n = len(s) // len(divisor)
    if s == divisor * n:
        return True
    else:
        return False

def gcdOfStrings(str1, str2):
    for i in range(len(str1), 0, -1): 
        divisor = str1[:i]
        # str1의 divisor인지 체크 -> str2의 divisor인지 체크
        if(is_divisor(str1, divisor)):
            if(is_divisor(str2, divisor)):
                return divisor
    return ""

if __name__ == '__main__':
    str1 = 'ABCABC'
    str2 = 'ABC'
    output = gcdOfStrings(str1, str2)
    expected = 'ABC'
    print("Output:  \t" + output)
    print("Expected:\t" + expected)

    str1 = 'ABABAB'
    str2 = 'ABAB'
    output = gcdOfStrings(str1, str2)
    expected = 'AB'
    print("Output:  \t" + output)
    print("Expected:\t" + expected)

    str1 = 'LEET'
    str2 = 'CODE'
    output = gcdOfStrings(str1, str2)
    expected = ''
    print("Output:  \t" + output)
    print("Expected:\t" + expected)