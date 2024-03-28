"""
문제
int array arr
-> true 반환(각 num별로 나오는 횟수가 다를 때)

문제해결전략
1. dictionary 활용 : arr에 대한 for문을 돌면서
해당 element가 dictionary key에 존재하지 않으면
key 추가, value는 0으로 / dictionary key에 들어있으면 value+=1
2. dictionary의 각 value가 다 unique한지 확인
value들로 list 구성한 후, set으로 만들어서 
list와 set의 개수가 같은지 비교하면 알 수 있음!

요구능력
1. dictionary의 key,value를 다룰 수 있는 능력
2. dict.values()를 쓰면 list비슷한 것을 리턴해줌. (list는 아니고 iterable함)
ex. iterable한 것은 list난 set으로 바로 처리 가능, 
list(counter.values()) 및 set(counter.values())
바로 len(counter.values()) 도 가능

다른 접근
1. dictionary의 value가 unique한지 확인을 위해서
sort한 후에 같은 값이 또 나오면 False하는 방법도 있음!
2. dic 초기화 경우가 if로 들어가는 편이 더 논리적 흐름에 부합하는 경향.
ex. for i not in arr
"""


def uniqueOccurence(arr)->bool:
    counter = {}
    for i in arr:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1 
    counts = [counter[key] for key in counter]
    set_counts = set(counts)
    
    return True if len(counts)==len(set_counts) else False


if __name__ == "__main__":
    arr = [1,2,2,1,1,3]
    expected_result = True
    result = uniqueOccurence(arr)
    print(result)
    print("test1 통과" if expected_result == result else "test1 실패")
    
    arr = [1,2]
    expected_result = False
    result = uniqueOccurence(arr)
    print(result)
    print("test2 통과" if expected_result == result else "test2 실패")
    
    arr = [-3, 0, 1, -3, 1,1,1, -3, 10, 0]
    expected_result = True
    result = uniqueOccurence(arr)
    print(result)
    print("test3 통과" if expected_result == result else "test3 실패")