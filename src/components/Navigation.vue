<template>
    <div class="navigation">
        <ul class="nav-list">
            <router-link tag="li" class="nav-item" active-class="active" to="/" exact><a class="nav-link">Home</a></router-link>
            <router-link tag="li" class="nav-item" active-class="active" to="/about"><a class="nav-link">About</a></router-link>
        </ul>
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
