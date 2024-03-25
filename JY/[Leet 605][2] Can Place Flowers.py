#605. Can Place Flowers

'''
문제 이해
- 대규칙 : 꽃들은 연속해서 심어질 수 없다. 010 형태가 무조건 이어져야 한다.


문제 접근
flowerbed의 처음과 마지막에 0을 padding 한다. (그려면 길이가 총 len(flowerbed) + 2 가 됨)
count를 n으로 초기화
flowerbed만큼 for loop(시작은 index 1부터, 마지막은 len(flowerbed)+1까지)을 돌면서 i-1번째 index, i번째 index, i번째 index의 값을 check 한다.
만약 i-1, i, i+1의 값이 모두 0이면 i를 1로 바꾸고 & count -= 1을 한다.
for loop을 다 돌았는데 count가 0이면 True 아니면 False임.
'''

def canPlaceFlowers(flowerbed, n)->bool:
    flowerbed_cp = [0] + flowerbed + [0]
    count = n
    for i in range(1, len(flowerbed)+1):
        if flowerbed_cp[i-1] == 0 and flowerbed_cp[i] == 0 and flowerbed_cp[i+1] == 0:
            flowerbed_cp[i] = 1
            count -= 1
    if count <= 0 :
        return True
    else:
        return False

if __name__ == '__main__':
    flowerbed = [1,0,0,0,1]
    n = 1
    answer = canPlaceFlowers(flowerbed, n)
    print(answer)

    flowerbed = [1,0,0,0,1]
    n = 2
    answer = canPlaceFlowers(flowerbed, n)
    print(answer)
