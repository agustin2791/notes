import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Index from './views/Index.vue'
import Subjects from './views/Subjects.vue'
import Sections from './views/Sections.vue'
import Register from './views/auth/Register.vue'
import Login from './views/auth/Login.vue'

import store from './store'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Home,
      beforeEnter(to, from, next) {
        if (store.state.idToken) {
          next()
        } else {
          next('/')
        }
      }
    },
    {
      path: '/subjects',
      name: 'subjects',
      component: Subjects,
      beforeEnter(to, from, next) {
        if (store.state.idToken) {
          next()
        } else {
          next('/')
        }
      }
    },
    {
      path: '/sections',
      name: 'sections',
      component: Sections,
      beforeEnter(to, from, next) {
        if (store.state.idToken) {
          next()
        } else {
          next('/')
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
