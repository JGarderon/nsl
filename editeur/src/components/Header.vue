
<template>
  <header>
    
    <nav class="navbar navbar-expand-md navbar-dark bg-dark"> fixed-top 
      
      <a class="navbar-brand" :href="site.url">{{ site.name }}</a>  
      
      <button
        v-on:click="test('coucou', $event)"  
      >test bouton</button>

      <router-link to="/user/1">Aller à user/1</router-link> 
      <router-link to="/foo">Aller à Foo</router-link> 
      <router-link to="/bar">Aller à Bar</router-link> 

    </nav> 

  </header>
</template>

<script> 

import Config from '../config.js'
import mixin_global from '../mixin-global.js'

export default {
  name: 'Header',
  mixins: [ Config, mixin_global ], 
  data: function() { 
    return { 
    }; 
  }, 
  props: { 
  }, 

  methods: { 

    test( m, event ) { 

      console.log("appel de 'test'", m, event); 

      var request = new Request("https://api.github.com", {
        method: "GET"
      }) 
      fetch(request).then(response => {
        if (response.ok) {
          console.log( "---> ok", response); 
        } else {
          console.log( "---> ko", response); 
        } 
      }).catch((error) => {
        console.log( "---> error", error);
      });

    }


  }


}


</script>

<style scoped>
</style>
