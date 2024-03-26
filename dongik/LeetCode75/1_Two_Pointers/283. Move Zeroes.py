'''
nums: array
return: array에서 0이 모두 오른쪽으로 몰아놓은 리스트

리스트의 원소를 빼면, 배열의 순서가 바뀌므로,
if 문으로 검사할 위치도 바뀜
원소를 검사하고 pop한다.
'''

def moveZeroes(nums):
    n_poped = 0
    for i in range(len(nums)):
        if nums[i - n_poped] == 0:
            nums.pop(i - n_poped)
            nums.append(0)
            n_poped += 1

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    expected =  [1,3,12,0,0]
    moveZeroes(nums)
    output = nums
    print(expected)
    print(output)
    print()

    nums = [0]
    expected =  [0]
    moveZeroes(nums)
    output = nums
    print(expected)
    print(output)
    print()
    
    nums = [0, 0, 1]
    expected =  [1, 0, 0]
    moveZeroes(nums)
    output = nums
    print(expected)
    print(output)
    print()