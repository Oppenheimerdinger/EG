#[Leet 724] Find Pivot Index
""" 
문제
nums는 integer array
Return leftmost pivot index 찾기 (없으면 -1)
(pivot index : 그 자리 기준으로 왼,오의 합이 같은 거)


문제 해결전략
1. left_sum = 0, right_sum = sum(nums)로 초기화
2. nums에 대한 순환을 돌면서 각 요소의 값을 left_sum += nums[i], right_sum -= nums[i] + nums[i+1]
3. left_sum == right_sum이면 return 해당 index 반환

요구능력
1. 점화식을 세울 수 있느냐!
2. 코드에서는 i+1 보다는, i-1을 활용한 점화식을 쓰는 편이 간단하다!


"""

# def pivotIndex(nums) :
#     left_sum = 0
#     right_sum = sum(nums)
    
#     for i in range(len(nums)-1):
#         if left_sum == right_sum: #rightsum이 0이면 return 0
#             return i        
#         left_sum += nums[i] # left_sum += nums[0], right_sum -= nums[0]+nums[1]
#         right_sum -= nums[i]+nums[i+1]
        
#     if left_sum + nums[-1] == right_sum - nums[-1]:
#         return len(nums)-1

#     return -1
        

def pivotIndex(nums) :
    left_sum = 0
    right_sum = sum(nums) - nums[0]
    
    if left_sum == right_sum :
        return 0
    
    for i in range(1, len(nums)):
        left_sum += nums[i-1] # left_sum += nums[0], right_sum -= nums[0]+nums[1]
        right_sum = right_sum - nums[i]
        if left_sum == right_sum: 
            return i  
    return -1


if __name__ == "__main__":
    nums = [1, 7, 3, 6, 5, 6]
    expected_result = 3
    result = pivotIndex(nums)
    print(result)
    print("test1 통과" if expected_result == result else "test1 실패")


    nums = [1, 2, 3]
    expected_result = -1
    result = pivotIndex(nums)
    print(result)
    print("test2 통과" if expected_result == result else "test2 실패")
    
    nums = [2, 1, -1]
    expected_result = 0
    result = pivotIndex(nums)
    print(result)
    print("test3 통과" if expected_result == result else "test3 실패")