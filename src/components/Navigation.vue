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

            <b-nav-item-dropdown right>
              <!-- Using button-content slot -->
              <template slot="button-content"><em>User</em></template>
              <b-dropdown-item href="#">Profile</b-dropdown-item>
              <b-dropdown-item href="#">Signout</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
</template>

<style lang="scss" scoped>
.bg-info {
  background:#34495e !important;
}
</style>
