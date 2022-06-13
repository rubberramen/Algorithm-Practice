"""<day33_백준 1152_단어의 개수>

# 문제
- 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

## 입력
- 첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1,000,000을 넘지 않는다. 단어는 공백 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다. 또한 문자열은 공백으로 시작하거나 끝날 수 있다.

## 출력
- 첫째 줄에 단어의 개수를 출력한다.

## 문제 링크
- https://www.acmicpc.net/problem/1152
"""

# case1 : https://wook-2124.tistory.com/223
print(len(input().split()))

# case2 : https://roseline124.github.io/algorithm/2019/03/29/Altorithm-baekjoon-1152.html
string = input("")
if string == " ":  # 문장 자체가 공백인 경우
    print(0)
else:
    words = string.split(" ")  # 띄어쓰기로 구분

    while '' in words:  # 문장 양쪽에 있는 공백이 없어질 때까지 반복
        words.remove('')

print(len(words))

# case3 : https://roseline124.github.io/algorithm/2019/03/29/Altorithm-baekjoon-1152.html
string = input("")
words = string.split(" ")
words = [w for w in words if w != ""] # 공백이 아닌 경우에만 words에 넣음 # 리스트 조건제시법
print(len(words))




