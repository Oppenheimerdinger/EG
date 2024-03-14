#1431. Kides With the Greatest Number of Candies

# candies : integer array
# candies[i] 는 i번째 kid의 candy개수
# estraCandies : #of extra candies that you have
    
# return은 boolean array인 result of length n인데
# 만약 i번째 kid가 extraCandies를 모두 가져가면 
# 가장 많은 수의 candy를 가지게 될 경우 True
# i번째 kid가 extraCandies를 모두 가져가도 가장 많은 수의
# candy를 가지지 않는다면 False
# 가장 많은 수의 candy는 여러 명이 가지는 것일수도 있음!

""" 풀이 전략
1. candies를 돌면서 max값을 확인한다.
2. max값에서 candies[i]를 뺀 값이 extraCandies보다 크면 False,
작으면 True
3. 1번에 대한 for loop을 돌리고
4. 2번에 대한 for loop을 돌려서 결과 list를 return

"""

def kidsWithCandies(candies, extraCandies):
        # """
        # :type candies: List[int]
        # :type extraCandies: int
        # :rtype: List[bool]
        # """
    max = 0
    for candy in candies:
        if max < candy :
            max = candy   #더 간편하게 하는 법 : max(list) 쓰면 list에서의 max값을 바로 찾을 수 있음!
    
    check_list = [False]*len(candies)
    
    for i in range(len(candies)):
        if max-candies[i] > extraCandies:
            continue
        else:
            check_list[i] = True
            
    return check_list
    
        

if __name__ == '__main__':
    candies = [2,3,5,1,3]
    extraCandies = 3
    result = kidsWithCandies(candies, extraCandies)
    print(result)
    
    candies = [4,2,1,1,2]
    extraCandies = 1
    result = kidsWithCandies(candies, extraCandies)
    print(result)
    
    candies = [12,1,2]
    extraCandies = 10
    result = kidsWithCandies(candies, extraCandies)
    print(result)
