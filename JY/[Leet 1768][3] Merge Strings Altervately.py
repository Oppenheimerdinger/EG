#1768. Merge Strings Altervately
"""
0) return 형태는 str. 빈 str에다가 덧붙이는 형태로 하자.
1) index에 접근하기 위한 i를 활용한다. (for 문)
2) 종결 조건을 어디까지 해야할 것인가.
    : word1, word2의 길이 중 짧은 것까지 하면 된다.
    : 더 긴 것은 그냥 끝까지 갖다붙이면 되니까
3) min(len(word1), len(word2))-1번째 인덱스까지는 교차로 붙임
   (i가 min 보다 작을 때!)
   (만약 두 str의 길이가 같다면 여기서 종결될 것)
4) 딱 min(len(word1, len(word2))일 때는 더 긴 str의 [i:]까지 붙이면 됨
   : min(len(word1), len(word2))를 활용하려면 for문 조건에는 +1 반드시 포함
    
"""
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        result = ''
        for i in range (min(len(word1), len(word2))+1):
            if i == min(len(word1), len(word2)):
                result += word1[i:]
                result += word2[i:]
            else:
                result += word1[i]
                result += word2[i]
        return result
        


    


