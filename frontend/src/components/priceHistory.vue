<script setup>
import { Line } from 'vue-chartjs'
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
} from 'chart.js'

import { api, formatNumber } from '../utils/config.js'
import axios from 'axios'
import { ref, defineProps, watch } from 'vue';

const props = defineProps({
    id: String
})
const product_price = ref(null)

watch(() => props.id, (currentvalue, oldvalue) => {
    api_get_product_price(currentvalue)
})

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
)

const data = ref({
    labels: [],
    datasets: [
        {
            data: []
        }
    ]
})
const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            display: false,
        },
    },
}

const api_get_product_price = (id) => {
    axios.get(`${api}/api/product/price/${id}`)
        .then(response => {
            product_price.value = response.data.results
            data.value = {
                labels: product_price.value.map(price => price.created.slice(0, 10)).reverse(),
                datasets: [
                    {
                        data: product_price.value.map(price => price.display_price).reverse()
                    }
                ]
            }
        })
}
api_get_product_price(props.id)

</script>

<template>
    <div class="chart-slot">
        <div class="d-flex justify-content-between">
            <h5 class="color-orange">Biến động giá</h5>
            <p>Giá hiện tại: <b style="font-size: 18px;color: red;" v-if="product_price">{{
                formatNumber(product_price[0].display_price) }} ₫</b></p>
        </div>
        <div class="d-flex justify-content-between mb-2">
            <p>Cao nhất <b>{{ formatNumber(Math.max(...data.datasets[0].data)) }} ₫</b> - Thấp nhất <b>{{
                formatNumber(Math.min(...data.datasets[0].data)) }} ₫</b></p>
            <p>Từ <b>{{ data.labels[0] }}</b> đến <b>{{ data.labels[data.labels.length - 1] }}</b></p>
        </div>
        <div style="height: 400px;">
            <Line :data="data" :options="options" />
        </div>
    </div>
</template>

<style>
.chart-slot {
    width: 100%;
    height: max-content;
    border: 1px solid #ff7227;
    border-radius: 10px;
    padding: 20px;
    margin-top: 10px;
}
</style>