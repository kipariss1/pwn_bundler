<template>
  <header class="sticky-header">
    <nav class="navbar navbar-expand-lg navbar navbar-dark bg-dark my-2, my-lg-0, mr-sm-0, my-sm-0">
      <img class="pwn-logo px-3" width="88" height="24" alt="PWN logo" src="/public/pwn-logo.svg">
      <a class="navbar-brand px-3">PWN Bundler</a>
    </nav>
  </header>
</template>

<style scoped>
.sticky-header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000; /* Optional: Ensure the header is above other elements */
  padding: 10px 20px; /* Optional: Add some padding */
}
</style>
