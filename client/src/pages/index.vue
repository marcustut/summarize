<script setup lang="ts">
import { useFetch } from "@vueuse/core";
import type {
  SummarizeMethod,
  SummarizeResponse,
  SummarizeType,
} from "~/types";

const BASE_URL = "http://127.0.0.1:8000/summarize";

const method = ref<SummarizeMethod>("naive");
const type = ref<SummarizeType>("text");
const text = ref("");
const requestUrl = ref("");

const { isFetching, execute, error, data } = useFetch<SummarizeResponse>(
  requestUrl,
  {
    immediate: false,
  }
)
  .get()
  .json();

watch(error, () => error.value && alert(error.value));

const handleSummarize = () => {
  requestUrl.value = `${BASE_URL}/${type.value}/${method.value}?text=${text.value}`;
  execute();
};

const { t } = useI18n();
</script>

<template>
  <div overflow="x-hidden">
    <p class="text-4xl">
      <carbon-document class="inline-block" />
    </p>
    <p>
      <a
        rel="noreferrer"
        href="https://github.com/marcustut/summarize"
        target="_blank"
      >
        Summarize
      </a>
    </p>
    <p>
      <em class="text-sm opacity-75">{{ t("intro.desc") }}</em>
    </p>

    <div class="py-4" />

    <textarea
      id="input"
      v-model="text"
      :placeholder="t('home.enter_text_here')"
      :aria-label="t('home.enter_text_here')"
      type="text"
      autocomplete="false"
      @keydown.enter="handleSummarize"
      p="x-4 y-2"
      w="400px"
      max-w="80vw"
      h="200px"
      bg="transparent"
      resize="~"
      border="~ rounded gray-200 dark:gray-700"
      outline="none active:none"
    />
    <label class="hidden" for="input">{{ t("home.enter_text_here") }}</label>

    <select
      name="method"
      id="method"
      v-model="method"
      m="x-auto t-2"
      w="400px"
      display="block"
      border="~ rounded"
      bg="transparent"
      outline="active:none"
    >
      <option value="naive">Naive</option>
      <option value="textrank">Textrank</option>
      <option value="bart" disabled>Bart</option>
      <option value="t5" disabled>T5</option>
      <option value="pegasus" disabled>Pegasus</option>
    </select>

    <div>
      <button
        class="m-3 text-sm btn"
        :disabled="!text"
        @click="handleSummarize"
      >
        {{ t("button.summarize") }}
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
