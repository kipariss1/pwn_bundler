<template>
    <div class="card" style="width: 40rem;">
        <div class="card-body">
            <div class="row align-self-center">
                <div class="col">
                    <h5 class="card-title">NFT assets:</h5>
                </div>  
            </div>
            <div class="row py-3" v-for="asset in assets_nft" :key="asset._uid">
                <div class="col">
                    <img
                        src="/public/img/nft.png"
                    />
                </div>
                <div class="col">
                    <h6>{{ asset.metadata.name }}</h6>
                    {{ asset.metadata.description }}
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">

    // TODO: make the typing of props
    import type { PropType } from 'vue'
    import type { WalletNFTAsset } from '@/interfaces/wallet_details_interface';
    import { onMounted } from 'vue'

    const props = defineProps({
        assets_nft: {
            type: Array as PropType<Array<WalletNFTAsset>>,
            required: true
        }
    })

    onMounted(() => {
        props.assets_nft.forEach((asset) => {
            asset.metadata = JSON.parse(asset.metadata);
        })
    })
</script>

<style scoped>
    img {
        width: 60px;
        height: auto;
    }
</style>