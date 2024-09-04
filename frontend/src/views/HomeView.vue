<script setup lang="ts">

import { onMounted } from 'vue';
import { storeToRefs } from 'pinia';
import { useWalletsStore } from '@/../stores/wallet_store'
import { 
  WALLET_LIST_FAIL,
  WALLET_LIST_REQUEST,
  WALLET_LIST_SUCCESS, 
} from 'constatnts/wallet_constants';

const walletStore = useWalletsStore()
const { wallets, type, error } = storeToRefs(walletStore)

onMounted(() => {
  walletStore.getWallets()
})

</script>

<template>
  <div class="container">
    <div class='row py-3'>
      <div class="alert alert-warning" role="alert" v-if="type===WALLET_LIST_FAIL">
        {{ error }}
      </div>
      <h1>
        Welcome to PWN's Token Bundler
      </h1>
    </div>
    <div class="row">
      <div class="col-7">
        <h6>
          <li>Start by connecting your wallet <router-link>here</router-link></li>
          <li>Or continue by connecting another wallet <router-link>here</router-link></li>
        </h6>
      </div>
      <div class="col-5">
        <div class="card" style="width: 18rem;" v-if="type===WALLET_LIST_SUCCESS">
          <div class="card-header">
            List of connected wallets:
          </div>
          <ul class="list-group list-group-flush">
            <li class="list-group-item">Dummy wallet #1</li>
            <li class="list-group-item">Dummy wallet #2</li>
            <li class="list-group-item">Dummy wallet #3</li>
          </ul>
        </div>
      </div class="spinner-border" role="status" v-else-if="type===WALLET_LIST_REQUEST">
        <span class="sr-only">Loading...</span>
      </div>
    </div>
  </div>
</template>
