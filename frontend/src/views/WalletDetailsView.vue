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
      {{ wallet.name }}
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { storeToRefs } from "pinia";
import { useWalletDetailsStore } from "@/stores/wallet_details_store"
import { 
  WALLET_DETAILS_FAIL,
  WALLET_DETAILS_REQUEST,
  WALLET_DETAILS_SUCCESS, 
} from '@/../constants/wallet_constants'

export default defineComponent({
  setup() {
    const route = useRoute();
    const wallet_detail_store = useWalletDetailsStore()
    const { wallet_details, type, error } = storeToRefs(wallet_detail_store)
    const wallet = ref({});
    onMounted(() => {
        wallet.value = localStorage.getItem('current_wallet') ? JSON.parse(localStorage.getItem('current_wallet') ?? "") : {};
        wallet_detail_store.getWalletDetailsAction(Number(route.params.id));
    })
    return {
        wallet_details,
        type,
        error,
        wallet,
        WALLET_DETAILS_FAIL,
        WALLET_DETAILS_REQUEST,
        WALLET_DETAILS_SUCCESS,
    };
  },
});
</script>

<style scoped></style>
