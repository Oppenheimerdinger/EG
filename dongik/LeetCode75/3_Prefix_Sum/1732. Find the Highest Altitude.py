'''
문제:
    i 가지 prefix sum 중에 최대값 찾기
    gain[i]: [i] point와 [i+1] point의 고도 차이

풀이:
    i point 의 고도 = gain[:i]의 총 합
    앞에서부터 고도를 차례로 구해서 최대를 찾자

필요 능력:
    이 문제가 prefix sum인지 알아보기
    sliding window랑 좀 비슷한듯?
'''

def largestAltitude(gain):
    val = 0
    maxVal = 0
    for t in gain:
        val += t
        if val > maxVal:
            maxVal = val
    return maxVal
        
if __name__ == "__main__":
    gain = [-5,1,5,0,-7]
    output = largestAltitude(gain)
    expected = 1
    print(output)
    print(expected)
    print()
    
    gain = [-4,-3,-2,-1,4,3,2]
    output = largestAltitude(gain)
    expected = 0
    print(output)
    print(expected)
    print()