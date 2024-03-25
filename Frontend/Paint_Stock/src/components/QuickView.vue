<template>
    <div class="quick-view-text">
      <button @click="toggleList">Quick View</button>
      <div v-show="showList">
        <ul>
          <li v-for="paint in paints" :key="paint.id">
            {{ paint.colour }}: {{ paint.stock_level }}L
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'QuickView',
    props: {
      paints: {
        type: Array,
        required: true
      }
    },
    data() {
      return {
        showList: false
      };
    },
    methods: {
      toggleList() {
        this.showList = !this.showList;
      }
    }
  };
  </script>
  
  <style scoped>
    .quick-view-text {
        font-weight: bold; 
        font-size: 20px; 
    }
  </style>