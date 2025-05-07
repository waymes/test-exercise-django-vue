<script setup>
import { useRoute } from 'vue-router';

const props = defineProps({
  limit: String,
  count: Number,
});
const route = useRoute();

const handleCreateLink = (type, newPage) => {
  let page = route.query.page ? parseInt(route.query.page, 10) : 1;
  switch (type) {
    case 'next':
      page += 1;
      break;
    case 'previous':
      page -= 1;
      break;
    case 'current':
      page = newPage;
    default:
      break;
  }
  const tooLarge = page * props.limit > props.count;
  const tooSmall = page <= 0;
  if ((tooLarge || tooSmall) && !newPage) {
    return null;
  }
  const query = new URLSearchParams({ ...route.query, page }).toString();
  return `/?${query}`;
};
</script>

<template>
  <div class="flex my-3">
    <nav
      class="isolate inline-flex -space-x-px rounded-md shadow-xs mx-auto"
      aria-label="Pagination"
    >
      <RouterLink
        :to="handleCreateLink('previous')"
        class="relative inline-flex items-center rounded-l-md px-2 py-2 text-gray-400 ring-1 ring-gray-300 ring-inset hover:bg-gray-50 focus:z-20 focus:outline-offset-0"
      >
        <span class="sr-only">Previous</span>
        <svg
          class="size-5"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          data-slot="icon"
        >
          <path
            fill-rule="evenodd"
            d="M11.78 5.22a.75.75 0 0 1 0 1.06L8.06 10l3.72 3.72a.75.75 0 1 1-1.06 1.06l-4.25-4.25a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0Z"
            clip-rule="evenodd"
          />
        </svg>
      </RouterLink>
      <RouterLink
        v-for="(_, id) in new Array(Math.ceil(props.count / props.limit))"
        :to="handleCreateLink('current', id + 1)"
        :key="id"
        :class="`${
          (route.query.page || '1') === `${id + 1}`
            ? 'bg-indigo-600 text-white'
            : ''
        } relative z-10 inline-flex items-center px-4 py-2 text-sm font-semibold focus:z-20 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600`"
        >{{ id + 1 }}</RouterLink
      >
      <RouterLink
        :to="handleCreateLink('next')"
        class="relative inline-flex items-center rounded-r-md px-2 py-2 text-gray-400 ring-1 ring-gray-300 ring-inset hover:bg-gray-50 focus:z-20 focus:outline-offset-0"
      >
        <span class="sr-only">Next</span>
        <svg
          class="size-5"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          data-slot="icon"
        >
          <path
            fill-rule="evenodd"
            d="M8.22 5.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.75.75 0 0 1-1.06-1.06L11.94 10 8.22 6.28a.75.75 0 0 1 0-1.06Z"
            clip-rule="evenodd"
          />
        </svg>
      </RouterLink>
    </nav>
  </div>
</template>
