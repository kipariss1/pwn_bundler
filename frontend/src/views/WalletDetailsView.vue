<template>
  <div>Here will be wallet details</div>
</template>

<script lang="ts">
import { defineComponent, onMounted } from "vue";
import { useRoute } from "vue-router";
import { storeToRefs } from "pinia";
import { useWalletDetailsStore } from "@/stores/wallet_details_store"

export default defineComponent({
  setup() {
    const route = useRoute();
    const wallet_detail_store = useWalletDetailsStore()
    const { wallet_details, type, error } = storeToRefs(wallet_detail_store)
    onMounted(() => {
        wallet_detail_store.getWalletDetailsAction(Number(route.params.id))
    })
    return {
        wallet_details,
        type,
        error
    };
  },
});
</script>

<style scoped></style>
