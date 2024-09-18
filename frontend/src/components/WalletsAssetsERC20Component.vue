<template>
    <div class="card" style="width: 40rem;">
        <div class="card-body">
            <div class="row align-self-center">
                <div class="col">
                    <h5 class="card-title">ERC20 balance:</h5>
                </div>  
            </div>
            <div class="row">
                <div class="col">
                    <img
                        src="/public/img/eth.png"
                    />
                </div>
                <div class="col" v-for="asset in assets_erc20">
                    {{ asset }}
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

    const props = defineProps({
        assets_erc20: {
            type: Array,
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