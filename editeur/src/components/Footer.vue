
<template>
<footer class="footer"> 

  <div class="container">
    <a :href="site.url">{{ site.name }}</a> 
    - <span>{{ site.slogan }}</span> 
    - <span><a :href="'mailto:'+site.maintener.mail">{{ site.maintener.name }}</a> </span> 
  </div>

</footer>
</template>

<script> 

import Config from '../config.js'
import mixin_global from '../mixin-global.js'

export default {
  name: 'Footer',
  mixins: [ Config, mixin_global ],  
  data: function() { 
    return { 
      "test": this.$parent.test,   
    }; 
  }, 
  props: { 
  }
}
</script>

<style scoped>

.footer { 
	margin: 1rem 0px 1rem 0px;  
	padding: 1rem;  
	color: white; 
	background: lightgray; 
} 

a { 
	color: inherit; 
}

</style>
