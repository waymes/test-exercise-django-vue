<script setup>
import TableFilters from './TableFilters.vue';
import TablePagination from './TablePagination.vue';
import Loader from './Loader.vue';

const props = defineProps({
  apartments: Array,
  limit: String,
  count: Number,
  loading: Boolean,
});
</script>

<template>
  <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
    <TableFilters></TableFilters>
    <Loader v-if="loading" />
    <p v-else-if="!loading && apartments.length === 0" class="my-5 mx-3">
      Couldn't find anything at the moment
    </p>
    <table
      v-if="apartments.length > 0"
      class="w-full text-sm text-left rtl:text-right text-gray-700"
    >
      <thead class="text-xs text-gray-700 uppercase">
        <tr>
          <th scope="col" class="px-6 py-3">Name</th>
          <th scope="col" class="px-6 py-3">Price $</th>
          <th scope="col" class="px-6 py-3">Rooms</th>
          <th scope="col" class="px-6 py-3">Availability</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in apartments"
          :class="`border-b dark:border-gray-700 border-gray-200 ${
            item.availability ? '' : 'blur-[1px] bg-gray-200'
          }`"
          :key="item.slug"
        >
          <th
            scope="row"
            class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap"
          >
            <RouterLink :to="`/apartments/${item.slug}`">{{
              item.name
            }}</RouterLink>
          </th>
          <td class="px-6 py-4">{{ item.price }}</td>
          <td class="px-6 py-4">{{ item.number_of_rooms }}</td>
          <td class="px-6 py-4">
            {{ item.availability ? 'Available' : 'Not available' }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <TablePagination :count="count" :limit="limit"></TablePagination>
</template>
