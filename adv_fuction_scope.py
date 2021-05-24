# 함수 스코핑 룰
x =1  # Global

def scope_func(a):
    return a + x  # Local 스코프에 x 가 없음 > 글로버 x 를 참조

def scope_func2(a):
    x = 2
    return a + x

print(scope_func(10))
print(scope_func2(10))
print("global x:", x)       # scope_func2에서 x가 치한되었지만 global x는 변경되지 않음

g = 1 # 글로벌 변수

def scope_func3(a):
    global g
    g = 3
    return a + g

print(scope_func3(10))
print("global g:", g)

# 글로벌 영역의 확인
print(dir())    # globals
# 내장 영역의 확인
print("내장영역:", dir('__builtins__'))
