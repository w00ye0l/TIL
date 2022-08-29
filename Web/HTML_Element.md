# HTML 요소

> HTML에서 자주 사용되는 요소 정리
>
> [Mozilla HTML Element](https://developer.mozilla.org/ko/docs/Web/HTML/Element) 참고

| 요소                                                         | 설명                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`<head>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/head) | 기계가 식별할 수 있는 문서 정보(메타데이터)를 담음<br />정보로는 문서가 사용할 [제목](https://developer.mozilla.org/ko/docs/Web/HTML/Element/title), [스크립트](https://developer.mozilla.org/ko/docs/Web/HTML/Element/script), [스타일 시트](https://developer.mozilla.org/ko/docs/Web/HTML/Element/style) 등이 있음 |
| [`<title>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/title) | 브라우저의 제목 표시줄이나 페이지 탭에 보이는 문서 제목을 정의<br />텍스트만 포함할 수 있으며 태그를 포함하더라도 무시 |
| [`<body>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/body) | HTML 문서의 내용을 나타냄<br />한 문서에 하나의 `<body> `요소만 존재할 수 있음 |
| [`<header>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/header) | 소개 및 탐색에 도움을 주는 콘텐츠<br />제목, 로고, 검색 폼, 작성자 이름등의 요소도 포함 가능 |
| [`<footer>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/footer) | 가장 가까운 구획 콘텐츠나 구획 루트의 푸터를 나타냄<br />일반적으로 구획의 작성자, 저작권 정보, 관련 문서 등의 내용을 담음 |
| [`<article>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/article) | 문서, 페이지, 애플리케이션, 또는 사이트 안에서 독립적으로 구분해 배포하거나 재사용할 수 있는 구획<br />예시로 게시판과 블로그 글, 매거진이나 뉴스 기사 등이 있음 |
| [`<section>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/section) | HTML 문서의 독립적인 구획을 나타내며, 더 적합한 의미를 가진 요소가 없을 때 사용<br />보통 `<section>`은 제목을 포함하지만 항상 그런 것은 아님 |
| [`<p>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/p) | 하나의 문단. 시각적인 매체에서, 문단은 보통 인접 블록과의 여백과 첫 줄의 들여쓰기로 구분하지만, HTML에서 문단은 이미지나 입력 폼 등 서로 관련 있는 콘텐츠 무엇이나 될 수 있음 |
| [`<div>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/div) | 플로우 콘텐츠를 위한 통용 컨테이너<br />CSS로 꾸미기 전에는 콘텐츠나 레이아웃에 어떤 영향도 주지 않음 |
| [`<span>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/span) | 구문 콘텐츠를 위한 통용 인라인 컨테이너로, 본질적으로는 아무것도 나타내지 않음<br />스타일을 적용하기 위해서, 또는 lang 등 어떤 특성의 값을 서로 공유하는 요소를 묶을 때 사용할 수 있음<br />적절한 의미를 가진 다른 요소가 없을 때에만 사용 |
| [`<img>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/img) | 문서에 이미지를 넣음                                         |
| [`<aside>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/aside) | 문서의 주요 내용과 간접적으로만 연관된 부분을 나타냄<br />주소 사이트바 혹은 콜아웃 박스로 표현 |
| [`<audio>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/audio) | 문서에 소리 콘텐츠를 포함할 때 사용<br />`src` 특성 또는 `<source>_(en-US)` 요소를 사용해 한 개 이상의 오디오 소스를 지정할 수 있으며, 다수를 지정한 경우 가장 적절한 소스를 브라우저가 고름 |
| [`<canvas>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/canvas) | [캔버스 스크립팅 API](https://developer.mozilla.org/ko/docs/Web/API/Canvas_API) 또는 [WebGL API](https://developer.mozilla.org/ko/docs/Web/API/WebGL_API)와 함께 사용해 그래픽과 애니메이션을 그릴 수 있음 |
| [`<datalist>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/datalist) | 다른 컨트롤에서 고를 수 있는 가능한, 혹은 추천하는 선택지를 나타내는 `<option>` 요소 여럿을 담음 |
| [`<details>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/details) | "열림" 상태일 때만 내부 정보를 보여주는 정보 공개 위젯을 생성<br />요약이나 레이블은 [`<summary>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/summary) 요소를 통해 제공 |
| [`<embed>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/embed) | 외부 어플리케이션이나 대화형 컨텐츠와의 통합점을 나타냄      |
| [`<nav>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/nav) | 문서의 부분 중 현재 페이지 내, 또는 다른 페이지로의 링크를 보여주는 구획을 나타냄<br />예시로는 메뉴, 목차, 색인 |
| [`<output>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/output) | 웹 사이트나 앱에서 계산이나 사용자 행동의 결과를 삽입할 수 있는 컨테이너 요소 |
| [`<progress>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/progress) | 어느 작업의 완료 정도를 나타내며, 주로 진행 표시줄의 형태를 띔 |
| [`<video>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Video) | 비디오 플레이백을 지원하는 미디어 플레이어를 문서에 삽입.<br />오디오 컨텐츠에도 사용할 수 있으나, `<audio>` 요소가 사용자 경험에 좀 더 적합 |
| [`<ul>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/ul) | 정렬되지 않은 목록을 나타냄. 보통 불릿으로 표현              |
| [`<ol>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/ol) | 정렬된 목록을 나타냄. 보통 숫자 목록으로 표현                |
| [`<li>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/li) | 목록의 항목을 나타냄. 반드시 정렬 목록(`<ol>`), 비정렬 목록(`<ul>`, 혹은 메뉴 [`<menu>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/menu)) 안에 위치해야 함. 메뉴와 비정렬 목록에서는 보통 불릿으로 항목을 나타내고, 정렬 목록에서는 숫자나 문자를 사용한 오름차순 카운터로 나타냄 |
| [`<blockquote>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/blockquote) | 안쪽의 텍스트가 긴 인용문임을 나타냄. 주로 들여쓰기를 한 것으로 그려짐. 인용문의 출처 URL은 `cite` 특성으로, 출처 텍스트는 [`<cite>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/cite) 요소로 제공할 수 있음 |

<br/>

## 인라인 요소 VS 블록 레벨 요소

> - 콘텐츠 모델
>   - 일반적으로 블록 레벨 요소는 인라인 요소와 (때때로) 다른 블록 레벨 요소를 포함할 수 있다. 이런 고유한 구조적 차이점으로 인해 블록 레벨 요소는 인라인 요소보다 더 "큰" 구조를 생성할 수 있다.
> - 기본 서식
>   - 기본적으로 블록 레벨 요소는 새로운 줄에서 시작하지만, 인라인 요소는 줄의 어느 곳에서나 시작할 수 있다

| 인라인 요소                                                  |                                                              | 블록 레벨 요소                                               |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`<a>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/a) | [`<abbr>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/abbr) | [`<address>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/address) | [`<article>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/article) |
| [`<acronym>_(en-US)`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/acronym) | [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio) | [`<aside>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/aside) | [`<blockquote>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/blockquote) |
| [`<b>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/b) | [`<bdi>_(en-US)`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdi) | [`<details>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/details) | [`<dialog>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/dialog) |
| [`<bdo>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdo) | [`<big>_(en-US)`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/big) | [`<dd>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/dd) | [`<div>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/div) |
| [`<br>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/br) | [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button) | [`<dl>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/dl) | [`<dt>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/dt) |
| [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas) | [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite) | [`<fieldset>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/fieldset) | [`<figcaption>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/figcaption) |
| [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/code) | [`<data>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/data) | [`<figure>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/figure) | [`<footer>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/footer) |
| [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist) | [`<del>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/del) | [`<form>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/form) | [`<h1>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/h1), [`<h2>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/h2), [`<h3>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/h3), [`<h4>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/h4), [`<h5>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/h5), [`<h6>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/h6) |
| [`<dfn>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dfn) | [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/em) | [`<header>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/header) | [`<hgroup>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/hgroup) |
| [`<embed>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/embed) | [`<i>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/i) | [`<hr>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/hr) | [`<li>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/li) |
| [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) | [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) | [`<main>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/main) | [`<nav>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/nav) |
| [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input) | [`<ins>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins) | [`<ol>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/ol) | [`<p>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/p) |
| [`<kbd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd) | [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label) | [`<pre>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/pre) | [`<section>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/section) |
| [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map) | [`<mark>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark) | [`<table>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/table) | [`<ul>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/ul) |
| [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter) | [`<noscript>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/noscript) |                                                              |                                                              |
| [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object) | [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output) |                                                              |                                                              |
| [`<picture>_(en-US)`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture) | [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress) |                                                              |                                                              |
| [`<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q) | [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) |                                                              |                                                              |
| [`<s>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/s) | [`<samp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/samp) |                                                              |                                                              |
| [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) | [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select) |                                                              |                                                              |
| [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot) | [`<small>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/small) |                                                              |                                                              |
| [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/span) | [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/strong) |                                                              |                                                              |
| [`<sub>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sub) | [`<sup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup) |                                                              |                                                              |
| [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/svg) | [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template) |                                                              |                                                              |
| [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea) | [`<time>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time) |                                                              |                                                              |
| [`<u>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/u) | [`<tt>_(en-US)`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tt) |                                                              |                                                              |
| [`<var>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/var) | [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video) |                                                              |                                                              |
| [`<wbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/wbr) |                                                              |                                                              |                                                              |

