import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import BootstrapVue from 'bootstrap-vue'
import VueTextareaAutosize from 'vue-textarea-autosize'
import './registerServiceWorker'

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(VueTextareaAutosize)

Vue.mixin({
	data(){
		return {
			isLoading: false,
		}
	},
	methods: {
		loading() {
			console.log(this.isLoading)
			this.isLoading = true
			console.log(this.isLoading)
		},
		notLoading() {
			this.isLoading = false
		}
	}
})

new Vue({
	store,
	router,
	render: h => h(App)
}).$mount('#app')
