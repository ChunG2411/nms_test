const api = "http://127.0.0.1:8000"

const formatNumber = (number)=>{
    return new Intl.NumberFormat("de-DE").format(number)
}

export { api, formatNumber }