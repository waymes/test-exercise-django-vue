<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import Table from '@/components/Table.vue';
import { fetchApartments } from '@/api/apartments';

const route = useRoute();
const apartmentList = ref([]);
const count = ref(0);
const loading = ref(true);
const limit = 10;

onMounted(() => {
  handleLoadApartments(route.query);
});

const handleLoadApartments = ({ page, ...params }) => {
  const overridenPage = page || route.query.page;
  const offset = (overridenPage ? parseInt(overridenPage) - 1 : 0) * limit;
  fetchApartments({ ...params, limit, offset })
    .then((data) => {
      apartmentList.value = data.results;
      count.value = data.count;
    })
    .finally(() => {
      loading.value = false;
    });
};

watch(
  () => route.query,
  () => {
    handleLoadApartments(route.query);
  }
);
</script>

<template>
  <div class="py-12">
    <h2 class="mt-12 mb-10 text-2xl/9 font-bold tracking-tight text-gray-900">
      Apartments
    </h2>
    <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
      <Table
        :apartments="apartmentList"
        :limit="limit"
        :count="count"
        :loading="loading"
      ></Table>
    </div>
  </div>
</template>

<style scoped></style>
