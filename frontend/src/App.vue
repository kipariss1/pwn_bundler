<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
// @ts-ignore
import HeaderComponent from '@/components/HeaderComponent.vue';
</script>

<template>
  <div>
    <HeaderComponent />
    <RouterView />
  </div>
</template>

<style scoped>


</style>
