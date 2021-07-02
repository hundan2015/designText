import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    jsonData: "",
  },
  mutations: {
    setJson(state, str) {
      state = str
    }
  },
  actions: {
  },
  modules: {
  }
})
