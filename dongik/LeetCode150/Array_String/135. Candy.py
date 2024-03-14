'''
given
n: children in the line
ratings: rating value (integer array)

Restriction
Each child at least one candy
higher rating -> more candies than neighor

minimum number of candies required
caides 를 1로 초기화 하고
step1. 연속한 오름차순을 따라 candy 숫자를 올림
step2. 반대방향 스캔 -> 연속한 오름차순을 따라 candy 숫자를 올림

step1의 오름차순의 끄트머리를
step2에서 떨어뜨리지 않게 조심

edge case: 빈 리스트가 인풋
'''

def candy(ratings):
    n = len(ratings)
    candies = [1] * n
    for i in range(n-1):
        if (ratings[i+1] > ratings[i]):
            candies[i+1] = candies[i] + 1
    for i in range(1, n):
        if (ratings[-i-1] > ratings[-i] and candies[-i-1] <= candies[-i]):
            candies[-i-1] = candies[-i] + 1
        
    s = 0
    for i in candies:
        s += i
    
    return s

if __name__ == "__main__":
    ratings = []
    ans = candy(ratings)
    print(ans)
    
    ratings = [1,0,2]
    ans = candy(ratings)
    print(ans)
    
    ratings = [1,2,2]
    ans = candy(ratings)
    print(ans)
    
    ratings = [1,3,4,5,2] # 11
    ans = candy(ratings)
    print(ans)