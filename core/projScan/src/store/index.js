import { createStore } from 'vuex'


export default createStore({
  state: {
    userInfo: null,

  },
  mutations: {
    setLogin (state, user){
        state.userInfo = user   
    },
    setLogout (state, user){
        state.userInfo = null
    }

  },
  getters: {
    getUser: (state) => {
      return state.userInfo
    },
    getLoginStatus: (state) => {
        return state.isLoggedIn
    }

  }
})

