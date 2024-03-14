#1차시도: 문제를 잘못이해하고 잘못 접근했음.... divisor의 개념을 제대로 이해하지 못함. 
def gcdOfStrings(str1, str2):
    """
    생각한 방법: str2를 str1[0:len(str2)]~str1[len(str2):]까지 체크
    일단 str2를 가지고 모든 combination을 만들어서 list안에 넣고, 그 list를 sort를 한다음에 긴애들부터 위처럼 체크를 해본다.
    """

    #1. str2를 가지고 모든 combination 만들기
    comb = []
    l2 = len(str2)
    for i in range(l2): #시작 index
        for j in range(l2): #길이
            candidate = str2[i:i+j+1]
            len_can = len(candidate)
            error_cnt = 0
            for i in range(l2-len_can):
                if str2[i:len_can] != candidate:
                    error_cnt += 1

    #2. comb를 unique하게 만들고 긴 순서대로 sort하기
    comb_unique = list(set(comb))
    comb_unique.sort(key = len, reverse = True)
    comb_unique.append("") #아무것도 없는애도 추가해주기

    #3. 긴거부터 check하면서 str1안에 있으면 그거 return하기
    for ele in comb_unique:
        if ele in str1:
            return ele


if __name__ == '__main__':
    str1 = "ABCABC"
    str2 = "ABC"
    gcdOfStrings(str1, str2)

    str1 = "ABABAB"
    str2 = "ABAB"
    gcdOfStrings(str1, str2)

    str1 = "LEET"
    str2 = "CODE"
    gcdOfStrings(str1, str2)
        