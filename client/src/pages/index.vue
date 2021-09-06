<script setup lang="ts">
import {
  NP,
  NH2,
  NCard,
  NSpace,
  NTabs,
  NTabPane,
  NInput,
  NSelect,
  NSlider,
  NButton,
  NStatistic,
  useThemeVars,
  useMessage,
} from "naive-ui";
import { wordCounter } from "~/logic";
import type { SelectOption } from "naive-ui";
import type {
  SummarizeMethod,
  SummarizeResponse,
  SummarizeType,
} from "~/types";

const BASE_URL = "http://127.0.0.1:8000/summarize";
const METHODS = [
  { label: "Naive", value: "naive" },
  { label: "Textrank", value: "textrank" },
  { label: "BART", value: "bart", disabled: true },
  { label: "T5", value: "t5", disabled: true },
  { label: "Pegasus", value: "pegasus", disabled: true },
] as SelectOption[];

const method = ref<SummarizeMethod | null>(null);
const type = ref<SummarizeType>("text");
const text = ref("");
const url = ref("");
const percentage = ref(50);
const requestUrl = ref("");

const wordCount = computed(() => wordCounter(text.value));
const charCount = computed(() => text.value.length);

const naiveTheme = useThemeVars();
const message = useMessage();

const { isFetching, execute, error, data, onFetchError, onFetchResponse } =
  useFetch<SummarizeResponse>(requestUrl, {
    immediate: false,
  })
    .get()
    .json<SummarizeResponse>();

onFetchError(() => message.error(error.value));
onFetchResponse(() => message.success("Your text is summarized"));

const handleSummarize = () => {
  if (type.value === "text" && text.value.length < 10) {
    message.warning("Text cannot be shorter than 10 characters");
    return;
  }

  if (type.value === "url" && !url.value.startsWith("http")) {
    message.warning("Url is not valid");
    return;
  }

  if (!method.value) {
    message.warning("Method must be specified");
    return;
  }

  requestUrl.value =
    type.value === "text"
      ? `${BASE_URL}/${type.value}/${method.value}?text=${text.value}`
      : `${BASE_URL}/${type.value}/${method.value}?url=${encodeURI(url.value)}`;

  execute();
};

const setType = (newType: SummarizeType) => (type.value = newType);
const setText = (newText: string) => (text.value = newText);
const setUrl = (newUrl: string) => (url.value = newUrl);

const { t } = useI18n();
</script>

<template>
  <div w="full" max-w="4/5 lg:800px">
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

    <n-card>
      <n-space vertical :size="16">
        <n-tabs
          default-value="text"
          justify-content="space-evenly"
          type="line"
          :on-update:value="(newType) => setType(newType)"
        >
          <n-tab-pane name="text" :tab="t('home.text')">
            <n-input
              h="200px"
              type="textarea"
              :placeholder="t('home.enter-text-here')"
              :aria-label="t('home.enter-text-here')"
              :value="text"
              :on-update:value="(newText) => setText(newText)"
              clearable
            />
          </n-tab-pane>
          <n-tab-pane name="url" :tab="t('home.url')">
            <n-input
              type="text"
              :placeholder="t('home.enter-url-here')"
              :aria-label="t('home.enter-url-here')"
              :value="url"
              :on-update:value="(newUrl) => setUrl(newUrl)"
            />
          </n-tab-pane>
        </n-tabs>

        <n-slider v-model:value="percentage" :step="1" />

        <n-select
          v-model:value="method"
          filterable
          :placeholder="t('home.choose-a-method')"
          :options="METHODS"
        />

        <n-button
          w="full"
          :color="naiveTheme.primaryColor"
          :loading="isFetching"
          @click="handleSummarize"
        >
          {{ t("button.summarize") }}
        </n-button>
      </n-space>
    </n-card>

    <n-space justify="center" v-show="type === 'text'">
      <n-statistic m="t-4" text="center" :label="t('home.word-count')">
        {{ wordCount }}
      </n-statistic>
      <n-statistic m="t-4" text="center" :label="t('home.character-count')">
        {{ charCount }}
      </n-statistic>
    </n-space>

    <n-card m="t-4" v-show="data">
      <n-h2>{{ t("home.summary") }}</n-h2>
      <n-p>{{ data?.summary }}</n-p>
      <n-space justify="center"
        >{{ t("home.word-count") }}: {{ data?.length }}</n-space
      >
    </n-card>
  </div>
</template>

<route lang="yaml">
meta:
  layout: home
</route>
