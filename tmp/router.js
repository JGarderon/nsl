import Vue from 'vue' 
import Router from 'vue-router' 
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router(
    {
      routes: [
          { 
            path: '/bar', 
            name: 'bar', 
            components: { 
              viewApplication: { template: `ok`} 
            } 
          }, 
          { 
            path: '/foo', 
            name: 'foo', 
            components: { 
              Footer: { template: `!footer!`} 
            } 
          }, 
          { 
            path: '/user/:id', 
            name: 'user', 
            component: User 
          } 
      ]
    }
); 

