<template>
  <div id="app">
  
    <Header></Header>

    <div class="container-fluid">

      <div class="row">
        Route : {{ $route }}
      </div> 
      
      <div class="row">
        <router-view name="viewApplication"></router-view> 
        <router-view></router-view>
        <router-view name="viewQuelquechose">----</router-view> 
      </div> 

    </div> 
    
    <Footer></Footer> 

  </div>
</template>

<script> 

import Header from './components/Header.vue' 
import Footer from './components/Footer.vue' 

export default {  
  name: 'App',
  data: function() {
    return { 
      "test": { "ok": "truc" } 
    }; 
  }, 
  components: { 
    Header,  
    Footer 
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px; 

  font-size: 14pt; 

} 
</style>
