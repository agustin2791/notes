<template>
    <div class="container">
        <b-form @submit.prevent="onSubmit"
            @reset="onReset">
            <b-form-group
                id="input-group-first_name"
                label="First Name: "
                label-for="input-first_name"

            >
                <b-form-input
                    id="input-first_name"
                    type="text"
                    v-model="register.first_name"
                    required
                ></b-form-input>
            </b-form-group>
            <b-form-group
                id="input-group-last_name"
                label="Last Name: "
                label-for="input-last_name"

            >
                <b-form-input
                    id="input-last_name"
                    type="text"
                    v-model="register.last_name"
                    required
                ></b-form-input>
            </b-form-group>
            <b-form-group
                id="input-group-username"
                label="Username: "
                label-for="input-username"

            >
                <b-form-input
                    id="input-username"
                    type="text"
                    v-model="register.username"
                    required
                ></b-form-input>
            </b-form-group>
            <b-form-group
                id="input-group-email"
                label="Email: "
                label-for="input-email"
            >
                <b-form-input
                    id="input-email"
                    type="email"
                    v-model="register.email"
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
                    v-model="register.password"
                    required
                ></b-form-input>
            </b-form-group>
            <b-form-group
                id="input-group-conf_pass"
                label="Confirm Password: "
                label-for="input-conf_pass"
            >
                <b-form-input
                    id="input-conf_pass"
                    type="password"
                    v-model="register.conf_pass"
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

<script>
export default {
    data() {
        return {
            register: {
                first_name: null,
                last_name: null,
                username: null,
                email: null,
                password: null,
                conf_pass: null
            }
        }
    },
    methods: {
        onSubmit() {
            this.loading()
            if (this.register.password == this.register.conf_pass) {
                this.$store.dispatch('register', this.register)
                    .then(res => {
                        if (res.status === 'ok') {
                            this.$router.push('/')
                            this.notLoading()
                        } else {
                            this.notLoading()
                        }  
                    })
            }
        },
        onReset() {
            console.log('reset')
        }
    }

}
</script>
