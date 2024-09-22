<script></script>

<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar navbar-dark bg-dark">
      <div className="container-fluid">
        <a class="navbar-brand px-3">
          <router-link :to="{ name: 'home' }">
            <img
              class="pwn-logo px-3"
              width="100"
              height="70"
              alt="PWN logo"
              src="/public/pwn-logo.png"
            />
          </router-link>
        </a>
      </div>
    </nav>
  </header>
</template>

<style scoped></style>
