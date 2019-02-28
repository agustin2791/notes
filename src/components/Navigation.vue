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
.navigation {
    width: 100%;
    height: 40px;
    display: block;
    position: fixed;
    top: 0;
    left: 0;
    background: #34495e;
    color: #ecf0f1;
    .nav-list {
        width: 100%;
        display: block;
        padding: 0;
        .nav-item {
            display: inline-block;
            height: 20px;
            margin: 0;
            padding: 5px;
            &.active {
                font-weight: 600;
            }
            .nav-link {
                height: 20px;
                margin: 0;
                padding: 5px;
                display: block;
                color: #ecf0f1;
            }
        }
    }
}
</style>
