import Vue from 'vue'
import VueRouter from 'vue-router' 

Vue.use(VueRouter) 

// const viewQuelquechose = { template: '<div>foo</div>'  } 

export default new VueRouter(
    { 
      routes: [ 
        { 
          path: "/",
          component: () => import("@/views/Home"),
          children: [
            // {
            //   path: "",
            //   name: "Test",
            //   components: {
            //     Test 
            //   }
            // },
          ] 
        } 
      ], 
      mode: 'history' 
    }
); 




