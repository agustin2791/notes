<template>
  <div id="app">
    <navigation></navigation>
    <router-view/>
    
  </div>
</template>

<script>
/* eslint-disable */
import Navigation from './components/Navigation.vue'
export default {
	components: {
		Navigation
	},
  created() {
    this.$store.dispatch('loginCheck');
  }
}
</script>

<style lang="scss">
@import './assets/custom.scss';
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
