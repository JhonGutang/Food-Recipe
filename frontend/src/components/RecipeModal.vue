<template>
    <div>
        <v-dialog v-model="localIsOpen" max-width="70vw" height="65vh">
            <template #default>
                <v-card>
                    <v-card-text>
                        <div class="d-flex">
                            <v-container class="d-flex align-center justify-center" width="40%" style="height: 100%;">
                                <v-img 
                                :src="recipe?.image_path"
                                class="rounded-lg"
                                contain
                                style="transition: transform 0.3s ease-in-out;"
                                @mouseover="hovered = true"
                                @mouseleave="hovered = false"
                                :style="{ transform: hovered ? 'scale(1.1)' : 'scale(1)' }"
                            />
                            </v-container>
                            <v-container class="d-flex flex-column justify-center pt-5" width="60%">
                                <div class="mb-4 d-flex justify-space-between h-auto">
                                    <div class="d-flex align-center">
                                        <v-btn-toggle v-model="option" mandatory class="me-2">
                                            <v-btn value="food">Food</v-btn>
                                            <v-btn value="recipe">Recipe</v-btn>
                                        </v-btn-toggle>
                                        <div v-if="option === 'food'">
                                            <v-btn v-if="!editMode" @click="editMode = true" variant="text">
                                                <Pencil :size="16"/>
                                            </v-btn>
                                            <v-btn 
                                                v-if="editMode" 
                                                @click="handleUpdateRecipe"
                                                :disabled="!isModified"
                                                class="me-3"
                                                variant="text"
                                            >
                                                <Save :size="16"/>
                                            </v-btn>
                                            <v-btn v-if="editMode" @click="resetFields" color="error" variant="flat">
                                                <X :size="16"/>
                                            </v-btn>
                                        </div>
                                    </div>
                                    <div>
                                        <v-btn @click="closeModal" variant="text">
                                            <X />
                                        </v-btn>
                                    </div>
                                </div>

                                <div class="h-100" v-if="option === 'food'">
                                    <div class="text-h5 mb-5 text-capitalize" v-if="!editMode">
                                        {{ recipe?.name }}
                                    </div>
                                    <v-text-field v-model="recipeName" v-if="editMode" label="Recipe Name" />
                                    <v-container height="70%" class="mb-3 pa-0">
                                        <div v-if="!editMode">{{ recipe?.description }}</div>
                                        <v-textarea v-model="recipeDescription" v-if="editMode" label="Recipe Description" />
                                    </v-container>
                                </div>

                                <div class="h-100" v-if="option === 'recipe'">
                                    <Recipe :id="recipe?.id" />
                                </div>
                            </v-container>
                            <div class="position-absolute right-0 bottom-0 pa-8 text-red-lighten-2 cursor-pointer" @click="confirmDelete">
                                Want to delete recipe?
                            </div>
                        </div>
                    </v-card-text>
                </v-card>
            </template>
        </v-dialog>

        <v-dialog v-model="deleteConfirmation" max-width="400">
            <template #default>
                <v-card class="pa-4">
                    <v-card-title class="text-h5">Confirm Deletion</v-card-title>
                    <v-card-text>Are you sure you want to delete this recipe?</v-card-text>
                    <v-card-actions>
                        <v-btn @click="handleDeleteRecipe" variant="flat" color="error">Yes, delete</v-btn>
                        <v-btn @click="deleteConfirmation = false">Cancel</v-btn>
                    </v-card-actions>
                </v-card>
            </template>
        </v-dialog>

        <v-snackbar v-model="snackbar" :timeout="3000" color="success" location="top">
            {{ snackbarMessage }}
            <template #action="{ attrs }">
                <v-btn text v-bind="attrs" @click="snackbar = false">Close</v-btn>
            </template>
        </v-snackbar>
    </div>
</template>

<script lang="ts" setup>
import { ref, defineProps, defineEmits, watch, computed } from "vue";
import { X, Pencil, Save } from "lucide-vue-next";
import Recipe from "./Recipe.vue";
import { deleteRecipe, updateRecipe } from "@/composables/useRecipe";

const props = defineProps<{
    isOpen: boolean;
    recipe: { id: number; name: string; description: string; image?: File | null } | null;
}>();

const hovered = ref(false)
const option = ref("food");
const deleteConfirmation = ref(false);
const snackbar = ref(false);
const snackbarMessage = ref("");
const editMode = ref(false);
const recipeName = ref(props.recipe?.name || "");
const recipeDescription = ref(props.recipe?.description || "");
const emit = defineEmits<{
    (e: "close"): void;
    (e: "delete", id: number): void;
}>();

const localIsOpen = ref(props.isOpen);

watch(
    () => props.isOpen,
    (newValue) => {
        localIsOpen.value = newValue;
    }
);

watch(
    () => props.recipe,
    (newRecipe) => {
        if (newRecipe) {
            recipeName.value = newRecipe.name;
            recipeDescription.value = newRecipe.description;
        }
    },
    { deep: true, immediate: true }
);

// Check if fields were modified
const isModified = computed(() => {
    return recipeName.value !== props.recipe?.name || recipeDescription.value !== props.recipe?.description;
});

const closeModal = () => {
    localIsOpen.value = false;
    option.value = "food";
    editMode.value = false;
    emit("close", false);
};

const confirmDelete = () => {
    deleteConfirmation.value = true;
};

const handleDeleteRecipe = async () => {
    if (props.recipe) {
        emit("delete", props.recipe.id);
        await deleteRecipe(props.recipe.id);
        snackbarMessage.value = "Recipe deleted successfully!";
        snackbar.value = true;
    }
    deleteConfirmation.value = false;
    setTimeout(() => {
        closeModal();
    }, 1000);
};

const handleUpdateRecipe = async () => {
    if (props.recipe && isModified.value) {
        const updatedRecipe = {
            name: recipeName.value,
            description: recipeDescription.value,
        };
        await updateRecipe(props.recipe.id, updatedRecipe);
        props.recipe.name = recipeName.value;
        props.recipe.description = recipeDescription.value;
        snackbarMessage.value = "Recipe updated successfully!";
        snackbar.value = true;
        editMode.value = false;
    }
};

const resetFields = () => {
    recipeName.value = props.recipe?.name || "";
    recipeDescription.value = props.recipe?.description || "";
    editMode.value = false;
};
</script>
