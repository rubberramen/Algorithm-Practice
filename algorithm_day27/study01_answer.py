"""<day27_백준 1157_단어 공부>
# 문제
- 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
- 단, 대문자와 소문자를 구분하지 않는다.

## 입력
- 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

## 출력
- 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
- 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

## 문제 링크
- https://www.acmicpc.net/problem/1157
"""

"""
블로그 정답 : https://ooyoung.tistory.com/70
"""

words = input().upper()
unique_words = list(set(words))                # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)                       # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :         # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])