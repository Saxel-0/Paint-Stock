<script>
import { ref } from 'vue';
import PaintCard from './components/Paintcards.vue';
import SwimLanes from './components/SwimLanes.vue';
import QuickView from './components/QuickView.vue';

export default {
  components: {
    PaintCard,
    SwimLanes,
    QuickView
  },
  setup() {
    const paints = ref([
      { id: 1, colour: 'White', stock_level: 10, status: 'Available'},
      { id: 2, colour: 'Grey', stock_level: 10, status: 'Available' },
      { id: 3, colour: 'Black', stock_level: 10, status: 'Available' },
      { id: 4, colour: 'Purple', stock_level: 10, status: 'Available' },
      { id: 5, colour: 'Blue', stock_level: 10, status: 'Available' }
    ]);
    console.log('test', paints.value)
    return {
      paints
    };
  }
};
</script>

<template>
  <div>
    <header>
      <QuickView :paints="paints" />
    </header>

    <main>
      <SwimLanes :paints="paints"/>
    </main>
  </div>
</template>

<style scoped>

</style>
