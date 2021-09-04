<script setup lang="ts">
import { useFetch } from "@vueuse/core";

const URL = "http://127.0.0.1:8000/summarize/text/textrank?text=";

const text = ref("");
const url = ref(`${URL}`);

const { isFetching, execute, error, data } = useFetch<string>(url, {
  immediate: false,
})
  .get()
  .json();

watch(error, () => error.value && alert(error.value));

const handleSummarize = () => {
  url.value = URL + text.value;
  execute();
};

const { t } = useI18n();
</script>

<template>
  <div>
    <p class="text-4xl">
      <carbon-campsite class="inline-block" />
    </p>
    <p>
      <a
        rel="noreferrer"
        href="https://github.com/antfu/vitesse"
        target="_blank"
      >
        Summarize
      </a>
    </p>
    <p>
      <em class="text-sm opacity-75">{{ t("intro.desc") }}</em>
    </p>

    <div class="py-4" />

    <input
      id="input"
      v-model="text"
      :placeholder="t('intro.whats-your-name')"
      :aria-label="t('intro.whats-your-name')"
      type="text"
      autocomplete="false"
      @keydown.enter="handleSummarize"
      p="x-4 y-2"
      w="250px"
      text="center"
      bg="transparent"
      border="~ rounded gray-200 dark:gray-700"
      outline="none active:none"
    />
    <label class="hidden" for="input">{{ t("intro.whats-your-name") }}</label>

    <div>
      <button
        class="m-3 text-sm btn"
        :disabled="!text"
        @click="handleSummarize"
      >
        {{ t("button.go") }}
      </button>
    </div>

    <p>isFetching: {{ isFetching }}</p>
    <p>{{ data }}</p>
  </div>
</template>

<route lang="yaml">
meta:
  layout: home
</route>
