'''
given
n: children in the line
ratings: rating value (integer array)

Restriction
Each child at least one candy
higher rating -> more candies than neighor

minimum number of candyies required

updown list 생성
    말 그대로 옆이랑 updown 만 함
    리스트의 시작은 1
리스트의 최솟값을 찾아서 해당 값이 1이 되도록, 모든 원소에 똑같은 값을 더해줌,
    최솟값 + 더할 값 = 1
    더할 값 = 1 - 최솟값
리스트의 모든 값을 합함.

edge case: 빈 리스트가 인풋

'''

def candy(ratings):
    if len(ratings)==0:
        return 0
    updown = [1]
    for i in range(len(ratings) - 1):
        if ratings[i+1] > ratings[i]:
            updown.append(updown[-1] + 1)
        elif ratings[i+1] < ratings[i]:
            updown.append(updown[-1] - 1)
        else:
            updown.append(1)
    adder = 1 - min(updown)
    
    for i in range(len(updown)):
        updown[i] += adder
    s = 0
    for eachCandy in updown:
        s += eachCandy
        
    return s

if __name__ == "__main__":
    ratings = [1,0,2]
    ans = candy(ratings)
    print(ans)
    
    ratings = [1,2,2]
    ans = candy(ratings)
    print(ans)