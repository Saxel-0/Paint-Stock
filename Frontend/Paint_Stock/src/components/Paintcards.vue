<!-- template for the cards, includes the colour name and stock level, as well as an input field to update the stock level -->
<template>
    <div class="paint-card">
        <h2>{{ paint.colour }}</h2>
        <p>Stock: {{ paint.stock_level }}</p>
        <input type="number" v-model="newStockLevel">
        <p>L</p>
        <button @click="updateStock">Update Stock</button>
    </div>
    
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
    props: { 
        paint: {
            required: true,
            type: Object
        },
    },
    setup(props) {
        console.log(props.paint);
        console.log('PaintCard component created', props);
        const newStockLevel = ref(0);

        const updateStock = async () => {
        try {
            const response = await axios.put(`http://tempUrl/paints/${props.paint.id}/`, {
            stock: props.paint.stock_level
            });
            props.paint.stock_level = newStockLevel.value;
        } catch (error) {
            console.error(error);
        }
        };

        return {
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