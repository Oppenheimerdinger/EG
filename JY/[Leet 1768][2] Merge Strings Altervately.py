#1768. Merge Strings Altervately

""" word1, word2를 교차로 추가한다.
    조건 비교를 어떻게 할 것인가.
    기준은 word1, word2 각각의 길이
    0) 일단 i를 가지고 index 단위로 str 접근. 
       (for 문 : 마지막은 max(len(word1), len(word2)))
    1) i < min(len(word1), len(word2)) -> 하나씩 교차로
    2) i가 1)보다는 크고 max(len(word1), len(word2)) 보다는 작을 떼
        -> str[i:-1] 까지 붙여넣기
"""    

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ''
        for i in range(max(len(word1), len(word2))): #이건 max로 굳이 안 해도 되지 않나?
            if i < min(len(word1), len(word2)):
                result += word1[i]
                result += word2[i]
            else:
                result += word1[i:]  #[k:]로 해야 끝까지 뱉음. [i:-1]은 마지막 요소 제외하고 뱉는 것임.
                result += word2[i:]
                return result
        return result
    


