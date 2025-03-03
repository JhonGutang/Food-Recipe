<template>
  <div>
    <Hero />
    <v-container height="100vh">
      <v-container class="mt-5">
        <div class="text-center text-h3 great-vibes-regular"> Add Recipe for Others to Discover
        </div>
      </v-container>
      <div class="d-flex flex-wrap justify-center">
        <div class="pa-4">
          <CreateBlog @updatedRecipes="handleNewRecipe" />
        </div>
        <div v-for="recipe in recipes" :key="recipe.id" class="pa-2" @click="openModal(recipe)">
          <Blog :recipe="recipe" class="cursor-pointer"  />
        </div>
      </div>
    </v-container>

    <RecipeModal :isOpen="isModalOpen" :recipe="selectedRecipe" @close="handleModal"
      @delete="handleDeleteRecipe" />
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from "vue";
import RecipeModal from "../components/RecipeModal.vue";
import { fetchRecipes } from '../composables/useRecipe.js'
import type { Recipe } from "@/composables/useRecipe";
export interface Recipe {
  id: number;
  name: string;
  description: string;
}

const recipes = ref<Recipe[]>([]);
const isModalOpen = ref(false);
const selectedRecipe = ref<Recipe | null>(null);


const openModal = (recipe: Recipe) => {
  selectedRecipe.value = recipe;
  isModalOpen.value = true;
};

const handleNewRecipe = (data: Recipe) => {
  recipes.value.push(data)
}

const handleModal = (value: boolean) => {
  isModalOpen.value = value
}

const handleDeleteRecipe = (recipeId: number) => {
  recipes.value = recipes.value.filter(recipe => recipe.id !== recipeId);
}

onMounted(async () => {
  const data = await fetchRecipes();
  recipes.value = data
});
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Roboto+Mono:ital,wght@0,100..700;1,100..700&display=swap');

.great-vibes-regular {
    font-family: "Great Vibes", serif;
    font-weight: 400;
    font-style: normal;
  }
</style>