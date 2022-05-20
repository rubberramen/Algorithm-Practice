
## <코딩 테스트 + 알고리즘 공부 일지>
- 2018 시나공 정보처리기사 실기 책 알고리즘 문제 참조
- 백준(https://www.acmicpc.net/) 문제

### - day15(220521, 토) : 백준 1884_알람 시계
- 해결 완료
- 배운점
  - map 메서드 다시 깊이 이해
- <소회>
  - 결과적으로 최종 정답 코드는 굉장히 간단함
  - 하지만 이걸 도출해내기 위한 논리적 과정은 생각보다 간단하지 않았음
  - 문제 독해 능력과 조건을 나누는 능력을 배양할 필요

### - day14(220520, 금) : 백준 14681_사분면 고르기
- 해결 완료
- <소회>
  - 백준 문제
  - 일단 지나치게 쉬운 느낌이 없지 않지만, 차근차근...

### - day13(220519,목) : 수학 - 시험 성적 출력, 숫자 A, B 비교
- 해결 완료
- 배운점
  - input().split() 사용 방법
  - map 메서드 활용 방법
- <소회>
  - 기분 전환 차원에서 백준 문제 시도, 난이도 쉬운 문제
  - 백준 문제는 입출력이 있기 때문에 고민할 단계가 하나 더 있음
  - 이같은 형식이 코딩 테스트에 더 적합하므로, 병행해서 공부할 예정

### - day12(220518,수) : 수학 - 이진법 변환
- <문제> : 10진수를 2진수로 변환하기
- 해결 완료
- 배운점
  - while문 이해 심화
- <소회>
  - 머리로만 하니 한계를 느낌 -> 종이와 펜 필요!(바람직한 방향인가?)
  - 구글링 결과, 메서드가 따로 있음;;;
  - 효율적인 알고리즘 참고 : https://codeuniv.tistory.com/58

### - day11(220516,월) : 수학 - 소인수분해
- <문제> : 정수를 입력 받아, 소인수를 구해 출력하시오
- 해결 완료
- 배운점
  - 로직이 복잡해지니, 하나의 알고리즘으로 해결하기 힘듦
  - 따라서 문제 해결을 위한 사전 메서드를 만들어야 함
  - 이렇게 스텝을 밟아가는 과정을 잘 익히고, 기획하는 능력을 키워야 할듯
- <소회>
  - 구글링 결과, 더 효율적인 해결 방법들이 많음
  - 값이 작은 수를 판별할 때는, 효율성이 문제가 되지 않지만 숫자가 커지면 속도 차이가 엄청남
  - 지금부터도 이같은 관점으로 고민을 하고, 실력이 더 쌓이면 본격적으로 구현해보기

### - day10(220514,토) : 수학 - 약수 구하기
- <문제> : 정수를 입력 받아, 약수를 구해 출력
- 해결 완료
- 배운점
  - 리스트를 활용한 정답 출력
- <소회>
  - 구글링 해보니, '임의의 자연수 N의 약수들 중에서 두 약수의 곱이 N이 되는 약수 A와 약수 B는 반드시 존재한다'는 규칙을 활용한 효율적 문제풀이 방식이 있음
  - 고민해 보기
  - 그런데, 애초에 수학적 규칙을 모른다면 알고리즘을 짤 수 없을 듯

### - day09(220513,금) : 수학 - 최대공약수, 최소공배수
- <문제> : 두 수를 입력 받아 두 수의 최대공약수와 최소공배수를 계산하여 출력
- 해결 완료
- 배운점
  - for문 더 깊이 이해
  - min, max 로직
- <소회>
  - 구글링 해보니, '유클리드 호제법'이란 방식이 있음
  - 추후 공부하기

### - day08(220512,목) : 수학 - 소수의 합 구하기
- <문제> : 임의의 정수를 입력 받아, 그 안에 포함된 소수의 합을 구하라
- 해결 완료
- 배운점
  - 이중 for문 스스로 고민해서 활용
  - isPrime 불린 변수를 실제로 이용 
- <소회>
  - day07 로직을 가져와, 확장하여 문제 해결

### - day07(220511,수) : 수학 - 소수 판별
- <문제> : 1보다 큰 임의의 정수를 입력받아 소수를 판별하라
- 해결 완료
- 배운점
  - for문 내, break 사용하여 리소스 낭비 방지
- <소회>
  - 가장 간단한 수학 알고리즘 문제

### - day06(220510,화) : 수열06 - 피보나치 수열
- <문제> : 1+1+2+3+5+8+13+...의 수열로 나열되는 피보나치 수열의 20번째 항까지의 합계
- 해결 완료
- 배운점
  - while문 활용 : 상황에 따라 판단하여, for문 vs while문 선택
  - temp 변수 활용
  - 주석 정렬 : 훨씬 깔끔해짐
    - 추후 내용적인 측면도 보완
- <소회>
  - 구글링 해보니, 리스트를 활용한 피보나치 수열 구현도 있음 -> 추후 **스스로** 고민

### - day05(220509,월) : 수열05
- <문제> : 1!+2!+3!+4!+5!+...+10!의 순서로 나열되는 수열의 10번째 항까지의 합계
- 해결 완료
- 배운점
  - 테스트부터 한단계 한단계 진행하며 최종 해결까지 진행
  - 주석을 작성함으로써 나뿐만 아니라, 타인이 볼때 쉽게 이해가도록 코드 작성
- <소회>
  - 차근차근 만들어 간다는 느낌으로 해야지 사고가 꼬이지 않음
  - 주석을 적절하게 활용하자
  - 변수명도 신경쓰자
  - 펙토리얼을 더 효율적으로 구현하는 로직이 많을테니, 추후 테스트 ex)재귀호출

### - day04(220507,토) : 수열04
- <문제> : 1+2+4+7+11+16+22+...의 순서로 나열되는 수열의 20번째 항까지의 합계
- 해결 완료
- 배운점
  - 알고리즘 짤때, 코드 순서에 대한 이해가 조금 깊어짐
  - 문제 해결을 위한 알고리즘은 무한히 많을 수 있겠다고 피부로 느낌
- <소회>
  - 금일 메인 문제에 딸린 추가 문제 못 품
  - 추후 꼭꼭 시도하기!

### - day03(220506,금) : 수열03
- <문제> : (1/2)+(2/3)-(3/4)+(4/5)-(5/6) ... -(99/100)의 합계
- 해결 완료
- 배운점
  - 소수점 처리 : round 메서드
  - 메서드 형태로 정답 출력
- <소회> : 양을 조금 늘려볼까?

### - day02(220505,목) : 수열02
- <문제> : 1-2+3-4+ ... +99-100의 합계
- 해결 완료
  - 확장 문제1 : 1-2+3-4+5-6+ ... +99 -> 해결
  - 확장 문제2 : (-1)×2×(-3)×4×(-5)× ··· ×100  -> 해결
- 배운점
  - 문자열 f-formatting 확실히 습득
  - 서식 지정자 자료형 확인 : https://dojang.io/mod/page/view.php?id=2305
- <소회> : 차근차근, 확실히

### - day01(220504,수) : 수열01, 
- <문제> : 1+2+3+...+100까지 합계
- 해결 완료
  - 확장 문제 : 1+3+5+7+...+99 -> 해결
  - 개선 필요 사항 : 정답을 '잘' 출력하는 방법도 고민 필요
- <소회> : 첫 스타트를 잘 끊었다.



