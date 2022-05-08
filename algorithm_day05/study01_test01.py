"""
<문제>
    1!+2!+3!+4!+5!+...+10!
    답 : 4037913
"""

# 펙토리얼 테스트 : 3! = 6
a = 1
for i in range(1, 3+1):
    a *= i
print(a)
print()

# 펙토리얼 테스트 : 4! = 24
a = 1
for i in range(1, 4+1):
    a *= i
print(a)
