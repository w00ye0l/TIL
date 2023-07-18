# [Vue] ref vs. reactive

Vue3에서 등장한 composition api.



## composition api가 등장한 배경

Vue2에서는 options api를 사용하고 있었음

- 객체 내에 다양한 속성을 사용하고 있는 형태
- 라이프 사이클을 제어하기 위해 사용하는 created, mounted, updated 그리고 컴포넌트 내에서 여러 메서드(methods)들을 정의하고 데이터(data)들을 참조할 때 정해진 속성에 정의해 사용



## options api 사용 예시

```js
// <script> 태그 안

export default {
  components: {
    // 컴포넌트 정의
  },
  data() {
    return {
      // 데이터 정의
    }
  },
  created() {
    // created 시점 정의
  },
  methods() {
    // 컴포넌트 내에서 사용할 method 정의
  }
}
```



### options api의 장점

- 명확한 구성

메서드를 수정하거나 추가하려면 methods 속성을 수정

데이터를 수정하거나 추가하려면 data, computed 속성을 수정

역할이 명확하여 유지보수가 용이하지만 소스코드가 복잡한 컴포넌트라면 가독성이 떨어지고 위치가 분리되어있어 서로 추적하기가 불편함



## composition api 사용 예시

```js
export default {
  setup() {
    // data 정의
    let fruit = "apple";
    let cost = "2";
      
    // computed 정의
      
    // methods 정의
    const calculateCost = () => {
      console.log(`${fruit}의 가격은 ${cost} 달러`);
    };
      
    // lifecycle hooks 정의
  }
}
```



### composition api의 장점

- 관심사의 구분

options api가 역할 별로 속성을 구분하였다면 composition api에서는 논리적 관심사끼리 구분하기 편하게 설계됨

기존 options api에서는 속성 별로 구분되어 같은 관심사도 흩어져있음. 하지만 composition api에서는 한 부분에 모여 설계할 수 있어 가독성이 향상됨



### composition api에서 data 반응형으로 만들기

#### ref 사용

```js
import { ref } from "vue";

export default {
  setup() {
    const person1 = ref({ name: "Hong Kil Dong", age: 30 });

    const updatePerson = () => {
      // ref로 감싼 date는 value로 접근한 뒤 값에 접근
      person1.value.age = 50;
    };

    return {
      person1,
      updatePerson,
    };
  },
};
```



#### reactive 사용

```js
import { reactive } from "vue";

export default {
  setup() {
    const person1 = reactive({ name: "Hong Kil Dong", age: 30 });

    const updatePerson = () => {
      // reactive로 감싼 date는 바로 접근한 뒤 값에 접근
      person1.age = 50;
    };

    return {
      person1,
      updatePerson,
    };
  },
};
```



#### ref와 reactive의 차이

1. 타입의 제한

ref에서는 String, Number, Object 등 어떤 타입에서든 사용 가능

reactive에서는 Object, Array, Map, Set과 같은 타입에서만 사용 가능

reactive에서 String, Number의 값을 초기에 지정하여 사용할 경우 원시값에 대해서는 반응형을 가지지 않음



2. 접근 방식

ref에서는 .value를 붙여야 접근할 수 있음. <template> 안에서 사용할 때는 붙이지 않아도 됨

reactive는 .value를 붙이지 않아도 접근할 수 있음.



### lifecycle hook

컴포넌트 라이프 사이클을 제어하기 위해서는 hook을 import하여 사용하면 됨

- onMounted, onUnmounted
- onUpdated, onBeforeUpdate
- onBeforeMount, onBeforeUnmount

```js
import { axios, onMounted } from "vue";

export default {
  setup() {
    const getPost = () => {
      axios.get("~~~~").then((res) => {
        console.log(JSON.stringify(res));
      });
    };

    // mounted 단계에서 'getPost' 호출
    onMounted(getPost);
  },
};
```



### computed, watch

computed, watch 속성을 사용하기 위해서는 import하여 사용하면 됨

```vue
<template>
  <div>
    <h2>{{ message }}</h2>
    <h2>{{ reverseMessage }}</h2>
  </div>
</template>
```



#### computed 사용

```vue
<script>
import { ref, computed } from "vue";

export default {
  setup() {
    const message = ref("hello");

    const reverseMessage = computed(() => {
      return message.value.split("").reverse().join("");
    });

    return { message, reverseMessage };
  },
};
</script>
```



#### watch 사용

```vue
<script>
import { ref, watch } from "vue";

export default {
  setup() {
    const message = ref("hello");
    const reverseMessage = ref("");

    watch(message, (oldValue) => {
      reverseMessage.value = oldValue.value.split("").reverse().join("");
    });

    return { message, reverseMessage };
  },
};
</script>
```



