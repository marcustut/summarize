<script setup lang="ts">
import {
  NConfigProvider,
  NLoadingBarProvider,
  NMessageProvider,
  NNotificationProvider,
  useOsTheme,
  darkTheme,
} from "naive-ui";
import { storeToRefs } from "pinia";
import { useThemeStore } from "~/stores/theme";

const themeStore = useThemeStore();
const { theme } = storeToRefs(themeStore);

const currentTheme = computed(() =>
  theme.value === "dark" ? darkTheme : null
);

const osTheme = useOsTheme();
debouncedWatch(osTheme, () => themeStore.setTheme(osTheme.value), {
  debounce: 500,
});
</script>

<template>
  <n-config-provider :theme="currentTheme">
    <n-loading-bar-provider>
      <n-message-provider>
        <NNotificationProvider>
          <slot />
        </NNotificationProvider>
      </n-message-provider>
    </n-loading-bar-provider>
  </n-config-provider>
</template>
