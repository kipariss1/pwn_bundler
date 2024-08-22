<script setup lang="ts">
</script>

<template>
  <div class="container">
    <div class='row py-3'>
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
        <div class="card" style="width: 18rem;">
          <div class="card-header">
            List of connected wallets:
          </div>
          <ul class="list-group list-group-flush">
            <li class="list-group-item">Dummy wallet #1</li>
            <li class="list-group-item">Dummy wallet #2</li>
            <li class="list-group-item">Dummy wallet #3</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
