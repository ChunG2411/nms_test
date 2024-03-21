<template>
    <div class="header">
        <router-link class="logo" to="/">
            <img src="../assets/logo.png" style="width: 200px;">
        </router-link>
        <div class="search">
            <input class="search-input" type="text" placeholder="Dán link hoặc tìm sản phẩm">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" viewBox="0 0 512 512">
                <path fill="#ff7227" d="M416 208c0 45.9-14.9 88.3-40 122.7L502.6 457.4c12.5 12.5 12.5 32.8 0 45.3s-32.8 12.5-45.3 0L330.7 376c-34.4 25.2-76.8 40-122.7 40C93.1 416 0 322.9 0 208S93.1 0 208 0S416 93.1 416 208zM208 352a144 144 0 1 0 0-288 144 144 0 1 0 0 288z"/>
            </svg>
        </div>
        <div class="category">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" viewBox="0 0 448 512">
                <path d="M0 96C0 78.3 14.3 64 32 64H416c17.7 0 32 14.3 32 32s-14.3 32-32 32H32C14.3 128 0 113.7 0 96zM0 256c0-17.7 14.3-32 32-32H416c17.7 0 32 14.3 32 32s-14.3 32-32 32H32c-17.7 0-32-14.3-32-32zM448 416c0 17.7-14.3 32-32 32H32c-17.7 0-32-14.3-32-32s14.3-32 32-32H416c17.7 0 32 14.3 32 32z"/>
            </svg>
            <p>DANH MỤC</p>
        </div>
        <div class="blog">
            <a href="https://muathongminh.vn/blog">BLOG</a>
        </div>
    </div>
</template>

<style>
.category{
    display: flex;
    gap: 5px;
}
.header {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    padding: 20px 0 20px 0;
}
.search{
    border: 1px solid gray;
    border-radius: 20px;
    padding: 5px 15px;
    width: 400px;
    display: flex;
    justify-content: space-between;
}
.search-input{
    border: none;
    width: 90%;
    outline: none;
}
</style>