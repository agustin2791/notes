<template>
    <div class="container">
        <b-form>
            <b-form-group
                id="input-group-username"
                label="Name: "
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
                label="Name: "
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
                label="Name: "
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
                label="Name: "
                label-for="input-conf_pass"
            >
                <b-form-input
                    id="input-conf_pass"
                    type="password"
                    v-model="register.conf_pass"
                    required
                ></b-form-input>
            </b-form-group>
        </b-form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            register: {
                username: null,
                email: null,
                password: null,
                conf_pass: null
            }
        }
    },

}
</script>
