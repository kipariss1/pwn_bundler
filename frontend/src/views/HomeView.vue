<script setup lang="ts">
import { onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useWalletsStore } from "@/stores/wallet_store";
import {
  WALLET_LIST_FAIL,
  WALLET_LIST_REQUEST,
  WALLET_LIST_SUCCESS,
} from "@/../constants/wallet_constants";

const walletStore = useWalletsStore();
const { wallets, type, error } = storeToRefs(walletStore);

onMounted(() => {
  walletStore.getWalletsAction();
});
</script>

<template>
  <div class="container">
    <div class="row py-3">
      <div
        v-if="type === WALLET_LIST_FAIL"
        class="alert alert-warning"
        role="alert"
      >
        {{ error }}
      </div>
    </div>
    <div class="row py-3">
      <h1>Welcome to PWN's Token Bundler</h1>
    </div>
    <div class="row">
      <div class="col-7">
        <h6>
          <li>
            Start by connecting your wallet <router-link>here</router-link>
          </li>
          <li>
            Or continue by connecting another wallet
            <router-link>here</router-link>
          </li>
        </h6>
      </div>
      <div class="col-5">
        <div
          v-if="type === WALLET_LIST_SUCCESS"
          class="card"
          style="width: 18rem"
        >
          <div class="card-header">List of connected wallets:</div>
          <ul class="list-group list-group-flush">
            <li class="list-group-item">Dummy wallet #1</li>
            <li class="list-group-item">Dummy wallet #2</li>
            <li class="list-group-item">Dummy wallet #3</li>
          </ul>
        </div>
        <div
          v-else-if="type === WALLET_LIST_REQUEST"
          class="spinner-border"
          role="status"
        >
          <span class="sr-only">Loading...</span>
        </div>
      </div>
    </div>
  </div>
</template>
