#[Leetcode 283] Move Zeroes

""" 
문제
: int array  nums가 있을 때 0을 맨 끝으로 옮기기!! 
0이 아닌 다른 요소들은 다 유지하고!!

주의사항 : copy를 만들지 말고 해야함!

- 문제 풀이 전략
0. N = len(s)
1. 두 개의 포인터를 선언한다. present, search
2. present는 0을 만나면 -= 1을 해줌. 0이 아니면 += 1
리스트에 append.(0)을 함. remove()
search는 그것과 상관없이 하나씩 다음자리로 간다. search는 += 1 
3. search == N-1이 되면 끝내기.


- 문제 풀이 전략 2
0. 0을 세는 count 만듦
1. for문을 돈다. 전체 리스트에 대해서
2. 해당 포인터가 가리키는 자리가 0이면 remove.(해당자리) 하고 append(0)
3. 그렇지 않으면 i-count

"""

def moveZeroes(nums):
    N = len(nums)
    present = 0
    search = 0
    
    while search <= N-1: 
        if nums[present] == 0 :
            search += 1
            nums.append(0)
            nums.remove(nums[present])
        else:
            search += 1
            present += 1
            
            
if __name__ == '__main__':
    nums = [0,1,0,3,12]
    moveZeroes(nums)
    expected_result = [1,3,12,0,0]
    print("test1 통과" if nums == expected_result else "test1 실패")
    
    nums = [0]
    moveZeroes(nums)
    expected_result = [0]
    print("test2 통과" if nums == expected_result else "test2 실패")