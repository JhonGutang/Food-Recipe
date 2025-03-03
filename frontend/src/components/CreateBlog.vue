<template>
    <BlogLayout>
        <template #main>
            <div style="height: 100%;">
                <div class="d-flex justify-center align-center cursor-pointer rounded-xl" style="height: 100%; border: 1px solid black"
                    @click="openModal">
                    <Plus :size="40" />
                </div>
                <v-dialog v-model="localIsOpen" max-width="60vw">
                    <template #default>
                        <v-card>
                            <v-card-title>
                                <span class="text-h5">Create a New Recipe</span>
                            </v-card-title>
                            <v-card-text class="d-flex align-center">
                                <v-container width="45%" height="30vh" @click="triggerImageUpload" 
                                    class="border pa-0 rounded-xl d-flex justify-center align-center cursor-pointer">
                                    <input type="file" @change="handleImageUpload" accept="image/*" style="display: none;" ref="imageInput" />
                                    <div class="d-flex justify-center align-center" style="height: 100%; width: 100%;">
                                        <div v-if="recipeImage" class="d-flex justify-center align-center position-relative" style="height: 100%; width: 100%;">
                                            <v-img :src="recipeImage" class="rounded-xl" height="100%" cover></v-img>
                                            <v-btn class="position-absolute top-0 right-0" variant="text" @click="recipeImage = null" icon>
                                                <X :size="24" />
                                            </v-btn>
                                        </div>
                                        <div v-else>
                                            <Plus :size="40" />
                                        </div>
                                    </div>
                                </v-container>
                                <v-carousel :show-arrows="false" hide-delimiters height="34vh" v-model="currentPage">
                                    <v-carousel-item>
                                        <FirstForm :firstFormComplete="firstFormComplete" @pass-to-parent="handleFirstForm" />
                                    </v-carousel-item>
                                    <v-carousel-item>
                                        <IngredientsForm :secondFormComplete="secondFormComplete" @pass-to-parent="handleSecondForm"/>
                                    </v-carousel-item>
                                </v-carousel>
                            </v-card-text>
                            <v-card-actions>
                                <v-btn v-if="currentPage === 0" color="primary" @click="nextPage">Next</v-btn>
                                <v-btn v-else @click="submitRecipe">Submit</v-btn>
                                <v-btn @click="closeModal">Cancel</v-btn>
                            </v-card-actions>
                        </v-card>
                    </template>
                </v-dialog>
            </div>
            <v-snackbar v-model="snackbar" :timeout="3000" color="success">
                {{ snackbarMessage }}
                <template #action="{ attrs }">
                    <v-btn text v-bind="attrs" @click="snackbar = false">Close</v-btn>
                </template>
            </v-snackbar>
        </template>
    </BlogLayout>
</template>

<script lang="ts" setup>
import BlogLayout from '@/layouts/BlogLayout.vue'
import FirstForm from './Forms/FirstForm.vue';
import IngredientsForm from './Forms/IngredientsForm.vue';
import { Plus, X } from 'lucide-vue-next';
import { ref, nextTick } from 'vue';
import { createNewRecipe } from '@/composables/useRecipe';
import type { Recipe } from '@/composables/useRecipe';

const emit = defineEmits(['updatedRecipes'])
const localIsOpen = ref(false);
const currentPage = ref(0);
const firstFormComplete = ref(false)
const secondFormComplete = ref(false)
const recipeForm = ref<Recipe>({
    image: null,
    name: '',
    description: '',
    ingredients: [],
})
const recipeImage = ref()

const snackbar = ref(false);
const snackbarMessage = ref('');
const imageInput = ref<HTMLInputElement | null>(null);

type Ingredient = {
    name: string,
    measurements: string,
}

const openModal = () => {
    localIsOpen.value = true;
};

const closeModal = () => {
    localIsOpen.value = false;
    currentPage.value = 0;
    firstFormComplete.value = false;
    secondFormComplete.value = false; 
    recipeForm.value = {
        image: null, 
        name: '', 
        description: '', 
        ingredients: [] 
    };
    recipeImage.value = null
};

const triggerImageUpload = () => {
    imageInput.value?.click();
};

const handleImageUpload = (event: Event) => {
    const target = event.target as HTMLInputElement;
    if (target.files && target.files.length > 0) {
        const file = target.files[0];
        const localUrl = URL.createObjectURL(file); // Get the local URL of the image
        recipeImage.value = localUrl
        recipeForm.value.image = file
    }
};

const nextPage = () => {
    currentPage.value++;
    firstFormComplete.value = true
};

const handleFirstForm = (data: Recipe) => {
    recipeForm.value.name = data.name
    recipeForm.value.description = data.description
}

const handleSecondForm = (data: Ingredient[]) => {
    recipeForm.value.ingredients = data
}

const submitRecipe = async () => {
    secondFormComplete.value = true; 
    await nextTick(); 

    // Remove empty ingredients
    recipeForm.value.ingredients = recipeForm.value.ingredients.filter(ingredient => ingredient.name && ingredient.measurements);

    if (recipeForm.value.ingredients.length > 0) {
        const data = await createNewRecipe(recipeForm.value);
        snackbarMessage.value = 'Recipe submitted successfully!';
        snackbar.value = true;
        emit('updatedRecipes', data);
    } else {
        snackbarMessage.value = 'Failed to submit recipe. Please check your ingredients.';
        snackbar.value = true;
    }
    setTimeout(() => {
        closeModal();
    }, 1000);
};

</script>

<style>
.d-flex {
    height: 100%;
}
</style>