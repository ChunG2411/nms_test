<script setup>
import { ref, defineProps, watch } from 'vue';
import { api } from '../utils/config.js'
import axios from 'axios'

const props = defineProps({
    id: String
})
const product_image = ref([])

watch(() => props.id, (currentvalue, oldvalue) => {
    api_get_product_image(currentvalue)
    get_swiper()
})

const get_swiper = () => {
    setTimeout(() => {
        const swiper = new Swiper('.swiper-bottom', {
            loop: true,
            slidesPerView: 4,
            spaceBetween: 10,
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
        });
        const element1 = document.querySelector('.image-preveiw');
        const element2 = document.querySelectorAll('.image-slice');

        element2.forEach(i => {
            i.addEventListener('mouseover', () => {
                element1.src = i.src
            });
        })
    }, 500);
}
get_swiper()

const api_get_product_image = (id) => {
    axios.get(`${api}/api/product/image/${id}`)
        .then(response => {
            product_image.value = response.data
        })
}
api_get_product_image(props.id)

</script>

<template>
    <div class="swiper-top">
        <img v-if="product_image[0]" :src="`${api}/${product_image[0].image}`" class="image-preveiw"
            style="width: 100%;">
    </div>
    <div class="swiper-bottom">
        <div class="swiper-wrapper">
            <div class="swiper-slide custom-slice" v-for="i in product_image">
                <img :src="`${api}/${i.image}`" class="image-slice" style="width: 100%;">
            </div>
        </div>
        <div class="swiper-button-prev"></div>
        <div class="swiper-button-next"></div>
    </div>
</template>

<style>
.swiper-top {
    width: 100%;
    aspect-ratio: 1;
}

.swiper-bottom {
    width: 100%;
    height: 100px;
    position: relative;
    overflow: hidden;
}

.custom-slice {
    border: 1px solid rgb(221, 221, 221);
    width: 100px !important;
    height: 100px !important;
}
</style>