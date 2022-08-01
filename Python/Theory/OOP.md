# 객체지향 프로그래밍(Object Oriented Programming)
> 파이썬은 모두 객체(object)로 이뤄져 있다.
> 
> 객체(object)는 특정 타입의 인스턴스(instance)이다.
- 123, 900, 5는 모두 int의 인스턴스
- 'hello', 'bye'는 모두 string의 인스턴스
- [232, 89, 1], []은 모두 list의 인스턴스

## 객체
- 객체(object)의 특징
    - 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
    - 속성(attribute) : 어떤 상태(데이터)를 가지는가?
    - 조작법(method) : 어떤 행위(함수)를 할 수 있는가?
- 객체지향 프로그래밍이란?
    - 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법

## 절차지향 프로그래밍 VS 객체지향 프로그래밍
- 절차지향 프로그래밍
    - 데이터와 함수로 인한 변화
    ```python
    a = 10
    b = 30
    square1_area = a * b
    square1_circumference = 2 * (a + b)

    c = 300
    d = 20
    square2_area = c * d
    square2_circumference = 2 * (c + d)
    
    #############

    def area(x, y):
      return x * y

    def circumference(x, y):
      return 2 * (x + y)

    a = 10
    b = 30
    c = 300
    d = 20
    square1_area = area(a, b)
    square1_circumference = circumference(a, b)
    square2_area = area(c, d)
    square2_circumference = circumference(c, d)
    ```
- 객체지향 프로그래밍
    - 데이터와 기능(메소드) 분리, 추상화된 구조(인터페이스)
    ```python
    class Rectangle:
      def __init__(self, x, y):
        self.x = x
        self.y = y

      def area(self):
        return self.x * self.y

      def circumference(self):
        return 2 * (self.x + self.y)
    
    r1 = Rectangle(10, 30)
    r1.area()
    r1.circumference()

    r2 = Rectangle(300, 20)
    r2.area()
    r2.circumference()

    # 사각형 - 클래스(class)
    # 각 사각형(R1, R2) - 인스턴스(instance)
    # 사각형의 정보 - 속성(attribute)
    ## 가로 길이, 세로 길이
    # 사각형의 행동/기능 - 메소드(method)
    ## 넓이를 구한다. 높이를 구한다.
    ```

## 객체지향의 장점
- 객체 지향 프로그래밍은 **프로그램을 유연하고 변경이 용이**하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용됨
- 또한, 프로그래밍을 더 배우기 쉽게 하고 **소프트웨어 개발과 보수를 간편하게** 하며, 보다 **직관적인 코드 분석**을 가능하게 하는 장점을 가지고 있음

# OOP 기초
- 기초 문법
  ```python
  # 클래스 정의
  class MyClass:
    pass
  # 인스턴스 생성
  my_instance = MyClass()
  # 메서드 호출
  my_instance.my_method()
  # 속성
  my_instance.my_attribute
  ```
- 객체의 틀(클래스)을 가지고, 객체(인스턴스)를 생성

- 클래스와 인스턴스
    - 클래스 : 객체들의 분류(class)
    - 인스턴스 : 하나하나의 실체/예(instance)
    - **파이썬은 모든 것이 객체, 모든 객체는 특정 타입의 인스턴스**
    ```python
    class Person:
      pass

    print(type(Person))
    # type
    p1 = Person()
    print(type(p1))
    # __main__.Person
    print(isinstance(person1, Person))
    # True
    ```

- 속성
    - 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미
    ```python
    class Person:

      def __init__(self, name):
        self.name = name


    person1 = Person('지민')
    print(person1.name)
    ```

- 메소드
    - 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)
    ```python
    class Person:

      def talk(self):
        print('안녕')

      def eat(self, food):
        print(f'{food}를 냠냠')

    
    person1 = Person()
    person1.talk()
    # 안녕
    person1.eat('피자')
    # 피자를 냠냠
    person1.eat('치킨')
    # 치킨를 냠냠
    ```

- 객체 비교하기
    - `==`
        - 동등한(equal)
        - 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True
        - 두 객체가 같이 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님
    - `is`
        - 동일한(identical)
        - 두 변수가 동일한 객체를 가리키는 경우 True(주소를 비교해줌)

    ```python
    a = [1, 2, 3]
    b = [1, 2, 3]

    print(a == b, a is b)
    # True False

    ##############

    a = [1, 2, 3]
    b = a

    print(a == b, a is b)
    # True True
    ```

- 인스턴스 변수
    - 인스턴스가 개인적으로 가지고 있는 속성(attribute)
    - 각 인스턴스들의 고유한 변수
    - 생성자 메소드에서 `self.<name>`으로 정의
    - 인스턴스가 생성된 이후 `<instance>.<name>`으로 접근 및 할당

    ```python
    class Person:

      def __init__(self, name):
        self.name = name

    
    john = Person('지민')
    print(john.name)
    # john
    john.name = 'John Kim'
    print(john.name)
    # John Kim
    ```

- 인스턴스 메소드
    - 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드
    - 클래스 내부에 정의되는 메소드의 기본
    - 호출 시, 첫 번째 인자로 인스턴스 자기자신(self)이 전달됨
    ```python
    class MyClaa

      def instance_method(self, arg1, ...)

    my_instance = MyClass()
    my_instance.instance_method(...)
    ```

- self
    - 인스턴스 자기자신
    - 파이썬에서 인스턴스 메소드는 호출 시 첫 번째 인자로 인스턴스 자신이 전달되게 설계
        - 매개변수 이름으로 `self`를 첫 번째 인자로 정의
        - 다른 단어로 써도 작동하지만, 파이썬의 암묵적인 규칙

- 생성자(constructor) 메소드
    - 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
    - 인스턴스 변수들의 초기값을 설정
        - 인스턴스 생성
        - `__init__` 메소드 자동 호출
    ```python
    class Person:

      def __init__(self):
        print('인스턴스가 생성')
    
    person1 = Person()
    # 인스턴스가 생성

    ############

    class Person:

      def __init__(self, name):
        print(f'{name} 인스턴스가 생성')
    
    person1 = Person('지민')
    # 지민 인스턴스가 생성
    ```

- 소멸자(destructor) 메소드
    - 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메소드
    ```python
    class Person:

      def __del__(self):
        print('인스턴스 삭제')

      person1 = Person()
      del person1
      # 인스턴스 삭제
    ```