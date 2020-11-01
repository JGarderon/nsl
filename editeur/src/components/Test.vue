
<template>
<div> 

  {{ test }} 

</div>
</template>

<script> 

import Config from '../config.js' 

export default {
  name: 'Test',
  mixins: [ Config ],  
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
</style>
