<script>
import { ref, reactive } from 'vue';
import PaintCard from './components/Paintcards.vue';
import SwimLanes from './components/SwimLanes.vue';
import QuickView from './components/QuickView.vue';
import AdminPanel from './components/AdminPanel.vue';
import UserLogin from './components/UserLogin.vue';

export default {
  components: {
    PaintCard,
    SwimLanes,
    QuickView,
    AdminPanel,
    UserLogin
  },
  setup() {
    const paints = ref([
      { id: 1, colour: 'White', stock_level: 10, status: 'Available'},
      { id: 2, colour: 'Grey', stock_level: 10, status: 'Available' },
      { id: 3, colour: 'Black', stock_level: 10, status: 'Available' },
      { id: 4, colour: 'Purple', stock_level: 10, status: 'Available' },
      { id: 5, colour: 'Blue', stock_level: 10, status: 'Available' }
    ]);
    const users = ref([
      { id: 1, username: 'CompanyPainter', password: '123', canEdit: true, isAdmin: false },
      { id: 2, username: 'John', password: '123', canEdit: true, isAdmin: false },
      { id: 3, username: 'Jane', password: '123', canEdit: true, isAdmin: false },
      { id: 4, username: 'Adam', password: '123', canEdit: true, isAdmin: true }
    ]);

    const permissions = reactive({
      canEdit: false,
      isAdmin: false
    });

    const currentUser = ref(null);

    const login = (user) => {
      currentUser.value = user;
      permissions.view_paints = user.canView;
      permissions.edit_paints = user.canEdit;
      permissions.edit_users = user.isAdmin;
    };

    return {
      paints,
      users,
      currentUser,
      login,
      permissions
    };
  }
};
</script>

<template>
  <div>
    <header>
      <QuickView :paints="paints" />
      <AdminPanel v-if="permissions.edit_users" :users="users" :isAdmin="permissions.edit_users" />
      <UserLogin :users="users" @login="login" />
    </header>

    <main>
      <SwimLanes v-if="currentUser" :key="currentUser.id" :paints="paints" :canEdit="permissions.edit_paints" />
    </main>
  </div>
</template>

<style scoped>

</style>
