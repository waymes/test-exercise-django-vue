import { createApp } from 'vue';
import { createWebHistory, createRouter } from 'vue-router';

import App from './App.vue';

import Apartments from './pages/Apartments.vue';
import ApartmentDetails from './pages/ApartmentDetails.vue';
import LoginView from './pages/Login.vue';
import NotFoundView from './pages/NotFound.vue';

import store from './store';
import './styles/main.css';

const routes = [
  { path: '/', component: Apartments },
  { path: '/apartments/:slug', component: ApartmentDetails },
  { path: '/login', component: LoginView },
  { path: '/:pathMatch(.*)*', component: NotFoundView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

createApp(App).use(router).use(store).mount('#app');
