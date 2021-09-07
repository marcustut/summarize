<script setup lang="ts">
import { useHead } from "@vueuse/head";
import Provider from "~/components/Provider.vue";
import Viewer from "~/components/Viewer.vue";

// https://github.com/vueuse/head
// you can use this to manipulate the document head in any components,
// they will be rendered correctly in the html results with vite-ssg
useHead({
  title: "Summarize",
  meta: [
    {
      name: "description",
      content: "Summarize text through Artificial Intelligence",
    },
    { name: "url", content: "https://text-summarize.netlify.app" },
    {
      name: "image",
      content: "https://i.ibb.co/rsZJhsK/pwa-512x512.png",
    },
  ],
});
</script>

<template>
  <provider>
    <viewer />
  </provider>
</template>
