<script setup>
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

const search = ref(route.query.search || '');
const availability = ref(route.query.available || '');
const priceMin = ref(route.query.price_min || '');
const priceMax = ref(route.query.price_max || '');
const rooms = ref(route.query.rooms || '');

const handleSubmit = (e) => {
  e.preventDefault();
  const newQuery = {
    ...route.query,
    search: search.value,
    available: availability.value,
    price_min: priceMin.value,
    price_max: priceMax.value,
    rooms: rooms.value,
    page: 1,
  };
  Object.keys(newQuery).forEach(
    (key) => newQuery[key] === '' && delete newQuery[key]
  );
  const queryString = new URLSearchParams(newQuery).toString();
  router.push(`/?${queryString}`);
};
</script>

<template>
  <form class="my-2 flex sm:flex-row flex-col" @submit="handleSubmit">
    <div class="block relative flex-grow mb-5 sm:mb-0">
      <span class="h-full absolute inset-y-0 left-0 flex items-center pl-2">
        <svg viewBox="0 0 24 24" class="h-4 w-4 fill-current text-gray-500">
          <path
            d="M10 4a6 6 0 100 12 6 6 0 000-12zm-8 6a8 8 0 1114.32 4.906l5.387 5.387a1 1 0 01-1.414 1.414l-5.387-5.387A8 8 0 012 10z"
          ></path>
        </svg>
      </span>
      <input
        v-model="search"
        placeholder="Search"
        class="appearance-none sm:rounded-l border border-gray-400 border-b block pl-8 pr-6 py-2 w-full bg-white text-sm placeholder-gray-400 text-gray-700 focus:bg-white focus:placeholder-gray-600 focus:text-gray-700 focus:outline-none"
      />
    </div>
    <div class="flex flex-row mb-5 sm:mb-0">
      <div class="relative w-full">
        <select
          v-model="availability"
          class="appearance-none h-full border sm:rounded-l-none sm:border-l-0 border-r border-b block appearance-none w-full bg-white border-gray-400 text-gray-700 py-2 px-4 pr-8 leading-tight focus:outline-none focus:border-l focus:border-r focus:bg-white focus:border-gray-500"
        >
          <option value="">Not selected</option>
          <option value="true">Available</option>
          <option value="false">Not available</option>
        </select>
        <div
          class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700"
        >
          <svg
            class="fill-current h-4 w-4"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
          >
            <path
              d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
            />
          </svg>
        </div>
      </div>
    </div>
    <div class="block relative mb-5 sm:mb-0">
      <input
        v-model="priceMin"
        placeholder="Price min"
        class="appearance-none sm:rounded-r-none border sm:border-l-0 border-gray-400 border-b block px-6 py-2 w-full bg-white text-sm placeholder-gray-400 text-gray-700 focus:bg-white focus:placeholder-gray-600 focus:text-gray-700 focus:outline-none"
      />
    </div>
    <div class="block relative mb-5 sm:mb-0">
      <input
        v-model="priceMax"
        placeholder="Price max"
        class="appearance-none sm:rounded-r-none border sm:border-l-0 border-gray-400 border-b block px-6 py-2 w-full bg-white text-sm placeholder-gray-400 text-gray-700 focus:bg-white focus:placeholder-gray-600 focus:text-gray-700 focus:outline-none"
      />
    </div>
    <div class="block relative mb-5 sm:mb-0">
      <input
        v-model="rooms"
        placeholder="Number of rooms"
        type="number"
        class="appearance-none sm:rounded-l-none border sm:border-l-0 border-gray-400 border-b block px-6 py-2 w-full bg-white text-sm placeholder-gray-400 text-gray-700 focus:bg-white focus:placeholder-gray-600 focus:text-gray-700 focus:outline-none"
      />
    </div>
    <div class="block relative flex-grow mb-5 sm:mb-0">
      <button
        type="submit"
        class="flex w-full h-full justify-center sm:rounded-l-none rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
      >
        Search
      </button>
    </div>
  </form>
</template>
