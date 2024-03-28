'''
문제:
    각 value의 '개수'가 unique 인가?
풀이:
    value의 개수를 Dict로 관리
    개수의 리스트를 만들고
    걔를 set으로 해서 리스트와 set의 길이 를 비교
필요능력:
    Dict로 개수 잘 세는 법:
        not in 을 먼저 해서 초기화 조건을 먼저 쓰는 것이 논리적으로 머리가 편하다.
    dict.values() 는 리스트 비슷한 것을 리턴해준다.
        list는 아니지만 iterable해서 거의 비슷하다고 보면 됨
        
'''

def uniqueOccurrences(arr):
    valCount = dict()
    for i in arr:
        if i not in valCount:
            valCount[i] = 1
        else:
            valCount[i] += 1
    return len(valCount.values()) == len(set(valCount.values()))

if __name__ == '__main__':
    arr = [1,2,2,1,1,3]
    expected = True
    output = uniqueOccurrences(arr)
    print(expected)
    print(output)
    print()
    
    arr = [1,2]
    expected = False
    output = uniqueOccurrences(arr)
    print(expected)
    print(output)
    print()