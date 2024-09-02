<template>
    <div class="login-page">
        <div class="left-login">
            <div class="main-framework">
                <img src="../assets/Logótipo_Politécnico_Leiria_01.png"/>
            </div>
            <div class="main-framework">
                <img src="../assets/cib-vue-js.svg"/>
            </div>
            <div class="main-framework">
                <img src="https://i.imgur.com/yGF4yPg.png"/>
            </div>
        </div>
        <div class="right-login">
            <div class="login-form">
                <div class="Icon-outside">
                    <input type="text" placeholder="Exemplo:jose.jose" v-model="username">
                    <i class="bi bi-person"></i>
                </div>
                <div class="Icon-outside">
                    <input type="password" placeholder="Exemplo:jose" v-model="password">
                    <i class="bi bi-lock"></i>
                </div>
                
              <button @click="getUserCredentials()">Sign In</button>

            </div>
        </div>
    </div>
</template>

  
  <script>
  import axios from 'axios';
  
  export default{
    data() {
      return {
        username:'',
        password:''
      };
    },
    methods: {
        async getUserCredentials() {
            try {
                // grab username and password and send request to Node.js server
                const response = await axios.get('http://localhost:3000/login', {
                    params: {
                    username: this.username,
                    password: this.password
                    }
                });
                if (response.data.length > 0){
                    this.$store.commit('setLogin', {username: this.username, password: this.password})
                    this.$router.push('/dashboard')
                }else{
                    alert("Login Inválido");
                }

            } catch (error) {
                console.error(error);
            }
        },
    }
    
  };
  </script>
  