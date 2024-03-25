<!-- template for the cards, includes the colour name and stock level, as well as an input field to update the stock level -->
<template>
    <div class="paint-card" :style="{ backgroundColor: paint.colour }" :class="{ 'text-black': paint.colour === 'White' }">
        <div class="paint-card-header">
            <h2>{{ paint.colour }}</h2>
            <p>Stock: {{ paint.stock_level }}L</p>
        </div>
        <div class="paint-card-footer">
            <input type="number" v-model="newStockLevel" :disabled="!canEdit">
            <button @click="updateStock" :disabled="!canEdit">Update Stock</button>
        </div>
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
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 20px;
  margin-right: 150px;
  color: white; 
}

.paint-card-header {
  align-self: flex-start;
}

.paint-card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text-black {
  color: black;
}
</style>