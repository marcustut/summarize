<script setup lang="ts">
import {
  NConfigProvider,
  NDialogProvider,
  NMessageProvider,
  NLoadingBarProvider,
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
      <n-dialog-provider>
        <n-message-provider>
          <n-notification-provider>
            <slot />
          </n-notification-provider>
        </n-message-provider>
      </n-dialog-provider>
    </n-loading-bar-provider>
  </n-config-provider>
</template>
