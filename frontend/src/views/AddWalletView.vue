<template>
  <div class="container">
    <div class="row py-3">
      <div
        v-if="type === WALLET_ADD_FAIL"
        class="alert alert-warning"
        role="alert"
      >
        {{ error }}
      </div>
      <div
        v-else-if="type === WALLET_ADD_SUCCESS"
        class="alert alert-success"
        role="alert"
      >
        Wallet was successfully added
      </div>
    </div>
    <div
      v-if="type === WALLET_ADD_REQUEST"
      class="spinner-border"
      role="status"
    >
      <span class="sr-only">Loading...</span>
    </div>
    <div
      class="row py-3 justify-content-center"
      v-if="type === WALLET_ADD_IDLE"
    >
      <div class="col-4">
        <form @submit="submitNewWallet">
          <div class="form-group">
            <label for="w_name">Name</label>
            <input
              type="text"
              class="form-control"
              id="w_name"
              placeholder="New wallet's name"
            />
          </div>
          <div class="form-group">
            <label for="w_address">Address</label>
            <input
              type="text"
              class="form-control"
              id="w_address"
              placeholder="New wallet's address"
            />
          </div>
          <button type="submit" class="btn btn-primary">Add</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAddWalletStore } from "@/stores/add_wallet_store";
import { storeToRefs } from "pinia";
import {
  WALLET_ADD_FAIL,
  WALLET_ADD_REQUEST,
  WALLET_ADD_SUCCESS,
  WALLET_ADD_IDLE,
} from "@/../constants/wallet_constants";
import { onMounted } from "vue";

const add_wallet_store = useAddWalletStore();
const { type, error } = storeToRefs(add_wallet_store);
onMounted(() => {
    add_wallet_store.$reset();
})
async function submitNewWallet(event: Event) {
  event.preventDefault();
  let name: string = event.target.elements.w_name.value;
  let address: string = event.target.elements.w_address.value;
  add_wallet_store.postNewWalletDetailsAction(name, address);
}
</script>

<style scoped></style>
