<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import NotFound from './NotFound.vue';
import Loader from '@/components/Loader.vue';
import { fetchApartmentDetails } from '@/api/apartments';
import { formatDate } from '@/utils/date';

const apartmentDetails = ref(null);
const loading = ref(true);
const route = useRoute();

onMounted(() => {
  fetchApartmentDetails(route.params.slug)
    .then((data) => {
      apartmentDetails.value = data;
    })
    .finally(() => {
      loading.value = false;
    });
});
</script>

<template>
  <Loader v-if="loading" />
  <div v-else-if="!apartmentDetails">
    <NotFound />
  </div>
  <div v-if="!!apartmentDetails" class="py-12">
    <h2 class="mt-12 mb-10 text-2xl/9 font-bold tracking-tight text-gray-900">
      Apartment Details
    </h2>
    <div>
      <div class="mt-6 border-t border-gray-100">
        <dl class="divide-y divide-gray-100">
          <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
            <dt class="text-sm/6 font-medium text-gray-900">Name</dt>
            <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
              {{ apartmentDetails.name }}
            </dd>
          </div>
          <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
            <dt class="text-sm/6 font-medium text-gray-900">Description</dt>
            <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
              {{ apartmentDetails.description }}
            </dd>
          </div>
          <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
            <dt class="text-sm/6 font-medium text-gray-900">Price</dt>
            <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
              {{ apartmentDetails.price }}$
            </dd>
          </div>
          <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
            <dt class="text-sm/6 font-medium text-gray-900">Number of rooms</dt>
            <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
              {{ apartmentDetails.number_of_rooms }}
            </dd>
          </div>
          <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
            <dt class="text-sm/6 font-medium text-gray-900">Square</dt>
            <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
              {{ apartmentDetails.square }}
            </dd>
          </div>
          <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
            <dt class="text-sm/6 font-medium text-gray-900">Availability</dt>
            <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
              {{
                apartmentDetails.availability ? 'Available' : 'Not available'
              }}
            </dd>
          </div>
          <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
            <dt class="text-sm/6 font-medium text-gray-900">Created at</dt>
            <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
              {{ formatDate(apartmentDetails.created_at) }}
            </dd>
          </div>
          <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
            <dt class="text-sm/6 font-medium text-gray-900">Updated at</dt>
            <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
              {{ formatDate(apartmentDetails.updated_at) }}
            </dd>
          </div>
        </dl>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
