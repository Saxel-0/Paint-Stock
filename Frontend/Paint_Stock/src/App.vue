<script>
import { ref } from 'vue';
import PaintCard from './components/Paintcards.vue';

export default {
  components: {
    PaintCard
  },
  setup() {
    const paints = ref([
      { id: 1, colour: 'white', stock_level: 10},
      { id: 2, colour: 'grey', stock_level: 10 },
      { id: 3, colour: 'black', stock_level: 10 },
      { id: 4, colour: 'purple', stock_level: 10 },
      { id: 5, colour: 'blue', stock_level: 10 }
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

    </header>

    <main>
      <PaintCard v-for="paint in paints" :key="paint.id" :paint="paint"/>
    </main>
  </div>
</template>

<style scoped>

</style>
