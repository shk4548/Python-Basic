class Point:
    # 클래스 멤버
    instance_count = 0

    #   클래스 이름 공간에 생성, 모든 인스턴스에서 객체 공유
    # 인스턴스 메서드의 첫 번째 인자는 항상 self
    def setX(self, x):
        self.x = x  # self는 인스턴스 자신

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    # 생성자 : __init__
    def __init__(self, x = 0, y = 0):   # x, y를 생성자 매개변수
        self.x, self.y = x, y
        Point.instance_count += 1

    # 소멸자 : __del__
    def __del__(self):
        Point.instance_count -= 1

    # 문자열 출력 포맷
    def __str__(self):
        return "Point x={}, y={}".format(self.x, self.y)

    # 문자열 출력 포맷
    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    # 연산자 오버로딩 +
    def __add__(self, other):
        # Point + other
        if isinstance(other, Point):    # + Point
            self.x += other.x
            self.y += other.y
        elif isinstance(other, int):    # + int
            self.x += other
            self.y += other

        return self