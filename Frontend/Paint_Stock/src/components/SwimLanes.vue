<template>
    <div class="swim-lanes">
      <section
        v-for="status in statuses"
        :key="status"
        @dragover.prevent
        @drop="canEdit ? drop($event, status) : null"
      >
        <h2 class="swim-lane-title">{{ status }}</h2>
        <PaintCard
          v-for="paint in paintsByStatus[status]"
          :key="paint.id"
          :paint="paint"
          :draggable="canEdit"
          :canEdit="canEdit"
          @dragstart="canEdit ? dragStart($event, paint) : null"
          @dragend="canEdit ? dragEnd : null"
        />
      </section>
    </div>
  </template>
  
  <script>
  import { computed, ref } from 'vue';
  import PaintCard from './Paintcards.vue';
  
  export default {
    name: 'SwimLanes',
    components: {
      PaintCard
    },
    props: {
      paints: {
        type: Array,
        required: true
      },
      canEdit: {
        type: Boolean,
        default: false
      }
    },
    setup(props) {
      const statuses = ['Available', 'Running Low', 'Out of Stock'];
      const draggedPaint = ref(null);
  
      const paintsByStatus = computed(() => {
        const statusMap = {};
        statuses.forEach(status => {
          statusMap[status] = props.paints.filter(paint => paint.status === status);
        });
        return statusMap;
      });
  
      const dragStart = (event, paint) => {
        draggedPaint.value = paint;
      };
  
      const dragEnd = () => {
        draggedPaint.value = null;
      };
  
      const drop = (event, status) => {
        if (draggedPaint.value) {
          draggedPaint.value.status = status;
        }
      };
  
      return {
        statuses,
        paintsByStatus,
        dragStart,
        dragEnd,
        drop
      };
    }
  };
  </script>
  
<style scoped>
    .swim-lanes > * {
        height: 33.33vh; 
        margin-bottom: 1vh; 
    }
    
    .swim-lanes {
        display: flex;
        flex-direction: row;
        justify-content: left; 
    }

    @media (max-width: 768px) {
        .swim-lanes {
            flex-direction: column-reverse;
        }
    }
    .swim-lane-title {
        margin-right: 150px;
        margin-left: 0px;
    }
</style>