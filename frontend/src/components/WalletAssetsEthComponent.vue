<template>
    <div class="card" style="width: 40rem;">
        <div class="card-body">
            <div class="row align-self-center">
                <div class="col">
                    <h5 class="card-title">Etherium balance:</h5>
                </div>  
            </div>
            <div class="row">
                <div class="col">
                    <img
                    src="/public/img/eth.png"
                    />
                </div>
                <div class="col">
                    {{ assets_eth }}
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

const props = defineProps({
    assets_eth: {
        type: Number,
        required: true
    }
})

</script>

<style scoped>
    img {
        width: 30px;
        height: auto;
    }
</style>