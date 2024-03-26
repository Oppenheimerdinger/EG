'''
문제:
    contiguous한 subarray중에서 average가 가장 큰 것을 return
전략:
    avg 함수를 만들고
    윈도우를 slide 해보자.
    
빠른실행 전략:
    sliding 할때 하나 빠지고 하나 들어오니까, 그 점을 이용해서 val sliding window에서 계속 새로 구하자
    대소 비교는 k개 원소의 sum으로 하고, 모든 작업을 마치고 마지막에 avg계산
    
요구능력:
    연산 횟수가 줄어드는 법을 생각해내기
    float 나눗셈이 오래 걸리는 점을 생각.
'''

def findMaxAverage_old(nums, k):
    def avg(lst):
        s = 0
        for i in lst:
            s += i
        return float(s) / float(len(lst))
    maxVal = -10 ** 4
    for i in range(len(nums)-k+1):
        val = avg(nums[i:i+k])
        if maxVal <= val:
            maxVal = val
    return maxVal

def findMaxAverage(nums, k):
    val = 0
    for i in range(k):
        val += nums[i]
    maxVal = val
    
    for i in range(1, len(nums)-k+1):
        val = val - nums[i-1] + nums[i+k-1]
        if val > maxVal:
            maxVal = val
            
    return float(maxVal) / float(k)

if __name__ == '__main__':
    nums = [1,12,-5,-6,50,3]
    k = 4
    expected = 12.75000
    output = findMaxAverage(nums, k)
    print(output)
    print(expected)
    print()

    nums = [5]
    k = 1
    expected = 5.00000
    output = findMaxAverage(nums, k)
    print(output)
    print(expected)