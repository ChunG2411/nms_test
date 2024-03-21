<script setup>
import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale,
    ArcElement,
    Filler
} from 'chart.js'
import { Bar } from 'vue-chartjs'
import { Pie } from 'vue-chartjs'

import { api, formatNumber } from '../utils/config.js'
import axios from 'axios'
import { ref, reactive } from 'vue';

const product_price = reactive({
    sales: 0,
    sold: 0,
    product: 0,
    shop: 0
})
const type = ref('industry')
const data_industry = ref({
    labels: [],
    datasets: [
        {
            backgroundColor: '#468cdd',
            data: []
        }
    ]
})
const options_industry = {
    responsive: true,
    maintainAspectRatio: false,
    indexAxis: 'y',
    plugins: {
        legend: {
            display: false,
        },
    },
    scales: {
        y: {
            ticks: {
                crossAlign: 'far',
            },
        },
    }
}
const data_brand = ref({
    labels: [],
    datasets: [
        {
            backgroundColor: [],
            data: []
        }
    ]
})
const options_brand = {
    responsive: true,
    maintainAspectRatio: false,
}
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend, ArcElement, Filler)


const api_get_statistical_industry = () => {
    axios.get(`${api}/api/industry/statistical`)
        .then(response => {
            for (let i = 0; i < response.data.length; i++) {
                product_price.sales += response.data[i].sales
                product_price.sold += response.data[i].sold
                product_price.product += response.data[i].product
                product_price.shop += response.data[i].shop
            }
            data_industry.value = {
                labels: response.data.map(data => data.industry.name),
                datasets: [
                    {
                        backgroundColor: '#468cdd',
                        data: response.data.map(data => data.sales)
                    }
                ]
            }
        })
}
const api_get_statistical_brand = () => {
    axios.get(`${api}/api/brand/statistical`)
        .then(response => {
            data_brand.value = {
                labels: response.data.map(data => data.brand.name),
                datasets: [
                    {
                        backgroundColor: response.data.map(data => '#' + Math.floor(Math.random() * 16777215).toString(16)),
                        data: response.data.map(data => data.sales)
                    }
                ]
            }
        })
}
api_get_statistical_industry()
api_get_statistical_brand()
</script>

<template>
    <div class="statistical-slot">
        <div>
            <h5 style="color: #ff7227;">Số liệu E-Commerce cho người bán/doanh nghiệp</h5>
        </div>
        <div class="d-flex gap-3">
            <select name="brand" id="brand" class="form-select w-auto">
                <option value="shopee" selected>Shopee</option>
                <option value="lazada">Lazada</option>
                <option value="tiki">Tiki</option>
            </select>
            <select name="duration" id="duration" class="form-select w-auto">
                <option value="7">Trong 7 ngày</option>
                <option value="30" selected>Trong 30 ngày</option>
            </select>
            <select name="type" id="type" class="form-select w-auto" v-model="type">
                <option value="industry">Ngành hàng</option>
                <option value="brand" selected>Thương hiệu</option>
            </select>
        </div>
        <div class="statistical-card-slot">
            <h6>Số liệu kênh bán Shopee trong 30 ngày</h6>
            <div class="d-flex justify-content-between">
                <div class="statistical-card">
                    <p>DOANH SỐ</p>
                    <p>{{ formatNumber(product_price.sales) }} ₫</p>
                    <svg width="95" height="94" viewBox="0 0 95 94" fill="none"
                        style="position: absolute;right: 0;top: 0;" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd"
                            d="M125.423 -17.5522C136.269 -13.986 139.684 1.1071 139.99 12.5629C140.258 22.6076 130.975 29.7568 126.932 38.9763C123.694 46.3599 123.668 54.7301 118.709 61.0889C112.669 68.8354 105.507 76.3787 95.9826 78.6667C85.4798 81.1897 73.3338 80.583 64.7809 74.044C56.377 67.6189 57.3494 54.9913 52.6172 45.5122C47.0114 34.2835 33.7593 26.0958 34.5716 13.5324C35.4052 0.640703 44.2612 -13.6824 56.6731 -17.2136C69.4344 -20.8443 79.4224 -2.93104 92.668 -2.99626C104.885 -3.05642 113.834 -21.3625 125.423 -17.5522Z"
                            fill="#FDBC64"></path>
                        <path opacity="0.1" fill-rule="evenodd" clip-rule="evenodd"
                            d="M113.563 -17.5522C124.409 -13.986 127.824 1.10711 128.13 12.5629C128.399 22.6076 119.116 29.7568 115.073 38.9763C111.835 46.3599 111.808 54.7301 106.85 61.0889C100.809 68.8354 93.6476 76.3787 84.1233 78.6667C73.6205 81.1897 61.4745 80.583 52.9215 74.044C44.5176 67.6189 45.49 54.9913 40.7578 45.5122C35.152 34.2835 21.8999 26.0958 22.7123 13.5324C23.5459 0.640697 32.4018 -13.6824 44.8137 -17.2136C57.575 -20.8443 67.563 -2.93104 80.8086 -2.99626C93.0255 -3.05641 101.975 -21.3625 113.563 -17.5522Z"
                            fill="#FDBC64"></path>
                    </svg>
                </div>
                <div class="statistical-card">
                    <p>SẢN PHẨM ĐÃ BÁN</p>
                    <p>{{ formatNumber(product_price.sold) }}</p>
                    <svg width="70" height="86" viewBox="0 0 70 86" fill="none"
                        style="position: absolute;right: 0;top: 0;" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd"
                            d="M10.3987 0.529322C10.3339 -11.5986 24.3861 -20.1275 35.8225 -24.2983C45.8502 -27.9554 56.1816 -21.0155 66.8318 -20.0515C75.3613 -19.2794 83.8016 -22.0748 91.8788 -19.2241C101.719 -15.7513 111.732 -11.0804 117.248 -2.25792C123.331 7.47103 126.815 19.9105 123.112 30.7308C119.474 41.3626 106.426 44.6408 98.4729 52.6038C89.0521 62.0366 85.2728 78.1464 72.3436 81.5642C59.0764 85.0713 41.6625 80.9799 33.9204 69.6678C25.9604 58.0373 40.637 41.9363 36.1052 28.6158C31.9254 16.3298 10.4679 13.4875 10.3987 0.529322Z"
                            fill="#FF738C" fill-opacity="0.8"></path>
                        <path opacity="0.2" fill-rule="evenodd" clip-rule="evenodd"
                            d="M0.703402 3.43753C0.638612 -8.69038 14.6907 -17.2193 26.1272 -21.3901C36.1549 -25.0472 46.4863 -18.1073 57.1365 -17.1433C65.6659 -16.3712 74.1063 -19.1666 82.1835 -16.3159C92.0234 -12.8431 102.037 -8.17224 107.553 0.650288C113.636 10.3792 117.12 22.8187 113.417 33.639C109.778 44.2708 96.7304 47.549 88.7776 55.512C79.3567 64.9448 75.5775 81.0546 62.6483 84.4724C49.3811 87.9795 31.9672 83.8881 24.2251 72.576C16.2651 60.9455 30.9417 44.8445 26.4099 31.524C22.2301 19.238 0.77263 16.3957 0.703402 3.43753Z"
                            fill="#FF738C"></path>
                    </svg>
                </div>
                <div class="statistical-card">
                    <p>SẢN PHẨM CÓ LƯỢT BÁN</p>
                    <p>{{ formatNumber(product_price.product) }}</p>
                    <svg width="38" height="89" viewBox="0 0 38 89" fill="none"
                        style="position: absolute;right: 0;top: 0;" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd"
                            d="M30.1482 -5.11699C41.8797 -8.50481 50.9794 5.09563 60.482 12.736C67.2182 18.1522 73.7178 23.7619 76.3132 32.0011C78.8795 40.1483 77.4903 48.6479 74.2915 56.576C70.7074 65.459 65.8181 73.759 57.5233 78.571C46.9515 84.7039 34.1957 91.3749 23.1015 86.2722C11.8788 81.1105 7.99019 67.1518 6.16247 54.948C4.62934 44.7113 10.2527 35.7523 14.0944 26.1319C18.6083 14.8283 18.4404 -1.73601 30.1482 -5.11699Z"
                            fill="#84E8F4"></path>
                        <path opacity="0.2" fill-rule="evenodd" clip-rule="evenodd"
                            d="M24.6677 -5.11699C36.3992 -8.50481 45.4989 5.09563 55.0015 12.736C61.7378 18.1522 68.2374 23.7619 70.8327 32.0011C73.399 40.1483 72.0098 48.6479 68.811 56.576C65.2269 65.459 60.3377 73.759 52.0429 78.571C41.471 84.7039 28.7152 91.3749 17.621 86.2722C6.39837 81.1105 2.50972 67.1518 0.682 54.948C-0.851133 44.7113 4.77225 35.7523 8.61396 26.1319C13.1278 14.8283 12.96 -1.73601 24.6677 -5.11699Z"
                            fill="#84E8F4"></path>
                    </svg>
                </div>
                <div class="statistical-card">
                    <p>SHOP CÓ LƯỢT BÁN</p>
                    <p>{{ formatNumber(product_price.shop) }}</p>
                    <svg width="70" height="86" viewBox="0 0 70 86" fill="none"
                        style="position: absolute;right: 0;top: 0;" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd"
                            d="M10.3987 0.529322C10.3339 -11.5986 24.3861 -20.1275 35.8225 -24.2983C45.8502 -27.9554 56.1816 -21.0155 66.8318 -20.0515C75.3613 -19.2794 83.8016 -22.0748 91.8788 -19.2241C101.719 -15.7513 111.732 -11.0804 117.248 -2.25792C123.331 7.47103 126.815 19.9105 123.112 30.7308C119.474 41.3626 106.426 44.6408 98.4729 52.6038C89.0521 62.0366 85.2728 78.1464 72.3436 81.5642C59.0764 85.0713 41.6625 80.9799 33.9204 69.6678C25.9604 58.0373 40.637 41.9363 36.1052 28.6158C31.9254 16.3298 10.4679 13.4875 10.3987 0.529322Z"
                            fill="#FF6B00"></path>
                        <path opacity="0.2" fill-rule="evenodd" clip-rule="evenodd"
                            d="M0.703402 3.43753C0.63861 -8.69037 14.6907 -17.2193 26.1272 -21.3901C36.1549 -25.0472 46.4863 -18.1073 57.1365 -17.1433C65.6659 -16.3712 74.1063 -19.1666 82.1835 -16.3159C92.0234 -12.843 102.037 -8.17224 107.553 0.650288C113.636 10.3792 117.12 22.8187 113.417 33.639C109.778 44.2708 96.7304 47.549 88.7776 55.512C79.3567 64.9448 75.5774 81.0546 62.6483 84.4724C49.3811 87.9795 31.9672 83.8881 24.2251 72.576C16.2651 60.9455 30.9417 44.8445 26.4099 31.524C22.2301 19.238 0.77263 16.3957 0.703402 3.43753Z"
                            fill="#FF6B00"></path>
                    </svg>
                </div>
            </div>
        </div>
        <div class="text-center mt-2" v-if="type == 'industry'">
            <h6>Thống kê ngành hàng</h6>
            <div style="height: 400px;">
                <Bar :data="data_industry" :options="options_industry" />
            </div>
        </div>
        <div class="text-center mt-2" v-else>
            <h6>Thống kê thương hiệu</h6>
            <div style="height: 400px;">
                <Pie :data="data_brand" :options="options_brand" />
            </div>
        </div>
    </div>
</template>

<style>
.statistical-slot {
    border: 1px solid rgb(223, 223, 223);
    border-radius: 5px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding: 20px;
    text-align: start;
    margin-top: 30px;
    width: 80%;
    height: max-content;
}

.statistical-card-slot {
    border: 1px solid rgb(223, 223, 223);
    border-radius: 5px;
    padding: 15px;
    text-align: center;
    margin-top: 10px;
    width: 100%;
    height: max-content;
}

.statistical-card {
    background: #468cdd;
    padding: 20px;
    border-radius: 10px;
    color: white;
    font-weight: 500;
    text-align: start;
    margin-top: 20px;
    min-width: 250px;
    position: relative;
    overflow: hidden;
}
</style>