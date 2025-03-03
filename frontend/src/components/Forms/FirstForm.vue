<template>
    <v-container>
        <v-form ref="form" v-model="valid">
          <v-text-field
            v-model="name"
            label="Recipe Name"
            :onchange="handleText()"
            :rules="[v => !!v || 'Name is required']"
          />
          <v-textarea
            v-model="description"
            label="Description"
            :rules="[v => !!v || 'Description is required']"
          />
        </v-form>

    </v-container>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const props = defineProps({
  firstFormComplete: {
    type: Boolean,
    required: true
  }
})
const emit = defineEmits(['passToParent'])
const valid = ref(false);
const name = ref('');
const description = ref('');

const handleText = () => {

}

import { watch } from 'vue';

watch(() => props.firstFormComplete, (newValue) => {
    if (newValue) {
        console.log('isNext is now true');
        emit('passToParent', {
          name: name.value,
          description: description.value,
        } )
    } else {
        console.log('isNext is now false');
    }
});

</script>

<style>

</style>