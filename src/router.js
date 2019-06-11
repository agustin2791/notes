import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Subjects from './views/Subjects.vue'
import Sections from './views/Sections.vue'
import Register from './views/auth/Register.vue'
import Login from './views/auth/Login.vue'

import state from './store'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/subjects',
      name: 'subjects',
      component: Subjects
    },
    {
      path: '/sections',
      name: 'sections',
      component: Sections,
      beforeRouterEnter (to, from, next) {
        if (state.state.idToken) {
          next()
        } else {
          next('/login')
        }
      }
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    }
  ]
})
