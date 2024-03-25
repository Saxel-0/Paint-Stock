<template>
    <form @submit.prevent="login">
      <input type="text" v-model="username" placeholder="Username">
      <input type="password" v-model="password" placeholder="Password">
      <button type="submit">Login</button>
    </form>
</template>
  
<script>
  export default {
    name: 'UserLogin',
    props: {
      users: {
        type: Array,
        default: () => []
      }
    },
    data() {
      return {
        username: '',
        password: ''
      };
    },
    methods: {
      login() {
        const user = this.users.find(user => user.username === this.username && user.password === this.password);
        if (user) {
          this.$emit('login', user);
          console.log('login successful');
        
        } else {
          alert('username or password error');
        }
      }
    }
  };
</script>
  
<style scoped>

</style>