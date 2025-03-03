<template>
  <v-container class="pa-0">
    <div class="text-h5 mb-2">Ingredients</div>
    <v-container height="35vh" class="overflow-y-auto">
        <ul v-for="ingredient in ingredients" :key="ingredient?.id">
            <li class="mb-3">{{ingredient.name}} - {{ingredient.measurements}}</li>
        </ul>
    </v-container>
  </v-container>
</template>

<script lang="ts" setup>
import { fetchIngredients } from '@/composables/useRecipe';
import type { Ingredient } from '@/composables/useRecipe';
import { onMounted, ref } from 'vue';
const props = defineProps({
    id: {
        type: Number,
        required: true
    }
})



const ingredients = ref<Ingredient[]>([]);


onMounted(async () => {
    const data = await fetchIngredients(props.id);
    ingredients.value = data;
})

</script>

<style>

</style>