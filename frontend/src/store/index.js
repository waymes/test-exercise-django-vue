import { createStore } from 'vuex';

// Create a new store instance.
const store = createStore({
  state() {
    return {
      auth: null,
    };
  },
  mutations: {
    LOGIN(state, payload) {
      state.auth = payload;
    },
    LOGOUT(state, payload) {
      state.auth = null;
    },
  },
  actions: {
    login(context, payload) {
      context.commit('LOGIN', payload);
    },
    logout(context) {
      context.commit('LOGIN');
    },
  },
});

export default store;
