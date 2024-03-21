<template>
  <div class="swiper mb-3">
    <div class="swiper-wrapper">
      <div class="swiper-slide" :id="i.id" v-for="i in list_suggest">
        <div>
          <img :src="`${api}/${i.image}`" style="width: 100%;">
        </div>

        <div style="width: 100%;padding: 10px 10px 20px 10px;">
          <p>{{ i.name }}</p>
          <p style="color: red;">{{ formatNumber(i.price) }} ₫</p>
        </div>

        <div class="swiper-slide-button" :id="i.id">
          <router-link class="btn-orange" :to="{ name: 'product', params: { id: i.id } }">
            <p>Đến nơi bán</p>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="white" width="24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3">
              </path>
            </svg>
          </router-link>
        </div>
      </div>
    </div>
    <div class="swiper-button-prev"></div>
    <div class="swiper-button-next"></div>
  </div>
</template>

<script setup>
import { formatNumber } from '../utils/config.js'

setTimeout(() => {
  const swiper = new Swiper('.swiper', {
    slidesPerView: 4,
    spaceBetween: 10,
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });

  const element1 = document.querySelectorAll('.swiper-slide');
  const element2 = document.querySelectorAll('.swiper-slide-button');

  element1.forEach(i => {
    i.addEventListener('mouseover', () => {
      i.style.border = '1px solid #ff7227';
      element2.forEach(j => {
        if (j.id == i.id) {
          j.style.display = 'grid'
        }
      })
    });
    i.addEventListener('mouseout', () => {
      i.style.border = '1px solid rgb(221, 221, 221)';
      element2.forEach(j => {
        if (j.id == i.id) {
          j.style.display = 'none'
        }
      })
    });
  });
}, 500);

import { ref } from 'vue';
import axios from 'axios'
import { api } from '../utils/config.js'

const list_suggest = ref([])

const get_suggest = () => {
  axios.get(`${api}/api/product?all=true`)
    .then(response => {
      list_suggest.value = response.data
    })
}
get_suggest()

</script>

<style>
.swiper {
  width: 100%;
  height: 400px;
}

.swiper-slide {
  display: flex;
  gap: 10px;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  border: 1px solid rgb(221, 221, 221);
  max-width: 250px;
  width: 250px;
}

.swiper-slide-button {
  position: absolute;
  display: none;
  place-items: center;
  height: 100%;
  background: rgba(223, 223, 223, 0.404);
  width: 100%;
}

.swiper-button-next,
.swiper-button-prev {
  color:black;
  background:rgba(255, 255, 255, .8);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 1px solid rgb(214, 214, 214);
  z-index: 9;
}

.swiper-button-next,
.swiper-button-prev::after {
  font-size: 18px;
  font-weight: 600;
}

.swiper-button-prev,
.swiper-button-next::after {
  font-size: 18px;
  font-weight: 600;
}

.swiper-button-next {
  right: 0px;
}

.swiper-button-prev {
  left: 0px;
}

.swiper-button-next:hover {
  color: #ff7227;
}

.swiper-button-prev:hover {
  color: #ff7227;
}
</style>
