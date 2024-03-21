<script setup>
import { ref } from 'vue';

const click_popup = ref(false)
</script>

<template>
    <div class="popup">
        <div class="popup-content" v-if="click_popup">
            <h3>Gợi ý dành cho bạn</h3>
            <p>Tiện ích Mua Thông Minh giúp bạn xem tất cả các mức giá trong quá khứ của mọi sản phẩm (Shopee, Tiki,
                Lazada, Sendo). <b>Tiết kiệm gấp đôi</b></p>
            <div class="align-items-center d-flex gap-4 justify-content-end mt-1">
                <small @click="click_popup = false">Đóng lại</small>
                <button type="button" class="btn-orange">Xem thêm chi tiết</button>
            </div>
        </div>
        <div class="popup-image" @click="click_popup = !click_popup">
            <img src="../assets/popup.png" style="width: 100%;">
        </div>
    </div>
</template>

<style>
.popup {
    position: fixed;
    bottom: 20px;
    left: 20px;
    cursor: pointer;
    z-index: 100;
}

.popup-image {
    border-radius: 50%;
    aspect-ratio: 1;
    overflow: hidden;
    width: 80px;
    background-color: rgb(255, 207, 103);
    padding: 10px;
}

.popup-content {
    margin-bottom: 20px;
    width: 430px;
    height: max-content;
    background: white;
    border-radius: 10px;
    padding: 20px 30px;
    box-shadow: 0 0px 5px 0 rgba(0, 0, 0, 0.2), 0 5px 15px 0 rgba(0, 0, 0, 0.19);
    display: flex;
    flex-direction: column;
    gap: 10px;
    text-align: start;
    position: relative;
}
</style>