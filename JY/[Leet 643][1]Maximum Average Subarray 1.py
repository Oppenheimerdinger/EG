""" [Leet 643] Maximum Average Subarray 1

문제
: 
integer array인 nums는 n개의 element로 이루어져있음.
그리고 interger k가 주어짐.
-> length가 k인 연속한 subarray의 maximum average value를 반환


접근 
연속된 array값들의 합이 가장 큰 것을 고른다.
그리고 그 합을 k로 나누고 반환한다.

세부전략
0. max를 0으로 초기화, sum_k을 0으로 초기화
1. nums[0]에서부터 nums[k-1]까지의 수를 다 더해서 sum_k로.
그 값을 max로 update
2. 그리고 다음 회차에서는 sum_k에서 nums[0]을 빼고 nums[k]를 더함.
그리고 이번 sum_k가 max보다 크다면 max로 update
3. 2번 과정을 i가 len(nums)-k일때까지만 진행함.
왜냐면 i+k-1이 마지막 번째니까 

요구능력!! ★문제 풀고나서는 이거를 정리하자 (다음에 복기할 때는 이거 위주로 기억)
- 어떻게 하면 연산횟수를 줄일 것이냐!! 
"""



def findMaxAverage(nums,k) -> float:
    max_sum = 0
    sum_k = 0
    
    
    for i in range(k):
        sum_k += nums[i]    #nums[0] + nums[[1] + nums[2] + nums[3]
        max_sum = sum_k

    for j in range(1, len(nums)-k+1):
        sum_k -= nums[j-1] # sum_k -= nums[0]
        sum_k += nums[j+k-1] # sum_k += nums[1+4-1] 
        # sum_k = sum_k - nums[j-1] + nums[j+k-1] 이렇게 한 줄로 표현 가능
        if max_sum < sum_k:
            max_sum = sum_k
    
    return max_sum/k

if __name__ == "__main__" :
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    result = findMaxAverage(nums, k)
    expected_result = 12.75000
    print("test1 통과" if result == expected_result else "test1 실패")
    
    nums = [5]
    k = 1
    result = findMaxAverage(nums, k)
    expected_result = 5.00000
    print("test2 통과" if result == expected_result else "test2 실패")