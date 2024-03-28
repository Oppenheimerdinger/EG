""" 문제 

nums1, nums2가 주어졌을 때,
answer list 반환 (요소 2개)
(answer[0]은 nums1에만 있는 distinct한 integer 개수)
(answer[1]은 num2에만 있는 distinct한 integer 개수)

---------------------------------
문제해결접근
1. set으로 보았을 때, answer[0]은 set(nums_1)-set(nums_2)
    answer[1]는 set(nums2)-set(nums1) 의 요소들을 리스트화

set_1 = set(nums1) 
set_2 = set(nums2) 

answer = []
answer.append((list(set_1-set_2)))
answer.append((list(set_2-set_1)))

2. 위와같이 쓰려면 set의 요소들을 list로 바로 만드는 게 
문법적으로 가능해야 함. 해보자. >> 됨!!
--------------------------------
요구능력
1. set의 특성을 알고 관련 문법을 활용해서 다룰 수 있어야 함!

"""
def findDifference(nums1, nums2):
    set_1 = set(nums1)
    set_2 = set(nums2)
    
    answer = []
    answer.append((list(set_1-set_2)))
    answer.append((list(set_2-set_1)))

    return answer



if __name__ == "__main__":
    nums1 = [1,2,3]
    nums2 = [2,4,6]
    expected_result = [[1,3], [4,6]]
    result = findDifference(nums1, nums2)
    print(result)
    print("test1 통과" if expected_result == result else "test1 실패")
    
    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]
    expected_result = [[3], []]
    result = findDifference(nums1, nums2)
    print(result)
    print("test2 통과" if expected_result == result else "test2 실패")
    