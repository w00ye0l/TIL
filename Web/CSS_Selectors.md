# CSS Selectors

## 선택자(Selector) 유형

- 기본 선택자
  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자
- 결합자(Combinators)
  - 자손 결합자, 자식 결합자
  - 일반 형제 결합자, 인접 형제 결합자
- 의사 클래스/요소(Pseudo Class)
  - 링크, 동적 의사 클래스
  - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

<br/>

## CSS 선택자 정리

- 요소 선택자
  - HTML 태그를 직접 선택
- 클래스(class) 선택자
  - 마침표(.) 문자로 시작하며, 해당 클래스가 적용된 항목을 선태가
- 아이디(id) 선택자
  - `#` 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
  - 일반적으로 하나의 문서에 1번만 사용
  - 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장

<br/>

## CSS 적용 우선순위 (cascading order)

1. 중요도 (Importance) : 사용시 주의
   - `!important`
2. 우선 순위 (Specificity)
   - 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
3. CSS 파일 로딩 순서

<br/>

## CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
  - 속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있다.
  - 상속되는 것 예시
    - 예) TEXT 관련 요소(font, color, text-align), opacity, visibility 등
  - 상속되지 않는 것 예시
    - 예) Box model 관련 요소(width, height, margin, padding, border, box-sizing, display), position 관련 요소(position, top/right/bottom/left, z-index) 등

<br/>

# CSS Box model

## CSS 원칙 1

> 모든 요소는 **네모(박스 모델)**이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다. (좌측 상단부터 배치)

<br/>

## Box model

- 모든 HTML 요소는 box 형태로 되어있음

- 하나의 박스는 네 부분(영역)으로 이루어짐

  - `margin` : 테두리 바깥의 외부 여백, 배경색을 지정할 수 없음

  - `border` : 테두리 영역

  - `padding` : 테두리 안쪽의 내부 여백 요소에 적용된 배경색, 이미지는 padding까지 적용

  - `content` : 글이나 이미지 등 요소의 실제 내용

    ```css
    .margin {
        /* 상하좌우 */
        margin: 10px;
        /* 상하, 좌우 */
        margin: 10px 20px;
        /* 상, 좌우, 하 */
        margin: 10px 20px 30px;
        /* 상, 우, 하, 좌 (시계 방향) */
        margin: 10px 20px 30px 40px;
    }
    
    .border {
    	border-width: 2px;
        border-style: dashed;
        border-color: black;
        /* 축약 */
        border: 2px dashed black;
    }
    ```

<br/>

## Box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box
  - Padding을 제외한 순수 contents 영역만을 box로 지정
- 다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px로 보는 것을 원함
  - 그 경우 box-sizing을 border-box로 설정

<br/>

# CSS Display

## CSS 원칙 2

> Display에 따라 크기와 배치가 달라진다.

<br/>

## 대표적으로 활용되는 display

- display: block
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지한다.
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.
- display: inline
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지한다.
  - width, height, margin-top, margin-bottom을 지정할 수 없다.
  - 상하 여백은 line-height로 지정한다.

### 블록 레벨 요소와 인라인 레벨 요소

- 블록 레벨 요소와 인라인 레벨 요소 구분 (HTML 4.1까지)
- 대표적인 블록 레벨 요소
  - div / ul, ol, li / p / hr / form 등
- 대표적인 인라인 레벨 요소
  - span / a / img / input, label / b, em, i, strong 등
- block의 기본 너비는 가질 수 있는 너비의 100%
  - 너비를 가질 수 없다면 자동으로 부여되는 margin
- inline의 기본 너비는 컨텐츠 영역만큼

<br/>

### 속성에 따른 수평 정렬

```css
.box {
    /* 왼쪽 정렬 */
    margin-right: auto;
    /* 오른쪽 정렬 */
    margin-left: auto;
    /* 가운데 정렬 */
    margin-right: auto;
    margin-left: auto;
}
```

<br/>

### display

- display: inline-block
  - block과 inline 레벨 요소의 특징을 모두 가짐
  - inline처럼 한 줄에 표시할 수 있고, block처럼 width, height, margin 속성을 모두 지정할 수 있음
- display: none
  - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
  - 이와 비슷한 visibility: hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.
- [https://developer.mozilla.org/ko/docs/Web/CSS/display](https://developer.mozilla.org/ko/docs/Web/CSS/display)