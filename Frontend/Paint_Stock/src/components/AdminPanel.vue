<template>
    <div v-if="isAdmin">
      <button @click="toggleMenu">Admin Panel</button>
      <div v-show="showMenu">
        <ul>
          <li v-for="user in users" :key="user.id">
            {{ user.username }}
            <input type="checkbox" v-model="user.canEdit" :disabled="!isAdmin"> Edit
            <input type="checkbox" v-model="user.isAdmin" :disabled="!isAdmin"> Admin
            <button @click="deleteUser(user.id)">Delete</button>
          </li>
        </ul>
        <button @click="createUser">Create User</button>
      </div>
    </div>
  </template>
  
<script>
  export default {
    name: 'AdminPanel',
    props: {
      isAdmin: {
        type: Boolean,
        default: false
      },
      users: {
        type: Array,
        default: () => []
      }
    },
    data() {
      return {
        showMenu: false
      };
    },
    methods: {
      toggleMenu() {
        this.showMenu = !this.showMenu;
      },
      deleteUser(userId) {
        this.$emit('delete-user', userId);
      },
      createUser() {
        this.$emit('create-user');
      }
    }
  };
</script>
  
<style scoped>
  
</style>