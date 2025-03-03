<template>
    <v-container
      fluid
      height="100vh"
      class="pa-0 custom-background d-flex flex-column align-center justify-center"
    >
      <!-- Title fades in first -->
      <div class="text-h1 mb-2 great-vibes-regular fade fade-delay-1">
        Food Blog
      </div>
  
      <!-- Subtitle fades in second -->
      <div class="text-h5 fade fade-delay-2 mb-4">
        A Journey Through Flavors
      </div>
  
      <!-- Authors fade in last -->
      <div class="text-subtitle-2 fade fade-delay-3">
        Clifford Castanares & Keeshia Booc
      </div>
    </v-container>
  </template>
  
  <script lang="ts" setup>
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Roboto+Mono:ital,wght@0,100..700;1,100..700&display=swap');
  
  .great-vibes-regular {
    font-family: "Great Vibes", serif;
    font-weight: 400;
    font-style: normal;
  }
  
  .custom-background {
    background: url('/background.jpg') no-repeat center center;
    background-size: cover;
    height: 100vh;
    width: 100vw;
  }
  
  /* Initially hide elements */
  .fade {
    opacity: 0;
  }
  
  /* Fade-in animation */
  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(10px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  /* Apply fade-in animation with delays */
  .fade-delay-1 {
    animation: fadeIn 1.5s ease-out forwards;
    animation-delay: 0s;
  }
  
  .fade-delay-2 {
    animation: fadeIn 1.5s ease-out forwards;
    animation-delay: 0.8s;
  }
  
  .fade-delay-3 {
    animation: fadeIn 1.5s ease-out forwards;
    animation-delay: 1.6s;
  }
  </style>
  