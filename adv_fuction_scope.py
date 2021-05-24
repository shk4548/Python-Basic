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