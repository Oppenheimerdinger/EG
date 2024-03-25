#leetcode 345. Reverse Vowerls of a String

"""
- 문제 : s가 주어졌을 때, reverse only all the vowels in the string and return it.
aeiou


- 해결 접근
1. 모음의 index와 어떤 모음인지 저장하는 dictionary (key : index, value : 해당 vowel)
2. 가장 중간 key에서부터 value 값을 서로 바꿔주기(이게되나)
3. s에 대해 for문 돌면서 해당하는 value 값으로 바꿔주기

-다시 생각
1. s에 대해서 for문을 돌면서 s[i]가 모음 중 하나에 해당하면 
새로운 vowel_list에 넣어주기
2. 위 for문이 끝나면 vowel_list를 reverse해주기
3. s에 대해 다시 for문을 돌면서 모음이 나올때마다 vowel_list에서
첫번째 요소를 찾아서 넣어주고, 그 요소를 삭제해버리기. (그럼 항상 첫번째 요소임)
-> 2,3을 동시에 할 수 있는 방법 : vowel_list.pop() 사용


"""

'''
def reverseVowels(s):
    vowel_list = []
    
    for i in range(len(s)):
        if s[i] in ('a','e','i','o','u'):
            vowel_list.append(s[i])
    for i in range(len(s)):
        if s[i] in ('a','e','i','o','u'):
            new_vowel = vowel_list.pop()
            s[i] = new_vowel  #여기서 error 발생 : str은 item assignment가 안된다 함.
    return s
'''    

def reverseVowels(s): 
    consonant_list = []
    vowel_list = []
    new_word =''
    N = len(s)
    for i in range(N):
        if s[i] in ('a','e','i','o','u', 'A','E','I','O','U'):
            vowel_list.append(s[i])
        else :
            consonant_list.append(s[i])
    consonant_list.reverse()
    for i in range(N):
        if s[i] in ('a','e','i','o','u', 'A','E','I','O','U'):
            new_vowel = vowel_list.pop()
            new_word += new_vowel
        else:
            new_word += consonant_list.pop()
    
    return new_word
        
# def reverseVowels(s):     #더 빨리 할 수 있는 방법
#     vowel_list = []
#     new_word= ''
#     for i in range(len(s)):
#         if s[i] in "aeiouAEIOU": 
#             vowel_list.append(s[i])
#     for i in range(len(s)):
#         if s[i] in "aeiouAEIOU":
#             new_vowel = vowel_list.pop()
#             new_word += new_vowel
#         else:
#             new_word += s[i]
    
#     return new_word
    
        
    

if __name__ == '__main__':
    s = 'hello'
    result = reverseVowels(s)
    expected_result = 'holle'
    print("test_1 통과" if result == expected_result else "test_1 실패")
    
    s = 'leetcode'
    result = reverseVowels(s)
    expected_result = 'leotcede'
    print("test_2 통과" if result == expected_result else "test_2 실패")