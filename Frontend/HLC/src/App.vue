<template>
  <!-- <NavBar />
  <RouterView />
  <Footer /> -->
  <ProfileView />
</template>

<script setup>
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'
import LoginView from './views/LoginView.vue';
import ProfileView from './views/ProfileView.vue';
import { RouterView } from 'vue-router';
</script>

<style scoped>
</style>
