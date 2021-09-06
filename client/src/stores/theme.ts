import { acceptHMRUpdate, defineStore } from "pinia";
import { useStorage } from "@vueuse/core";

export type ThemeOptions = "dark" | "light" | null;

export const useThemeStore = defineStore("theme", {
  state: () => ({
    theme: useStorage("summarize-theme", "dark" as ThemeOptions),
  }),
  actions: {
    setTheme(newTheme: ThemeOptions) {
      this.theme = newTheme;
    },
  },
});

if (import.meta.hot)
  import.meta.hot.accept(acceptHMRUpdate(useThemeStore, import.meta.hot));
