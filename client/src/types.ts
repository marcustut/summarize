import { ViteSSGContext } from "vite-ssg";

export type UserModule = (ctx: ViteSSGContext) => void;

export type SummarizeType = "text" | "url";

export type SummarizeMethod = "naive" | "textrank" | "bart" | "t5" | "pegasus";

export type SummarizeResponse = {
  summary: string;
  length: number;
};
