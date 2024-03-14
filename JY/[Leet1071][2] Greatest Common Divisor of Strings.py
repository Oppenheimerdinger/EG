#1071. Greatest Common Divisor of Strings
"""여기서 GCD의 정의 : GCD를 1번 이상 concat해서 해당 str이 나오는 경우

1. 먼저 GCD의 후보로, str1과 str2 중 짧은 친구를 할당한다.
2. len(str1), len(str2)이 len(GCD)로 나누어 떨어져야 times가 나오는 것이다.
3. 그러므로 먼저 len(str1), len(str2)가 len(GCD)로 나누어떨어지는지 확인한다.
만약 나누어떨이지지 않으면 GCD를 후보의 길이를 조정해야 한다.
4. 현재 GCD는 str1, str2 중 짧은 것인데
뒤에서부터 하나씩 줄여나가면서 GCD인지 체크할 수 있다.
어차피 GCD 자체를 1번 이상 붙여가서 str1, str2를 구성해야 하므로 앞글자는 포함될 수밖에 없다는 점에 유의
5. GCD인지 체크할 때는 str1, str2 각각 i번, j번 해서 나누어떨어지는지 보면 된다.
이 때, i <= len(str1)/len(gcd), j <= len(str2)/len(gcd)
"""

def gcdOfStrings(str1, str2):
    if len(str1) <= len(str2):
        gcd = str1
    else:
        gcd = str2
    
    for k in range(len(gcd),0,-1):
        if len(str1)%len(gcd) ==0 and len(str2)%len(gcd)==0:
            i = len(str1)//len(gcd)
            j = len(str2)//len(gcd)
            if gcd*i == str1 and gcd*j == str2:
                return gcd
            else:
                continue
        else:
            gcd = gcd[:k+1]
    return ""


if __name__ == '__main__':
    str1 = "ABCABC"
    str2 = "ABC"
    result1 = gcdOfStrings(str1, str2)
    print(result1)
    
    str1 = "ABABAB"
    str2 = "ABAB"
    result2 = gcdOfStrings(str1, str2)
    print(result2)
    
    str1 = "LEET"
    str2 = "CODE"
    result3 = gcdOfStrings(str1, str2)
    print(result3)