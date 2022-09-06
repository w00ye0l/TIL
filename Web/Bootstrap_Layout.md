# Bootstrap 사용하기

## [Bootstrap 적용](https://getbootstrap.com/docs/5.2/getting-started/introduction/)

<br/>

## Layout

### Breakpoints [link](https://getbootstrap.com/docs/5.2/layout/breakpoints/)

> Breakpoints는 반응형 디자인의 블록을 만드는 것
>
> Media queries를 사용하여 breakpoint로 CSS를 설계하는 것
>
> 모바일을 우선으로 반응형 디자인을 하는 것

| Breakpoint        | Class infix | Dimensions |
| ----------------- | ----------- | ---------- |
| Extra small       | None        | < 576px    |
| Small             | `sm`        | >= 576px   |
| Medium            | `md`        | >= 768px   |
| Large             | `lg`        | >= 992px   |
| Extra large       | `xl`        | >= 1200px  |
| Extra extra large | `xxl`       | >= 1400px  |

<br/>

### Containers [link](https://getbootstrap.com/docs/5.2/layout/containers/)

> 사용자 기기에 따라 뷰 포인트를 맞춰, 기본적인 블록을 만드는 것

- `.container` : 각각의 반응형 breakpoint에 대해 `max-width`를 맞춤
- `.container-{breakpoint}` : breakpoint까지 `width: 100%`
- `.container-fluid` : 모든 breakpoint에 대해 `width: 100%`

|                    | Extra small<br /><576px | Small<br />>=576px | Medium<br />>=768px | Large<br />>=992px | X-Large<br />>=1200px | XX-Large<br />>=1400px |
| ------------------ | ----------------------- | ------------------ | ------------------- | ------------------ | --------------------- | ---------------------- |
| `.container`       | 100%                    | 540px              | 720px               | 960px              | 1140px                | 1320px                 |
| `.container-sm`    | 100%                    | 540px              | 720px               | 960px              | 1140px                | 1320px                 |
| `.container-md`    | 100%                    | 100%               | 720px               | 960px              | 1140px                | 1320px                 |
| `.container-lg`    | 100%                    | 100%               | 100%                | 960px              | 1140px                | 1320px                 |
| `.container-xl`    | 100%                    | 100%               | 100%                | 100%               | 1140px                | 1320px                 |
| `.container-xxl`   | 100%                    | 100%               | 100%                | 100%               | 100%                  | 1320px                 |
| `.container-fluid` | 100%                    | 100%               | 100%                | 100%               | 100%                  | 100%                   |

- #### Default container

  - `.container`는 각 breakpoint에 따라 `max-width`가 변하는 반응형이고 고정된 너비를 갖는 container이다

  ```html
  <div class="container">
    <!-- Content here -->
  </div>
  ```

<br/>

- #### Responsive containers

  - `Responsive comtainers`는 각 breakpoint 이전의 값까지는 `width: 100%`를 갖는다

  ```html
  <div class="container-sm">100% wide until small breakpoint</div>
  <div class="container-md">100% wide until medium breakpoint</div>
  <div class="container-lg">100% wide until large breakpoint</div>
  <div class="container-xl">100% wide until extra large breakpoint</div>
  <div class="container-xxl">100% wide until extra extra large breakpoint</div>
  ```

  
