<script setup lang="ts">
import { NLayout, NLayoutFooter } from "naive-ui";
</script>

<template>
  <n-layout style="min-height: 100vh">
    <div
      flex="~ col"
      justify="center"
      align="items-center"
      min-h="[100vh]"
      p="y-12"
    >
      <router-view pb="24" max-w="4/5 lg:800px" />
      <n-layout-footer
        bordered
        position="absolute"
        flex="~"
        justify="center"
        pb="4"
      >
        <Footer />
      </n-layout-footer>
    </div>
  </n-layout>
</template>
