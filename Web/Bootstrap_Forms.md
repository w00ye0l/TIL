# Bootstrap 사용하기

## Form controls [link](https://getbootstrap.com/docs/5.2/forms/form-control/)

> `<input>`과 `<textarea>`와 같은 텍스트 형식의 form 제어들을 자신만의 스타일(styles, sizing, focus states 등)로 꾸밀 수 있도록 해준다.

- Example

  ```html
  <div class="mb-3">
    <label for="exampleFormControlInput1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
  </div>
  <div class="mb-3">
    <label for="exampleFormControlTextarea1" class="form-label">Example textarea</label>
    <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
  </div>
  ```

<br/>

### Sizing

> `.form-control-lg`, `.form-control-sm`

```html
<input class="form-control form-control-lg" type="text" placeholder=".form-control-lg" aria-label=".form-control-lg example">
<input class="form-control" type="text" placeholder="Default input" aria-label="default input example">
<input class="form-control form-control-sm" type="text" placeholder=".form-control-sm" aria-label=".form-control-sm example">
```

<br/>

### Disabled

> `disabled`라는 boolean 속성을 부여하여 입력을 막을 수 있다

```html
<input class="form-control" type="text" placeholder="Disabled input" aria-label="Disabled input example" disabled>
<input class="form-control" type="text" value="Disabled readonly input" aria-label="Disabled input example" disabled readonly>
```

<br/>

### Readonly

> `readonly`라는 boolean 속성을 부여하여 input의 값을 수정하는 것을 막고 focused와 selected 될 수 있다.

```html
<input class="form-control" type="text" value="Readonly input here..." aria-label="readonly input example" readonly>
```

<br/>

### Readonly plain text

> 읽기 전용 plain text로 만들고 싶다면 `.form-control`을 `.form-control-plaintext`로 바꾸어주면 된다

```html
<div class="mb-3 row">
  <label for="staticEmail" class="col-sm-2 col-form-label">Email</label>
  <div class="col-sm-10">
    <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="email@example.com">
  </div>
</div>
<div class="mb-3 row">
  <label for="inputPassword" class="col-sm-2 col-form-label">Password</label>
  <div class="col-sm-10">
    <input type="password" class="form-control" id="inputPassword">
  </div>
</div>
```

<br/>

### Visually hidden

> label을 숨기고 싶을 때 `visually-hidden`을 적용하면 된다

```html
<form class="row g-3">
  <div class="col-auto">
    <label for="staticEmail2" class="visually-hidden">Email</label>
    <input type="text" readonly class="form-control-plaintext" id="staticEmail2" value="email@example.com">
  </div>
  <div class="col-auto">
    <label for="inputPassword2" class="visually-hidden">Password</label>
    <input type="password" class="form-control" id="inputPassword2" placeholder="Password">
  </div>
  <div class="col-auto">
    <button type="submit" class="btn btn-primary mb-3">Confirm identity</button>
  </div>
</form>
```

<br/>

### File input

> 여러 방식의 파일을 첨부하는 class가 존재한다
>
> `Default file input example`, `Multiple files input example`, `Disabled file input example`, `Small file input example`, `Large file input example`

```html
<div class="mb-3">
  <label for="formFile" class="form-label">Default file input example</label>
  <input class="form-control" type="file" id="formFile">
</div>
<div class="mb-3">
  <label for="formFileMultiple" class="form-label">Multiple files input example</label>
  <input class="form-control" type="file" id="formFileMultiple" multiple>
</div>
<div class="mb-3">
  <label for="formFileDisabled" class="form-label">Disabled file input example</label>
  <input class="form-control" type="file" id="formFileDisabled" disabled>
</div>
<div class="mb-3">
  <label for="formFileSm" class="form-label">Small file input example</label>
  <input class="form-control form-control-sm" id="formFileSm" type="file">
</div>
<div>
  <label for="formFileLg" class="form-label">Large file input example</label>
  <input class="form-control form-control-lg" id="formFileLg" type="file">
</div>
```

<br/>

### Color

> `type="color"` 그리고 `.form-control-color`를 input에 적용한다. bootstrap에서는 브라우저와의 충돌을 막기 위해 클래스를 재정의하여 고정된 height를 사용한다

```html
<label for="exampleColorInput" class="form-label">Color picker</label>
<input type="color" class="form-control form-control-color" id="exampleColorInput" value="#563d7c" title="Choose your color">
```

<br/>

### Datalists

> `<input>`을 선택했을 경우 선택할 수 있는 `<option>`들을 그룹화해 보여줄 수 있다

```html
<label for="exampleDataList" class="form-label">Datalist example</label>
<input class="form-control" list="datalistOptions" id="exampleDataList" placeholder="Type to search...">
<datalist id="datalistOptions">
  <option value="San Francisco">
  <option value="New York">
  <option value="Seattle">
  <option value="Los Angeles">
  <option value="Chicago">
</datalist>
```



