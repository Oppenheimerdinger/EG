def kidsWithCandies(candies, extraCandies):
    #list element 중 max값을 찾는다
    #extra candies를 원래 candies list에 각각 더했을때 max보다 크면 True 아니면 False
    
    #1. list element 중 max값 찾기
    max_num = 0
    for ele in candies:
        if ele > max_num:
            max_num = ele
    
    #2. 각각 더했을때 max보다 크면 True 아니면 False인 리스트 만들기
    result_list = [False]*len(candies)
    for i in range(len(result_list)):
        if candies[i]+extraCandies >= max_num:
            result_list[i] = True
    return result_list

if __name__ == '__main__':
    candies = [2,3,5,1,3]
    extraCandies = 3
    k1 = kidsWithCandies(candies, extraCandies)
    print(k1)
