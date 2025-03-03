<template>
  <v-container fluid>
    <BlogLayout>
      <template #main>
        <div class="image-wrapper elevation-10">
          <v-img 
            :src="recipe?.image_path || 'https://i.pinimg.com/736x/d5/d4/bb/d5d4bb7e8a83e3cc20f3383e4ca3e5c7.jpg'" 
            class="background-image rounded-t-xl" 
            cover 
            height="100%"
            style="height: 100%; width: 100%;" />        
        </div>
        <div style="position: relative; z-index: 1; margin-top: -110px; padding: 20px; background-color: rgba(0, 0, 0, 0.5); height: 13.5vh" class="rounded-b-lg">
          <div class="mb-4 text-h6 " style="color: white;">
            {{ recipe?.name || 'No recipe available' }}
          </div>
        </div>
      </template>
    </BlogLayout>
  </v-container>
</template>

<script lang="ts" setup>
import { defineProps } from 'vue';
import BlogLayout from '@/layouts/BlogLayout.vue';

defineProps({
  recipe: {
    type: Object,
    required: true,
  },
});
</script>

<style>
.image-wrapper {
  overflow: hidden;
  border-radius: 12px; /* Ensure the image expansion is contained */
  height: 100%; /* Ensure the wrapper takes full height */
}

.background-image {
  transition: transform 0.3s ease;
  height: 100%; /* Ensure the image takes full height of the wrapper */
}

.background-image:hover {
  transform: scale(1.1);
}
</style>
