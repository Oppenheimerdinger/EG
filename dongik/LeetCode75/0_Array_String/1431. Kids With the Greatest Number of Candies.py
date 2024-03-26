'''
n: int (num of kids)
candies[i]: int array
extraCandies: int
result: bullian array

max(candies) <= extraCandies + candies[i] : 이 식을 만들어 내는 것이 핵심
result[i] = True 

python 은 list에서 max를 바로 찾을 수 있음.

argmax는 아래처럼 함.
output = [0.1,0.25, 0.3 ,0.2 ,0.1,0.05]
f = lambda i: output[i]
argmax_i = max(range(len(output)), key=f)
'''

def kidsWithCandies(candies, extraCandies):
    n = len(candies)
    result = [0 for i in range(n)]
    for i in range(n):
        if extraCandies + candies[i] >= max(candies):
            result[i] = True
        else:
            result[i] = False
    return result



if __name__ == '__main__':
    candies = [2,3,5,1,3]
    extraCandies = 3
    expected = [True,True,True,False,True]
    output = kidsWithCandies(candies, extraCandies)
    print(f'Output:\t\t{output}')
    print(f'Expected:\t{expected}')
    
    candies = [4,2,1,1,2]
    extraCandies = 1
    expected = [True,False,False,False,False]
    output = kidsWithCandies(candies, extraCandies)
    print(f'Output:\t\t{output}')
    print(f'Expected:\t{expected}')
    
    candies = [12,1,12]
    extraCandies = 10
    expected = [True,False,True]
    output = kidsWithCandies(candies, extraCandies)
    print(f'Output:\t\t{output}')
    print(f'Expected:\t{expected}')