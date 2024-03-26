'''
word1, word2 를 mergeSort하듯 합치는데, 크기 비교 하는 부분은 없는 문제.
짧은 word 전까지는 하나씩 빼온다.
꼬다리는 그냥 뒤에 바로 붙인다.
'''

def mergeAlternately(word1, word2):
    ans = ''
    for i in range(min(len(word1), len(word2))):
        ans += word1[i]
        ans += word2[i]
    if(len(word1)>len(word2)):
        ans += word1[len(word2):]
    else:
        ans += word2[len(word1):]
    return ans

if __name__ == '__main__':
    word1 = 'abc'
    word2 = 'pqr'
    ans = mergeAlternately(word1, word2)
    print(ans)
    
    word1 = 'ab'
    word2 = 'pqrs'
    ans = mergeAlternately(word1, word2)
    print(ans)
    
    word1 = 'abcd'
    word2 = 'pq'
    ans = mergeAlternately(word1, word2)
    print(ans)
    