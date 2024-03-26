'''
문제 이해
    flowerbed: integer array {0: empty, 1: not empty}
    no adjecent flower rule 있음

    return 
    n개 flower 심을 수 있으면 true
    없으면 false
    
풀이
    1부터 다음 1까지 몇 개의 꽃을 심을 수 있는지 세어서 모두 더하자.
    
    사이에 0의 개수와 심는 꽃의 개수를 보자
    0->0
    1->0
    2->0
    3->1
    4->1
    5->2
    
    0의 개수가 k개 이면
    꽃의 수 = max(0, (k-1)//2)
        
    edge에 대해서는 꽃의 수 = k // 2 이다.
        귀찮으니까, 맨 앞이랑 맨 뒤에 [1, 0], [0, 1]을 padding 하자
        
필요한 능력
    max로 relu 구현하기
    case 뜯어보기
    edge에 패딩하기
    list 덧셈
''' 
def canPlaceFlowers(flowerbed, n):
    num_of_zero = 0
    result = 0
    flowerbed = [0] + flowerbed + [0, 1]

    for item in flowerbed:
        if item == 0:
            num_of_zero += 1
        else:
            result += max(0, (num_of_zero-1) // 2)
            num_of_zero = 0
    
    return  n <= result


if __name__ == "__main__":
    flowerbed = [1,0,0,0,1]
    n = 1
    output = canPlaceFlowers(flowerbed, n)
    expected = True
    print(output)
    print(expected)
    print()

    flowerbed = [1,0,0,0,1]
    n = 2
    output = canPlaceFlowers(flowerbed, n)
    expected = False
    print(output)
    print(expected)
    print()