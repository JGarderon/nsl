<template>
  <div class="home">
    <h1>This is an about page</h1>
    <Test></Test>
  </div>
</template>

<script> 

import Config from '../config.js'
import mixin_global from '../mixin-global.js'

import Test from '../components/Test.vue' 

console.log( Test ); 

export default { 
  mixins: [ Config, mixin_global ],  
  data: function() { 
    return { 
      "test": this.$parent.test,   
    }; 
  }, 
  components: { 
    Test 
  }, 
  props: { 
  }
}
</script>

<style scoped></style> 