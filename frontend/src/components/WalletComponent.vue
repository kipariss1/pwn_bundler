<template>
  <li class="list-group-item">
    <router-link
      :to="`/wallet_details/${wallet.id}`"
      @click="logWalletToLocalStorage"
      ><font-awesome-icon :icon="['fas', 'wallet']" />
      {{ wallet.name }}</router-link
    >
  </li>
</template>

<script setup lang="ts">
const props = defineProps({
  wallet: {
    type: Object,
    required: true,
  },
});

function logWalletToLocalStorage() {
  localStorage.setItem("current_wallet", JSON.stringify(props.wallet));
}
</script>

<style scoped></style>
