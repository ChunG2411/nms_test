<script setup>
import Header from '../components/header.vue'
import Footer from '../components/footer.vue'
import PriceHistory from '../components/priceHistory.vue'
import ProductSuggest from '../components/productSuggest.vue'
import Report from '../components/report.vue'
import ProductImage from '../components/productImage.vue'
import Popup from '../components/popup.vue'

import { ref, watch } from 'vue';
import { useRoute } from 'vue-router'
import axios from 'axios'
import { api, formatNumber } from '../utils/config.js'

const route = useRoute()

watch(() => route.params.id, (currentvalue, oldvalue) => {
    api_get_product(currentvalue)
    api_get_product_image(currentvalue)
    api_get_product_price(currentvalue)
    api_get_product_rate(currentvalue)
    api_get_list_product(currentvalue)
})

const show_price_board = ref(false)
const product = ref(null)
const product_list = ref(null)
const product_image = ref(null)
const product_price = ref(null)
const product_rate = ref(null)

const have_more_rate = ref(null)


const api_get_product = (id) => {
    axios.get(`${api}/api/product/${id}`)
        .then(response => {
            product.value = response.data
        })
}
const api_get_product_image = (id) => {
    axios.get(`${api}/api/product/image/${id}`)
        .then(response => {
            product_image.value = response.data
        })
}
const api_get_product_price = (id) => {
    axios.get(`${api}/api/product/price/${id}`)
        .then(response => {
            product_price.value = response.data.results
        })
}
const api_get_product_rate = (id) => {
    axios.get(`${api}/api/product/rate/${id}`)
        .then(response => {
            product_rate.value = response.data.results
            if (response.data.next) {
                have_more_rate.value = response.data.next
            }
        })
}
const api_get_list_product = () => {
    axios.get(`${api}/api/product`)
        .then(response => {
            product_list.value = response.data.results
        })
}
api_get_product(route.params.id)
api_get_product_image(route.params.id)
api_get_product_price(route.params.id)
api_get_product_rate(route.params.id)
api_get_list_product()

const get_discount = (a, b) => {
    return Math.abs(a - b)
}

const get_min_max_price = (list) => {
    let min = list[0].price;
    let max = list[0].price;
    for (let i = 0; i < list.length; i++) {
        if (list[i].price < min) {
            min = list[i].price
        }
        if (list[i].price > max) {
            max = list[i].price
        }
    }
    return [min, max]
}

const load_more_rate = () => {
    axios.get(have_more_rate.value)
        .then(response => {
            for (let i = 0; i < response.data.results.length; i++) {
                product_rate.value.push(response.data.results[i])
            }
            if (response.data.next) {
                have_more_rate.value = response.data.next
            }
            else have_more_rate.value = null
        })
}

</script>

<template>
    <div class="notification">
        <p>Thông báo: Từ ngày 01/01/2024 BeeCost.Vn sẽ chuyển đổi thương hiệu và địa chỉ website thành MuaThongMinh.Vn
        </p>
    </div>
    <Header></Header>

    <div class="product">
        <div class="product-link">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" width="20">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6">
                </path>
            </svg>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" width="20">
                <path
                    d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                    clip-rule="evenodd"></path>
            </svg>
            <p>Máy tính &amp; Laptop</p>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" width="20">
                <path
                    d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                    clip-rule="evenodd"></path>
            </svg>
            <p>Phụ Kiện Máy Tính</p>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" width="20">
                <path
                    d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                    clip-rule="evenodd"></path>
            </svg>
            <p>Bộ chia cổng USB &amp; Đọc thẻ nhớ</p>
        </div>

        <div class="product-main">
            <div class="product-main-image">
                <ProductImage :id="route.params.id"></ProductImage>
            </div>
            <div style="width: 50%;">
                <h3>{{ product?.name }}</h3>

                <button type="button" class="product-follow mt-3" @click="show_price_board = true">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="#ff7227" width="24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9">
                        </path>
                    </svg>
                    <p>Theo dõi giảm giá</p>
                </button>
                <div class="board" v-if="show_price_board">
                    <div class="board-card">
                        <div style="text-align: end;">
                            <button type="button" @click="show_price_board = false"
                                style="background-color: transparent !important;">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" width="20"
                                    stroke="#000000">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M6 18L18 6M6 6l12 12"></path>
                                </svg>
                            </button>
                        </div>
                        <div>
                            <div class="d-flex justify-content-center">
                                <div class="card-bell">
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" width="24"
                                        stroke="#ff7227">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9">
                                        </path>
                                    </svg>
                                </div>
                            </div>
                            <div class="mt-2 text-center sm:mt-5">
                                <h5>Nhận thông báo khi giảm giá</h5>
                                <div class="mt-3">
                                    <p>Bạn có muốn nhận thông báo qua email ngay khi sản phẩm này vừa giảm giá?</p>
                                    <div class="product-card-mini">
                                        <img v-if="product_image" :src="`${api}/${product_image[0].image}`"
                                            style="width: 70px;">
                                        <div class="">
                                            <p>{{ product?.name }}</p>
                                            <p style="color: red;">{{ formatNumber(product?.price) }} ₫</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div>
                            <div class="email-input">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" width="20">
                                    <path fill="gray"
                                        d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z">
                                    </path>
                                    <path fill="gray" d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z">
                                    </path>
                                </svg>
                                <input type="text" name="email" placeholder="Email của bạn"
                                    style="border: none;outline: none;width: 90%;">
                            </div>
                            <button type="button" class="btn btn-primary" style="width: 100%; margin-top: 5px;">
                                Đăng ký theo dõi giảm giá
                            </button>
                        </div>
                    </div>
                </div>

                <p class="mt-3 mb-3">
                    <span>Giá từ {{ product?.channel.name }}</span>
                    <img alt="Shopee" class="channel-icon ms-2" :src="`${api}/${product?.channel.image}`" lazy="loaded">
                </p>

                <div class="price-slot">
                    <div v-if="product_price">
                        <p class="price-current">{{ formatNumber(product_price[0].display_price) }} ₫</p>
                        <p class="price-before-discount">{{ formatNumber(product_price[0].price) }} ₫</p>
                    </div>
                    <div class="btn-green">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" width="20"
                            stroke="#047857">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M13 17h8m0 0V9m0 8l-8-8-4 4-6-6"></path>
                        </svg>
                        <p v-if="product_price">{{ formatNumber(get_discount(product_price[0].price, product_price[0].display_price))
                            }} ₫</p>
                    </div>
                    <div class="btn-orange">
                        <p>Đến nơi bán</p>
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="white"
                            width="24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M17 8l4 4m0 0l-4 4m4-4H3">
                            </path>
                        </svg>
                    </div>
                </div>

                <div class="rate-slot">
                    <div class="d-flex">
                        <p style="color:#fbbf24; padding-top: 2px;">{{ product?.rate }}</p>
                        <div class="ms-2">
                            <svg focusable="false" data-prefix="fas" data-icon="star" role="img"
                                xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" width="20"
                                v-for="i in Array.from({ length: parseInt(product?.rate) })">
                                <path fill="#fbbf24"
                                    d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z">
                                </path>
                            </svg>
                            <svg focusable="false" data-prefix="fas" data-icon="star-half-alt" role="img"
                                xmlns="http://www.w3.org/2000/svg" viewBox="0 0 536 512" width="20"
                                v-if="product?.rate % 1 > 0">
                                <path fill="#fbbf24"
                                    d="M508.55 171.51L362.18 150.2 296.77 17.81C290.89 5.98 279.42 0 267.95 0c-11.4 0-22.79 5.9-28.69 17.81l-65.43 132.38-146.38 21.29c-26.25 3.8-36.77 36.09-17.74 54.59l105.89 103-25.06 145.48C86.98 495.33 103.57 512 122.15 512c4.93 0 10-1.17 14.87-3.75l130.95-68.68 130.94 68.7c4.86 2.55 9.92 3.71 14.83 3.71 18.6 0 35.22-16.61 31.66-37.4l-25.03-145.49 105.91-102.98c19.04-18.5 8.52-50.8-17.73-54.6zm-121.74 123.2l-18.12 17.62 4.28 24.88 19.52 113.45-102.13-53.59-22.38-11.74.03-317.19 51.03 103.29 11.18 22.63 25.01 3.64 114.23 16.63-82.65 80.38z">
                                </path>
                            </svg>
                            <svg focusable="false" data-prefix="fas" data-icon="star" role="img"
                                xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" width="20" stroke="#fbffd4"
                                v-else>
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1"
                                    d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z">
                                </path>
                            </svg>
                        </div>
                    </div>
                    <div class=""><span>{{ product?.rate_count }}</span> <span class="color-gray">đánh giá</span></div>
                    <div class=""><span>{{ product?.sold }}</span> <span class="color-gray">lượt bán</span></div>
                </div>
            </div>
        </div>
        <div class="product-infor">
            <div class="tab1 mb-3">
                <h4>So sánh giá</h4>
                <p class="mt-3 mb-3" v-if="product_list">Tìm thấy <b>{{ product_list.length }}</b> nơi bán khác, giá từ
                    <b>{{ formatNumber(get_min_max_price(product_list)[0]) }} ₫ -
                        {{ formatNumber(get_min_max_price(product_list)[1]) }} ₫</b>
                </p>
                <div class="mb-3">
                    <img src="../assets/shopee-logo-text.png" style="width: 130px;" class="mb-3">
                    <div v-for="i in product_list">
                        <div class="product-card-big mb-3" v-if="i.channel.name == 'Shopee'">
                            <img :src="`${api}/${i.image}`" style="width: 80px;">
                            <div>
                                <p>{{ i.name }}</p>
                                <small>{{ i.sold }} <span class="color-gray">đã bán</span></small>
                            </div>
                            <p class="price-card">{{ formatNumber(i.price) }} ₫</p>
                            <router-link class="btn-orange" :to="{ name: 'product', params: { id: i.id } }">
                                <p>Đến nơi bán</p>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="white"
                                    width="24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M17 8l4 4m0 0l-4 4m4-4H3">
                                    </path>
                                </svg>
                            </router-link>
                        </div>
                    </div>
                </div>
                <div class="mb-3 mt-3">
                    <img src="../assets/lazada-logo-text.png" style="width: 130px;" class="mb-3">
                    <div v-for="i in product_list">
                        <div class="product-card-big mb-3" v-if="i.channel.name == 'Lazada'">
                            <img :src="`${api}/${i.image}`" style="width: 80px;">
                            <div>
                                <p>{{ i.name }}</p>
                                <small>{{ i.sold }} <span class="color-gray">đã bán</span></small>
                            </div>
                            <p class="price-card">{{ formatNumber(i.price) }} ₫</p>
                            <router-link class="btn-orange" :to="{ name: 'product', params: { id: i.id } }">
                                <p>Đến nơi bán</p>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="white"
                                    width="24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M17 8l4 4m0 0l-4 4m4-4H3">
                                    </path>
                                </svg>
                            </router-link>
                        </div>
                    </div>
                </div>
                <div class="mt-3 mb-3">
                    <img src="../assets/tiki-logo-text.png" style="width: 130px;" class="mb-3">
                    <div v-for="i in product_list">
                        <div class="product-card-big mb-3" v-if="i.channel.name == 'Tiki'">
                            <img :src="`${api}/${i.image}`" style="width: 80px;">
                            <div>
                                <p>{{ i.name }}</p>
                                <small>{{ i.sold }} <span class="color-gray">đã bán</span></small>
                            </div>
                            <p class="price-card">{{ formatNumber(i.price) }} ₫</p>
                            <router-link class="btn-orange" :to="{ name: 'product', params: { id: i.id } }">
                                <p>Đến nơi bán</p>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="white"
                                    width="24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M17 8l4 4m0 0l-4 4m4-4H3">
                                    </path>
                                </svg>
                            </router-link>
                        </div>
                    </div>
                </div>
            </div>

            <div class="tab2 mb-3">
                <div class="align-items-center d-flex justify-content-between">
                    <h4>Lịch sử giá</h4>
                    <button type="button" class="product-follow" @click="show_price_board = true">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="#ff7227"
                            width="24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9">
                            </path>
                        </svg>
                        <p>Theo dõi giảm giá</p>
                    </button>
                </div>
                <div>
                    <PriceHistory :id="route.params.id"></PriceHistory>
                </div>
            </div>

            <div class="tab3 mb-3">
                <h4>Mô tả sản phẩm</h4>
                <p>{{ product?.description }}</p>
            </div>

            <div class="tab4 mb-3">
                <h4>Đánh giá từ người mua</h4>
                <div>
                    <div style="border-bottom: 1px solid #e8e8e8; padding: 10px;" v-if="product_rate"
                        v-for="i in product_rate">
                        <div class="profile-slot mb-2">
                            <div class="avatar-slot">
                                <img alt="Shopee" style="width: 100%;"
                                    src="https://lh3.googleusercontent.com/mvI9jsrKjP7Q7ZqYOXuJTRZF9Q1e4PZJjjmNAyzh6OKtxtSUNPK920MMFsXploU60VPMqHCdJLEMzaEF_ktvIXuII2IEamnw0Cr5Cb97_803ePqQQYOLtHQLrVUe9e2DPZ3MoxTp"
                                    lazy="loaded">
                            </div>
                            <div>
                                <p>user1234324445</p>
                                <div>
                                    <svg focusable="false" data-prefix="fas" data-icon="star" role="img"
                                        xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" width="18"
                                        v-for="i in Array.from({ length: parseInt(i.rate) })">
                                        <path fill="#fbbf24"
                                            d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z">
                                        </path>
                                    </svg>
                                    <svg focusable="false" data-prefix="fas" data-icon="star" role="img"
                                        xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" width="18"
                                        v-for="i in Array.from({ length: 5 - parseInt(i.rate) })">
                                        <path fill="#e7e0ce"
                                            d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z">
                                        </path>
                                    </svg>
                                </div>
                            </div>
                        </div>
                        <p>{{ i.content }}</p>
                        <div class="rate-image mt-2">
                            <img style="width: 90px; border: 1px solid #e8e8e8;" :src="`${api}/${j}`"
                                v-for="j in i.image">
                        </div>
                    </div>
                    <div class="d-flex justify-content-center mt-2">
                        <button type="button" class="product-follow" v-if="have_more_rate" @click="load_more_rate">Xem
                            thêm</button>
                    </div>
                </div>
            </div>

            <div>
                <h4>Gợi ý dành cho bạn</h4>
                <div style="width: 100%; display: grid; margin-top: 20px;">
                    <ProductSuggest></ProductSuggest>
                </div>
            </div>
        </div>
        <div class="blog-slot">
            <div class="blog-card">
                <div>
                    <img style="width: 100%;"
                        src="https://static.beecost.vn/upload/uploads/2020/03/1584424796.6228461..jpe">
                </div>
                <div class="">
                    <h5>
                        Có nên mua và sử dụng pin laptop giá rẻ không ?
                    </h5>
                    <p style="height: 100px; overflow: hidden;">
                        Giá một chiếc pin laptop mới sẽ là không hề rẻ chút nào đối với những học sinh, sinh
                        viên. Cho nên, không ít sinh viên nghĩ tới phương án.
                        Tuy nhiên, việc sử dụng loại pin giá rẻ này có thực sự tốt, nên
                        hay không nên?
                    </p>
                    <div class="bg-dark-subtle mt-4 p-2 text-center">
                        <p>ĐỌC THÊM</p>
                    </div>
                </div>
            </div>
            <div class="blog-card">
                <div>
                    <img src="https://static.beecost.vn/upload/uploads/2020/03/1584427223.9663014..jpe"
                        style="width: 100%;">
                </div>
                <div class="">
                    <h5>
                        Quạt tản gió là gì? Ưu nhược điểm của quạt tản gió
                    </h5>
                    <p style="height: 100px; overflow: hidden;">
                        Được sử dụng phổ biến, thế nhưng khi nhắc tới “quạt tản gió” đa số mọi người lại không
                        hề biết chúng là gì? Bài viết này BeeCost sẽ giúp bạn hiểu hơn về khái niệm quạt tản gió
                        cũng như những ưu và nhược điểm của chúng.
                    </p>
                    <div class="bg-dark-subtle mt-4 p-2 text-center">
                        <p>ĐỌC THÊM</p>
                    </div>
                </div>
            </div>
            <div class="blog-card">
                <div>
                    <img src="https://static.beecost.vn/upload/uploads/2020/03/1584427774.4921753..jpe"
                        style="width: 100%;">
                </div>
                <div class="">
                    <h5>
                        Hướng dẫn kiểm tra độ chai pin khi mua laptop cũ
                    </h5>
                    <p style="height: 100px; overflow: hidden;">
                        Ngoài cấu hình máy, màn hình, vỏ máy… thì pin laptop cũng được khá nhiều người quan tâm
                        khi mua laptop cũ. Chính vì vậy BeeCost sẽ hướng dẫn kiểm tra độ chai pin khi mua laptop
                        cũ để chọn được những chiếc laptop có pin chai ít nhất.
                    </p>
                    <div class="bg-dark-subtle mt-4 p-2 text-center">
                        <p>ĐỌC THÊM</p>
                    </div>
                </div>
            </div>
        </div>
        
        <Report></Report>
    </div>
    
    <Popup></Popup>
    <Footer></Footer>
</template>

<style>
.product {
    text-align: start;
    display: grid;
    place-items: center;
    border-top: 1px solid rgb(214, 214, 214);
}

.product-link {
    display: flex;
    width: 80%;
    gap: 10px;
    padding: 10px 0 10px 0;
    margin-bottom: 20px;
}

.product-main {
    display: flex;
    width: 80%;
    gap: 20px;
}

.product-main-image{
    width: 40%;
    border: 1px solid rgb(212, 212, 212);
    border-radius: 15px;
    padding: 10px;
}

.product-follow {
    border: 1px solid #ff7227;
    border-radius: 20px;
    display: flex;
    gap: 5px;
    padding: 5px 15px;
    width: max-content;
    color: #ff7227;
}

.product-follow:hover {
    background: #ff7227;
    color: white;
    border: 1px solid #ff7227;
}

.product-follow:hover>svg {
    stroke: white;
}

.price-slot {
    display: flex;
    width: 90%;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}

.price-current {
    font-size: 25px;
    color: red;
    font-weight: 700;
}

.price-before-discount {
    text-decoration: line-through;
}

.rate-slot {
    display: flex;
    gap: 30px;
    align-items: center;
}

.board {
    position: fixed;
    width: 100vw;
    height: 100vh;
    background: rgba(105, 143, 204, 0.62);
    z-index: 20;
    top: 0;
    left: 0;
    display: grid;
    place-items: center;
}

.board-card {
    width: max-content;
    height: max-content;
    border-radius: 10px;
    background: white;
    padding: 20px;
}

.card-bell {
    background: #ff73271f;
    border-radius: 50%;
    padding: 5px 4px 5px 6px;
    width: 50px;
    aspect-ratio: 1;
    display: grid;
    place-items: center;
}

.product-card-mini {
    margin-top: 10px;
    display: flex;
    gap: 5px;
    box-shadow: 0 0 0 0 rgba(0, 0, 0, 0.2), 0 5px 10px 0 rgba(0, 0, 0, 0.19);
    justify-content: center;
    align-items: center;
    border-radius: 10px;
}

.email-input {
    width: 100%;
    border: 1px solid rgb(177, 177, 177);
    border-radius: 5px;
    display: flex;
    gap: 5px;
    padding: 5px 10px;
    margin-top: 20px;
}

.product-infor {
    width: 80%;
    margin-top: 20px;
}

.product-card-big {
    display: flex;
    gap: 15px;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 0 0 0 rgba(0, 0, 0, 0.2), 0 5px 10px 0 rgba(0, 0, 0, 0.19);
    border-radius: 10px;
    width: max-content;
    padding: 10px 20px;
    min-width: 600px;
}

.product-card-big:hover {
    box-shadow: 0 0px 5px 0 rgba(0, 0, 0, 0.2), 0 15px 20px 0 rgba(0, 0, 0, 0.19);
}

.price-card {
    color: red;
    font-size: 18px;
    font-weight: 500;
}

.profile-slot {
    display: flex;
    height: max-content;
    gap: 10px;
    align-items: center;
}

.rate-image {
    display: flex;
    gap: 10px;
}

.blog-slot {
    width: 80%;
    margin-top: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: max-content;
}

.blog-card {
    width: 30%;
    height: 500px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    text-align: justify;
    justify-content: space-between;
}
</style>