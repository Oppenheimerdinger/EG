'''
문제:
    set1에만 있는 distinct 숫자 리스트
    set2에만 있는 distinct 숫자 리스트
풀이:
    각 list에서 distinct인 숫자만 모아서 set으로 만듦
    서로 차집합 하면 됨
팁:
    차집합은 set끼리 빼면 됨
'''

def findDifference(nums1, nums2):
    s1 = set(nums1)
    s2 = set(nums2)
    return [list(s1-s2), list(s2-s1)]
    
if __name__ == '__main__':
    nums1 = [1,2,3]
    nums2 = [2,4,6]
    expected = [[1,3],[4,6]]
    output = findDifference(nums1, nums2)
    print(expected)
    print(output)
    print()
    
    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]
    expected = [[3],[]]
    output = findDifference(nums1, nums2)
    print(expected)
    print(output)
    print()