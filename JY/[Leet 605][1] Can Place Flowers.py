#605. Can Place Flowers

""" 대규칙 : flowers들이 adjacent 영역에 심어질 수 없다
0인 구간에만 심길 수 있다.

문제 접근
1) for loop을 돈다.
2) 만약 i번째 index가 1이면 -> 다다음 index부터 n이 시작할 수 있다.
3) n이 시작된 후에, while 해당 index가 0인 동안 n이 이어짐. 
   만약 중간에 while문 다 못 돌고 끝나면 False
4) 그리고 n이 시작되고 그 갯수만큼 이어졌으면, 

문제접근 2
1) flowerbed의 복제본을 하나 만든다.
2) flowerbed for loop안에 n개수만큼 for loop을 돌면서 
   flowerbed[i] 값과 flowerbed[i+1]이 0일 때만 i+1번째 자리를 1로 바꾼다.
3) 다 돌았는데 마지막 1의 다음 index값이 0이 아니면 False
4) else True


"""
def canPlaceFlowers(flowerbed, n) -> bool:
    
    flowerbed_cp = flowerbed
    count = n
    
    for i in range(len(flowerbed)-1):
        #for j in range(n):
        while count > 0 :
            if flowerbed_cp[i] == 0 and flowerbed_cp[i+1]==0:
                flowerbed_cp[i+1] = 1
                count -= 1
            if flowerbed_cp[i] == 1 :
                return False
                #고민되는 사항 : 충돌하는 상황을 어떻게 조건설정
        if flowerbed_cp[i] == 1 and flowerbed_cp[i+1] == 1:
            return False
    return True 
#<문제 재이해> 새로 심을 때도 연속하면 안됨!!
# 000이면 가운데를 1로 바꾸고 , count -=1 

if __name__ == '__main__':
    flowerbed = [1,0,0,0,1]
    n = 1
    answer = canPlaceFlowers(flowerbed, n)
    print(answer)

    flowerbed = [1,0,0,0,1]
    n = 2
    answer = canPlaceFlowers(flowerbed, n)
    print(answer)