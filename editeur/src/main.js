import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'

import router from './router'

import App from './App.vue' 

Vue.config.productionTip = false;

const v = new Vue( 
  {
    router,
    render: h => h(App), 
    // components: { App } 
  } 
);

v.$mount('#app'); 


