# JavaScript 활용

## 기본 활용

```html
<script>
    // console 창에 print 해줌
	console.log('hello, js!')
    
    // h1 요소(element)를 만들고
    const title = document.createElement('h1')
    // 텍스트를 추가하고
    title.innerText = 'JS 기초'
    // 선택자로 body 태그를 가져와서
    const body = document.querySelector('body')
    // body 태그에 자식 요소로 추가
    body.appendChild(title)
</script>
```

<br/>

## DOM 조작

```html
<body>
    <h1 id="title">
        JS 기초
    </h1>
    <h2>
        DOM 조작
    </h2>
    <p class="text">
        querySelector
    </p>
    <p class="text">
        querySelectorAll
    </p>
</body>
```

```js
document.querySelector('#title')
// <h1 id="title">JS 기초</h1>

document.querySelector('h2')
// <h2>DOM 조작</h2>

document.querySelectorAll('h2')
// NodeList [h2]

document.querySelectorAll('.text')
// NodeList(2) [p.text, p.text]
```


<br/>

## 변수 선언 예시

### const & let & var

- `var`
  - **전역 변수**로 사용하는 방식
  - 옛날에 사용했던 변수 선언 방식
  - 요즘은 const, let을 더 많이 사용
- `const`
  - 블록 내에서 사용되는 **지역 변수**
  - 변수를 선언 후 변경할 수 없음
  - 변수(객체) 안의 속성 값은 변경 가능
- `let`
  - 블록 내에서 사용되는 **지역 변수**
  - 변수를 선언 후 변경할 수 있음

<br/>

- `var`의 경우 변수 호이스팅(hoisting) 때문에 나중에 선언된 변수를 참조할 수 있어 문제를 일으킬 수 있음

  - 호이스팅을 통해 끌어올려진 `var` 변수는 `undefined` 값을 반환하고 변수를 사용 혹은 참조한 후에 선언 및 초기화하여도, 여전히 `undefined`를 반환함

- `const`, `let`는 변수를 상단으로 끌어올리지만 초기화를 하지 않아 문제가 발생하지 않음

  - 선언되기 전에 블록 안에서 변수를 참조하게 되면 `ReferenceError`를 발생시킴

- ### 따라서 변수 호이스팅의 문제를 방지하기 위해 const, let을 사용하여 변수를 정의하는 것이 안전하다.

<br/>

```javascript
// const 변수 선언
const a = 1

a = 2
// a는 const이기 때문에 값을 변경할 수 없음

// let 변수 선언
let b = 1

b = 2
// b는 let이기 때문에 값이 변경됨

b // 2
```

<br/>

