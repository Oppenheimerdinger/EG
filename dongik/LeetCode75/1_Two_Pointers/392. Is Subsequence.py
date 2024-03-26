'''
문제
    s가 t의 subsequence?

풀이 전략
    s = abc이면 s의 안을 가리키는 pointer: i
    t = ahbgdc이면 ahbgdc 가리키는: j

    i는 s를 가리키며 한 칸씩 진행
    j는 t를 가리키며 해당 문자를 찾을 때까지 진행
    다 못 찾았는데 (= for loop가 다 돌지 못 했는데)
        j가 len(t) 에 도달(혹은 이상) 이면 False
    다 찾았으면 (for loop가 끝남)
        return True

요구 능력:
    s의 포인터, t의 포인터를 쭈루룩 따라가면서 if 문을 논리적으로 만들 수 있는가

'''
def isSubsequence(s, t):
    j = 0
    for i in range(len(s)):
        while True:
            if j == len(t):
                return False
            if s[i] == t[j]:
                j += 1
                break
            else:
                j += 1
    return True



if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    output = isSubsequence(s, t)
    expected = True
    print(output)
    print(expected)
    print()

    s = "axc"
    t = "ahbgdc"
    output = isSubsequence(s, t)
    expected = False
    print(output)
    print(expected)