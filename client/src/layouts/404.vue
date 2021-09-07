<script setup lang="ts">
import { NLayout, NResult, NButton } from "naive-ui";

const router = useRouter();
</script>

<template>
  <n-layout
    style="
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
    "
  >
    <n-result
      status="404"
      title="404 Not Found"
      description="Try going to another path."
    >
      <template #footer>
        <n-button @click="router.back()">Go back</n-button>
      </template>
    </n-result>
  </n-layout>
</template>
