<script setup lang="ts">
// @ts-ignore
import pdfjsWorker from "pdfjs-dist/build/pdf.worker.entry";
import { getDocument, GlobalWorkerOptions } from "pdfjs-dist";
import Countable from "countable";
import {
  NP,
  NH2,
  NSpin,
  NCard,
  NSpace,
  NTabs,
  NTabPane,
  NInput,
  NSelect,
  NSlider,
  NButton,
  NIcon,
  NText,
  NUpload,
  NUploadDragger,
  NStatistic,
  useThemeVars,
  useMessage,
  useNotification,
  useDialog,
} from "naive-ui";
import { SERVER_URL } from "~/logic";
import type { SelectOption, UploadFileInfo } from "naive-ui";
import type {
  SummarizeMethod,
  SummarizeResponse,
  SummarizeType,
} from "~/types";
import type { TextItem } from "pdfjs-dist/types/display/api";

GlobalWorkerOptions.workerSrc = pdfjsWorker;

const BASE_URL = `${SERVER_URL}/summarize`;

const METHODS = [
  { label: "Naive", value: "naive" },
  { label: "Textrank", value: "textrank" },
  { label: "BART", value: "bart" },
  { label: "T5", value: "t5" },
  { label: "Pegasus", value: "pegasus" },
] as SelectOption[];

const method = ref<SummarizeMethod | null>(null);
const type = ref<SummarizeType | "pdf">("text");
const text = ref("");
const url = ref("");
const percentage = ref(50);
const requestUrl = ref("");
const wordCount = ref(0);
const ready = ref(false);

const isNotNaive = computed(() => method.value !== "naive");
const charCount = computed(() => text.value.length);

watch(text, () =>
  Countable.count(text.value, (counter) => (wordCount.value = counter.words))
);

const naiveTheme = useThemeVars();
const dialog = useDialog();
const message = useMessage();
const notification = useNotification();

const { isFetching, execute, error, data, onFetchError, onFetchResponse } =
  useFetch<SummarizeResponse>(requestUrl, {
    immediate: false,
  })
    .get()
    .json<SummarizeResponse>();

onFetchError(() => message.error(error.value));
onFetchResponse(() => message.success("Your text is summarized"));

onMounted(() => {
  fetch(SERVER_URL)
    .then(() => (ready.value = true))
    .catch(() => {
      const n = notification.error({
        title: "Opps, there's been an error",
        content: "The server is currently offline",
        meta: new Date().toLocaleString(),
        action: () =>
          h(
            NButton,
            {
              text: true,
              type: "primary",
              onClick: () => {
                ready.value = true;
                n.destroy();
              },
            },
            {
              default: () => "Continue anyway",
            }
          ),
      });
    });
});

const handleSummarize = () => {
  if (type.value === "text" && text.value.length < 10) {
    message.warning("Text cannot be shorter than 10 characters");
    return;
  }

  if (type.value === "url" && !url.value.startsWith("http")) {
    message.warning("Url is not valid");
    return;
  }

  if (type.value === "pdf" && text.value.length < 10) {
    message.warning("PDF is not uploaded or lesser than 10 characters");
    return;
  }

  if (!method.value) {
    message.warning("Method must be specified");
    return;
  }

  requestUrl.value =
    type.value === "text" || type.value === "pdf"
      ? `${BASE_URL}/text/${method.value}?text=${encodeURIComponent(
          text.value
        )}&percentage=${percentage.value}`
      : `${BASE_URL}/${type.value}/${method.value}?url=${encodeURI(
          url.value
        )}&percentage=${percentage.value}`;

  execute();
};

const handleFileUpload = async ({
  file,
  fileList,
}: {
  file: UploadFileInfo;
  fileList: UploadFileInfo[];
  event: ProgressEvent | Event | undefined;
}) => {
  if (fileList.length === 0) return;

  if (!file.file) {
    console.error("Error uploading file: ", file);
    message.error("Error uploading file, try again");
    return;
  }

  if (fileList.length > 1) {
    fileList.pop();
    message.error("Only 1 file is accepted, remove previous file");
    return;
  }

  text.value = "";

  const arrBuffer = await file.file.arrayBuffer();

  getDocument(new Uint8Array(arrBuffer))
    .promise.then((pdf) => {
      for (let i = 1; i <= pdf.numPages; i++) {
        pdf.getPage(i).then((page) =>
          page.getTextContent().then((textContent) =>
            textContent.items.forEach((item) => {
              if (item && (item as TextItem).str) {
                text.value += (item as TextItem).str + "\n";
              }
            })
          )
        );
      }

      message.success(`${file.name} is uploaded`);
    })
    .catch((err) => {
      console.error(err);
      message.error("Failed converting PDF to text. Try another file");
    });
};

const handleFilePreview = () => {
  if (text.value === "") {
    message.error("No file uploaded");
    return;
  }

  dialog.info({
    title: "Preview",
    content: () =>
      h(NText, { class: "whitespace-pre-wrap" }, { default: () => text.value }),
  });
};

const handleFileRemove = () => (text.value = "");

const setType = (newType: SummarizeType) => (type.value = newType);
const setText = (newText: string) => (text.value = newText);
const setUrl = (newUrl: string) => (url.value = newUrl);

const { t } = useI18n();
</script>

<template>
  <div w="full">
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

    <n-spin :show="!ready">
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
            <n-tab-pane name="pdf" :tab="t('home.pdf')">
              <n-upload
                accept="application/pdf"
                @change="handleFileUpload"
                @preview="handleFilePreview"
                @remove="handleFileRemove"
              >
                <n-upload-dragger>
                  <div style="margin-bottom: 12px">
                    <n-icon size="48" :depth="3">
                      <ion:archive-outline />
                    </n-icon>
                  </div>
                  <n-text style="font-size: 16px">
                    {{ t("home.upload-title") }}
                  </n-text>
                  <n-p depth="3" style="margin: 8px 0 0 0">
                    {{ t("home.upload-description") }}
                  </n-p>
                </n-upload-dragger>
              </n-upload>
            </n-tab-pane>
          </n-tabs>

          <n-slider v-show="isNotNaive" v-model:value="percentage" :step="1" />

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

      <n-space justify="center" v-show="type === 'text' || type === 'pdf'">
        <n-statistic m="t-4" text="center" :label="t('home.word-count')">
          {{ wordCount }}
        </n-statistic>
        <n-statistic m="t-4" text="center" :label="t('home.character-count')">
          {{ charCount }}
        </n-statistic>
      </n-space>
    </n-spin>

    <n-card m="t-4" v-show="data">
      <n-h2>{{ t("home.summary") }}</n-h2>
      <n-p style="word-wrap: break-word">{{ data?.summary }}</n-p>
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
