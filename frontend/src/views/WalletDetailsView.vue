<template>
  <div class="container">
    <div class="row py-3">
      <div
        v-if="type === WALLET_DETAILS_FAIL"
        class="alert alert-warning"
        role="alert"
      >
        {{ error }}
      </div>
    </div>
    <div class="row py-3">
      <h2>{{ wallet.name }}</h2>
    </div>
    <div class="row py-3" v-if="type === WALLET_DETAILS_SUCCESS">
      <WalletAssetsEthComponent :assets_eth="wallet_details.AssetsETH" />
      <WalletAssetsERC20Component :assets_erc20="wallet_details.AssetsERC20" />
      <WalletAssetsNFTDetails :assets_nft="wallet_details.AssetsNFT" />
    </div>
    <div
      v-else-if="type === WALLET_DETAILS_REQUEST"
      class="spinner-border"
      role="status"
    ></div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { storeToRefs } from "pinia";
import { useWalletDetailsStore } from "@/stores/wallet_details_store";
import {
  WALLET_DETAILS_FAIL,
  WALLET_DETAILS_REQUEST,
  WALLET_DETAILS_SUCCESS,
} from "@/../constants/wallet_constants";
import WalletAssetsEthComponent from "@/components/WalletAssetsEthComponent.vue";
import WalletAssetsERC20Component from "@/components/WalletsAssetsERC20Component.vue";
import WalletAssetsNFTDetails from "@/components/WalletAssetsNFTDetails.vue";

const route = useRoute();
const wallet_detail_store = useWalletDetailsStore();
const { wallet_details, type, error } = storeToRefs(wallet_detail_store);
const wallet = ref({});
onMounted(() => {
  wallet.value = localStorage.getItem("current_wallet")
    ? JSON.parse(localStorage.getItem("current_wallet") ?? "")
    : {};
  wallet_detail_store.getWalletDetailsAction(Number(route.params.id));
});
</script>

<style scoped>
img {
  width: 30px;
  height: auto;
}
</style>
