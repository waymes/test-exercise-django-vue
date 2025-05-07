<script setup>
import Header from './components/Header.vue';
</script>

<template>
  <Header />
  <main class="container mx-auto px-5 sm:px-0">
    <RouterView />
  </main>
</template>
