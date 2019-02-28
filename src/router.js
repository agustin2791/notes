import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Subjects from './views/Subjects.vue'
import Sections from './views/Sections.vue'

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
      component: Sections
    }
  ]
})
