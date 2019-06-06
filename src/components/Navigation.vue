<template>
    <div>
      <b-navbar toggleable="sm" type="dark" variant="info">
        <b-navbar-toggle target="navigation" />

        <b-collapse is-nav id="navigation">
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">

            <b-nav-item-dropdown text="Links" right>
              <b-dropdown-item to="/">Home</b-dropdown-item>
              <b-dropdown-item to="/subjects">Subject Info</b-dropdown-item>
              <b-dropdown-item to="/sections">Section Info</b-dropdown-item>
            </b-nav-item-dropdown>
            <b-nav-item v-if="user == 'Login'" to="/login">Login</b-nav-item>
            <b-nav-item v-if="user == 'Login'" to="/register">Register</b-nav-item>
            <b-nav-item-dropdown right v-if="user != 'Login'">
              <!-- Using button-content slot -->
              <template slot="button-content"><em>{{user.username}}</em></template>
              <b-dropdown-item href="#">Profile</b-dropdown-item>
              <b-dropdown-item @click="signOut">Logout</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
</template>

<script type="text/javascript">
  export default {
    data() {
      return {

      }
    },
    methods: {
      signOut() {
        this.$store.dispatch('logout')
      }
    },
    computed: {
      user() {
        let user = this.$store.getters.getUser;
        if (user == null) return 'Login'
        return user
      }
    }
  }
</script>

<style lang="scss" scoped>
.bg-info {
  background:#34495e !important;
}
</style>
