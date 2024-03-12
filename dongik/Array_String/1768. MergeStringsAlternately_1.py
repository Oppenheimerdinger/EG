'''
word1, word2
mergesort인데, 크기 비교는 안 하는 버전인듯함.
len(word1), len(word2), i 의 크기를 비교해서 무엇을 빼올지 결정함.
'''

def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    ans = ""
    for i in range(max(len(word1), len(word2))):
        if(i < min(len(word1), len(word2))):
            ans += word1[i]
            ans += word2[i]
        else:
            if (len(word1) < len(word2)):
                ans += word2[i]
            else:
                ans += word1[i]
    return ans

if __name__ == '__main__':
    word1 = "abc"
    word2 = "pqr"
    ans = mergeAlternately(word1, word2)
    print(ans)
    
    word1 = "ab"
    word2 = "pqrs"
    ans = mergeAlternately(word1, word2)
    print(ans)
    
    word1 = "abcd"
    word2 = "pq"
    ans = mergeAlternately(word1, word2)
    print(ans)