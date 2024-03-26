# [Leetcode 1732] Find the Highest Altitude
"""
문제
road trip : n+1 points at different altitudes.
starts at 0 (altitude가 0)

int array gain은 길이가 n, 
gain[i]는 net gain in altitude between i, i+1
return highest altitude of a point

아이디어
일단 각 point의 altitude는 n+1개임. (0 start point)
gain에서 앞에서부터 현재 element까지의 합이 i+1번째 point에서의 altitude임.

해결전략
:누적합과 max_altitude=0을 활용한다.
1. 1번째 altitude인 now_altitude = 0
2. i+1번째 altitude는 now_altitude += gain[i]   
3. max_altitude < now_altitude이면 max_altitude update
4. return max_altitude
"""

def largestAltitude(gain):
    now_altitude = 0
    max_altitude = 0
    
    for i in gain :
        now_altitude += i
        if max_altitude < now_altitude :
            max_altitude = now_altitude
    
    return max_altitude

if __name__ == "__main__":
    gain = [-5, 1, 5, 0, -7]
    expected_result = 1
    result = largestAltitude(gain)
    print(result)
    print("test1 통과" if expected_result == result else "test1 실패")
    
    gain = [-4, -3, -2, -1, 4, 3, 2]
    expected_result = 0
    result = largestAltitude(gain)
    print(result)
    print("test2 통과" if expected_result == result else "test2 실패")
    