'''
String에서 모음만 순서를 뒤집기

vowels에 모음을 모아서
앞에서부터 교체하기
'''

def reverseVowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    s_vowels = ''
    ans = ''
    
    # s에서 vowel 만 모아보자
    for c in s:
        if c in vowels:
            s_vowels += c

    # ans를 재생성 해보자.
    i_ptr = 1
    for c in s:
        if c in vowels:
            ans += s_vowels[-i_ptr]
            i_ptr += 1
        else:
            ans += c
               
    return ans

if __name__ == "__main__":
    s = "hello"
    output = reverseVowels(s)
    expected = "holle"
    print(expected)
    print(output)
    print()
    
    s = "leetcode"
    output = reverseVowels(s)
    expected = "leotcede"
    print(expected)
    print(output)