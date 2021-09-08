declare module "countable" {
  type Counter = {
    paragraphs: number;
    sentences: number;
    words: number;
    characters: number;
    all: number;
  };

  type Option = {
    hardReturns: boolean;
    stripTags: boolean;
    ignoreReturns: boolean;
    ignoreZeroWidth: boolean;
  };

  type Countable = {
    on: (
      target: Element | string,
      callback: (counter: Counter) => void,
      options?: Option
    ) => void;
    off: (element: Element) => void;
    count: (
      target: Element | string,
      callback: (counter: Counter) => void,
      options?: Option
    ) => void;
    enabled: (element: Element) => boolean;
  };

  const countable: Countable = {};

  export default countable;
}
