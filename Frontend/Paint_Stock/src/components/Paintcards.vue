<!-- template for the cards, includes the colour name and stock level, as well as an input field to update the stock level -->
<template>
    <div class="paint-card">
      <h2>{{ paint.colour }}</h2>
      <p>Stock: {{ paint.stock_level }}</p>
      <input type="number" v-model="newStockLevel" :disabled="!canEdit">
      <p>L</p>
      <button @click="updateStock" :disabled="!canEdit">Update Stock</button>
    </div>
  </template>
  
<script>
import { ref, reactive, toRefs } from 'vue';
import axios from 'axios';
  
export default {
    props: {
        paint: {
            required: true,
            type: Object
        },
        canEdit: {
            type: Boolean,
            default: false
        }
    },
    setup(props) {
        const localPaint = reactive({ ...props.paint });
        const newStockLevel = ref(0);
        const updateStock = async () => {
            if (props.paint) {
                try {
                    const response = await axios.put(`http://tempUrl/paints/${props.paint.id}/`, {
                        stock: newStockLevel.value
                    });
                    if (response.status === 200) {
                        localPaint.stock_level = newStockLevel.value;
                    }
                }   catch (error) {
                    console.error(error);
                }
            }
        };

        return {
        ...toRefs(localPaint),
        newStockLevel,
        updateStock
        };
    }
}
</script>

<style scoped>  /* CSS styling for the cards */
.paint-card {
    display: block;
    visibility: visible;
}
</style>