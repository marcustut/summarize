<script setup lang="ts">
import { useLoadingBar } from "naive-ui";
import { useRouter } from "vue-router";

const loadingBar = useLoadingBar();
const router = useRouter();

router.beforeEach(() => loadingBar.start());
router.afterEach(() => loadingBar.finish());
router.onError(() => loadingBar.error());
</script>

<template>
  <router-view />
</template>
