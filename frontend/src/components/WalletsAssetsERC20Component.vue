<template>
    <div class="card" style="width: 40rem;">
        <div class="card-body">
            <div class="row align-self-center">
                <div class="col">
                    <h5 class="card-title">ERC20 assets:</h5>
                </div>  
            </div>
            <div class="row py-3" v-for="asset in assets_erc20" :key="asset._uid">
                <div class="col">
                    <img
                        src="/public/img/erc20.jpg"
                    />
                </div>
                <div class="col" >
                    <h6>{{ asset.name }}</h6>
                    Amount: {{ ethers.formatEther(asset.balance) }}
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">

    import type { PropType } from 'vue'
    import type { WalletERC20Asset } from '@/interfaces/wallet_details_interface';
    import { ethers } from 'ethers';

    const props = defineProps({
        assets_erc20: {
            type: Array as PropType<Array<WalletERC20Asset>>,
            required: true
        }
    })
</script>

<style scoped>
    img {
        width: 40px;
        height: auto;
    }
</style>