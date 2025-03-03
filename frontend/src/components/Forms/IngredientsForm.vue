<template>
    <v-container>
        <v-form ref="form" v-model="valid" lazy-validation>
            <v-container class="overflow-y-auto pa-0 mb-3" max-height="26vh">
                <div v-for="(ingredient, index) in ingredients" :key="index" class="d-flex">
                    <v-text-field
                        v-model="ingredient.name"
                        label="Ingredient Name"
                        class="me-4 w-100" 
                        :rules="[v => !!v || 'Ingredient Name is required']"
                        required
                    ></v-text-field>
                    <v-text-field
                        v-model="ingredient.measurements"
                        label="Measurements"
                        class="w-50"  
                        :rules="[v => !!v || 'Measurements are required']"
                        required
                    ></v-text-field>
                </div>
            </v-container>
            <v-btn @click="addIngredient">Add Ingredients</v-btn>
        </v-form>
    </v-container>
</template>

<script lang="ts" setup>
import { ref, watch } from 'vue'

const emit = defineEmits(['passToParent'])
const props = defineProps({
    secondFormComplete: {
        type: Boolean,
        required: true
    }
})
const valid = ref(false);
const ingredients = ref([{ name: '', measurements: '' }]);

const addIngredient = () => {
    const lastIngredient = ingredients.value[ingredients.value.length - 1];
    if (lastIngredient.name !== '' && lastIngredient.measurements !== '') {
        ingredients.value.push({ name: '', measurements: '' }); 
    }
};

watch(() => props.secondFormComplete, (newValue) => {
    if (newValue) {
        console.log('isNext is now true');
        emit('passToParent', ingredients.value)
    } else {
        console.log('isNext is now false');
    }
});

</script>

<style>

</style>