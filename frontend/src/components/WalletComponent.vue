<template>
  <li class="list-group-item">
    <!-- TODO: fix the icon, so it would display wallet -->
    <router-link :to="`/wallet_details/${wallet.id}`"><font-awesome-icon :icon="['fas', 'wallet']" />{{ wallet.name }}</router-link>
  </li>
</template>

<script>

  import { defineComponent } from 'vue'
  
  export default defineComponent({
    name: "WalletComponent",
    props: {
      wallet: {
        type: Object,
        required: true
      },
    },
  })

</script>

<style lang="scss" scoped></style>
