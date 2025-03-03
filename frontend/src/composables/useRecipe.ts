import axios from 'axios';

export type Ingredient = {
    id?: number;
    name: string;
    measurements: string;
}

export type Recipe = {
    image: File;
    name: string;
    description: string;
    ingredients: Ingredient[]
}

export const fetchRecipes = async () => {
    const response = await axios.get('recipes/');
    return response.data;
}

export const fetchIngredients = async (recipeId: number): Promise<Ingredient[]> => {
    const response = await axios.get(`recipes/${recipeId}/ingredients/`);
    return response.data;
}

export const createNewRecipe = async (recipe: Recipe): Promise<void> => {
    const base64Image = await toBase64(recipe.image); // Convert image file to Base64

    const data = {
        image_path: base64Image, // Send Base64 string
        name: recipe.name,
        description: recipe.description,
        ingredients: recipe.ingredients,
    };

    const response = await axios.post('recipes/', data, {
        headers: { 'Content-Type': 'application/json' }
    });

    return response.data;
}

export const updateRecipe = async (recipeId: number, updatedRecipe: Omit<Recipe, 'ingredients'>): Promise<void> => {
    const data = {
        name: updatedRecipe.name,
        description: updatedRecipe.description,
    };

    const response = await axios.put(`recipes/${recipeId}/update/`, data, {
        headers: { 'Content-Type': 'application/json' }
    });

    return response.data;
};

// Helper function to convert file to Base64
const toBase64 = (file: File): Promise<string> => {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result as string);
        reader.onerror = (error) => reject(error);
    });
};

export const deleteRecipe = async(recipeId: number) => {
    console.log(recipeId);
    const response = await axios.delete(`recipes/${recipeId}/`)
}
