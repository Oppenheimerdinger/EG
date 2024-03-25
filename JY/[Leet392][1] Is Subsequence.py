""" 문제 정의 
s, t가 주어졌을 때, 
만약 s가 t의 subsequence이면 true
그렇지 않으면 false

subsequence란 몇 개의 character를 지우고 남은 것들의 
순서가 유지되는 것

--------------------
문제 전략
1. s-t를 했을 때 공집합이면 true, 그렇지 않으면 fasle 
(근데 이거는 순서를 고려하지 못함)

1. s랑 t를 일단 list로 바꿔준다.
2. s안에 있는 문자들의 순서 a < b < c 이 순서가 t에서도 유지되어야 하는 것임.
3. 그렇다면, pointer를 두 개 써보자.
하나는 한 자리씩 앞으로 나아가면서 모든 문자들을 다 확인했는지 체크
이게 t의 글자수와 같아지면 끝.

다른 하나는 t에서 s와 같은 것을 발견했을 때 
s를 한 칸 앞으로 옮기는 역할. + counter도 한 칸 앞으로
발견하지 못하면 counter만 한 칸 앞으로 나아감.

"""

def isSubsequence(s,t) :
    counter = 0
    checker = 0
    
    # if s == "":
    #     return True (필요없음)
    while checker < len(s) and counter < len(t):
        if s[checker] == t[counter]:
            counter += 1
            checker += 1
        else :
            counter += 1
    
    return True if counter <= len(t) and checker == len(s) else False
    
if __name__ == "__main__" :
    s = "abc"
    t = "ahbgdc"
    result = isSubsequence(s,t)
    expected_result = True
    print("test1 통과" if result == expected_result else "test1 실패")
    
    # 1) s[0] == t[0] couter 1 checker 1
    # 2) s[1] == t[1] counter 2 checker 1
    # 3) s[1] == t[2] counter 3 checker 2
    # 4) s[2] == t[3] counter 4 checker 2
    # 5) s[2] == t[4] counter 5 checker 2
    # 6) s[2] == t[5] counter 6 checker 3    
    
    
    s = "axc"
    t = "ahbgdc"
    result = isSubsequence(s,t)
    expected_result = False
    print("test2 통과" if result == expected_result else "test2 실패")
    
    # 1) s[0] == t[0] couter 1 checker 1
    # 2) s[1] == t[1] counter 2 checker 1
    # 3) s[1] == t[2] counter 3 checker 1
    # 4) s[2] == t[3] counter 4 checker 1
    # 5) s[2] == t[4] counter 5 checker 1
    # 6) s[2] == t[5] counter 6 checker 1
    # 7) 
    
    s = "b"
    t = "abc"
    result = isSubsequence(s,t)
    expected_result = True
    print("test3 통과" if result == expected_result else "test3 실패")
    
    #1) s[0] != t[0] counter 1 checker 0
    #2) s[0] == t[1] counter 2 checker 1  탈출
    #3) s[1] != t[2] counter 3 checker 1
    
    
    
    

