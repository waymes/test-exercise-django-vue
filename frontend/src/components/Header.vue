<script setup>
import { ref } from 'vue';
import store from '@/store';

const menuOpen = ref(false);

const handleLogout = () => {
  store.dispatch('logout');
  localStorage.removeItem('auth');
};
</script>

<template>
  <header class="container mx-auto">
    <nav class="px-5 sm:px-0">
      <div class="mx-auto max-w-7xl">
        <div class="flex h-16 items-center justify-between">
          <div class="flex items-center flex-grow">
            <div class="shrink-0">
              <RouterLink to="/"
                ><img
                  class="size-8"
                  src="https://tailwindcss.com/plus-assets/img/logos/mark.svg?color=indigo&shade=500"
                  alt="Your Company"
              /></RouterLink>
            </div>
            <div class="hidden md:block ms-auto">
              <div class="ml-10 flex items-baseline space-x-4">
                <RouterLink
                  class="rounded-md px-3 py-2 text-sm font-medium"
                  to="/"
                  >Apartments</RouterLink
                >
                <RouterLink
                  v-if="!store.state.auth"
                  class="rounded-md bg-indigo-600 text-white px-3 py-2 text-sm font-medium"
                  to="/login"
                  >Login</RouterLink
                >
                <RouterLink
                  v-if="store.state.auth"
                  class="rounded-md bg-indigo-600 text-white px-3 py-2 text-sm font-medium"
                  to="/login"
                  @click="handleLogout()"
                  >Logout</RouterLink
                >
              </div>
            </div>
          </div>
          <div class="-mr-2 flex md:hidden">
            <!-- Mobile menu button -->
            <button
              type="button"
              class="relative inline-flex items-center justify-center rounded-md bg-indigo-600 p-2 text-white focus:ring-2 focus:ring-white focus:ring-offset-2"
              aria-controls="mobile-menu"
              aria-expanded="false"
              @click="menuOpen = !menuOpen"
            >
              <span class="absolute -inset-0.5"></span>
              <span class="sr-only">Open main menu</span>
              <!-- Menu open: "hidden", Menu closed: "block" -->
              <svg
                class="block size-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                aria-hidden="true"
                data-slot="icon"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
                />
              </svg>
              <!-- Menu open: "block", Menu closed: "hidden" -->
              <svg
                class="hidden size-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                aria-hidden="true"
                data-slot="icon"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M6 18 18 6M6 6l12 12"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>
      <div v-if="menuOpen" class="md:hidden" id="mobile-menu">
        <div class="space-y-1 px-2 pt-2 pb-3 sm:px-3">
          <RouterLink
            class="block px-3 py-2 text-base font-medium border-b-1"
            to="/"
            >Apartments</RouterLink
          >
          <RouterLink
            v-if="!store.state.auth"
            class="block px-3 py-2 text-base font-medium border-b-1"
            to="/login"
            >Login</RouterLink
          >
          <RouterLink
            v-if="store.state.auth"
            class="block px-3 py-2 text-base font-medium border-b-1"
            to="/login"
            @click="handleLogout()"
            >Logout</RouterLink
          >
        </div>
      </div>
    </nav>
  </header>
</template>
