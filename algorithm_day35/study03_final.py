"""<day33_백준 16916_부분 문자열>

# 문제
- 문자열 S의 부분 문자열이란, 문자열의 연속된 일부를 의미한다.
- 예를 들어, "aek", "joo", "ekj"는 "baekjoon"의 부분 문자열이고, "bak", "p", "oone"는 부분 문자열이 아니다.
- 문자열 S와 P가 주어졌을 때, P가 S의 부분 문자열인지 아닌지 알아보자.

## 입력
- 첫째 줄에 문자열 S, 둘째 줄에 문자열 P가 주어진다. 두 문자열은 빈 문자열이 아니며, 길이는 100만을 넘지 않는다. 또, 알파벳 소문자로만 이루어져 있다..

## 출력
- P가 S의 부분 문자열이면 1, 아니면 0을 출력한다.

## 문제 링크
- https://www.acmicpc.net/problem/16916
"""

def getPI(pattern):
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

def KMP(s, pattern):
    getPI(pattern)
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = pi[j - 1]
        if s[i] == pattern[j]:
            if j == len(pattern) - 1:
                return True
            else:
                j += 1
    return False

s = input()
pattern = input()
pi = [0 for x in range(len(pattern))]

if KMP(s, pattern):
    print('1')
else:
    print('0')