'''
문제:
    pivot index를 찾으시오
    pivot index:
        특정 index 기준으로 왼쪽의 총 합 = 오른쪽의 총 합

풀이 전략:
    left = 왼쪽합
    right = 오른쪽 합

    점화식:
        초기 조건
            left[0] = 0
            right[0] = totalSum - left[0]
        
        점화식
            left[i], right[i]를 알 때
            left[i+1] = left[i] + nums[i]
            right[i+1] = right[i] - nums[i+1]
        
        코드에서는 left[i]와 right[i]를 left[i-1]과 right[i-1]로부터 계산이 효과적
            left[i] = left[i-1] + nums[i-1]
            right[i] = right[i-1] - nums[i]
        
    [0,  1,  2, 3, 4, 5, 6, 7, 8]
    [-, i-1, -, -, -, -, -, -, -]
    [-,  -,  i, -, -, -, -, -, -]
    
요구 능력:
    점화식을 만들 줄 알아야 함.
    수식으로는 a[i+1] = f(a[i]) 로 만드는 것이 자연스럽지만
    코드에서는 a[i] = f(a[i-1]) 로 이용하는 것이 더 편리함.
'''


def pivotIndex(nums):
    # 점화식 초기 조건
    left = 0
    right = 0
    for i in range(1, len(nums)):
        right += nums[i]
    if left == right:
        return 0
    
    # 점화식 풀이
    for i in range(1, len(nums)):
        left += nums[i-1]
        right -= nums[i]
        if left == right:
            return i
    
    # No Pivot
    return -1

if __name__ == '__main__':
    nums = [1,7,3,6,5,6]
    expected = 3
    output = pivotIndex(nums)
    print(output)
    print(expected)
    print()
    
    nums = [1,2,3]
    expected = -1
    output = pivotIndex(nums)
    print(output)
    print(expected)
    print()