<template>
	<div class="container">
		<br><br>
		<b-form @submit.prevent="onSubmit"
            @reset="onReset">
            <b-alert show variant="danger" v-if="logErr">Username/email and password did not match</b-alert>
            <b-form-group
                id="input-group-username"
                label="Username: "
                label-for="input-username"

            >
                <b-form-input
                    id="input-username"
                    type="text"
                    v-model="login.username"
                    required
                ></b-form-input>
            </b-form-group>
            <b-form-group
                id="input-group-password"
                label="Password: "
                label-for="input-password"
            >
                <b-form-input
                    id="input-password"
                    type="password"
                    v-model="login.password"
                    required
                ></b-form-input>
            </b-form-group>
            <b-button type="submit" variant="primary">Submit</b-button>
            <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
        <div v-if="isLoading" class="loading">
	      <div class="center-spinner">
	        Logging in... <b-spinner variant="success" label="Logging in..."></b-spinner>
	      </div>
    	</div>
	</div>
</template>

<script type="text/javascript">
	export default {
		data() {
			return {
				logErr: false,
				login: {
					username: '',
					password: ''
				}
			}
		},
		methods: {
			onSubmit() {
				this.loading()
				this.$store.dispatch('login', this.login)
					.then(res => {
						if (res.status === 'ok') {
							this.$router.push('/')
							this.notLoading()
							this.logErr = false;
						} else {
							this.logErr = true;
							this.notLoading();
						}
					});
			},
			onReset() {
				console.log('reset')
			}
		},
		computed: {
			isLoggedIn() {
				let user = this.$store.getters.getUser;
				if (user != null) {
					return true
				} else {
					return false
				}
			}
		}
	}
</script>
<style lang="scss">
	
</style>