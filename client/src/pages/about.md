---
title: About
---

<div class="text-center">
  <!-- You can use Vue components inside markdown -->
  <carbon-dicom-overlay class="text-4xl -mb-6 m-auto" />
  <h3>About</h3>
</div>

<br/>
<br/>

**Summarize** is a simple yet amazing tool for your everyday reading needs!

This tool utilises five algorithms: [Naive](https://github.com/marcustut/summarize/blob/main/notebooks/naive.ipynb), [TextRank](https://github.com/marcustut/summarize/blob/main/notebooks/textrank.ipynb), [BART](https://github.com/marcustut/summarize/blob/main/notebooks/BART.ipynb), [T5](https://github.com/marcustut/summarize/blob/main/notebooks/T5.ipynb) and [Pegasus](https://github.com/marcustut/summarize/blob/main/notebooks/pegasus.ipynb). Feel free to click on them to understand the workings under the hood!

This tool is so easy to use that we believe you need no further prompts. Though, there are a couple of things to take note of:

1. Adjust the slider to tweak your summary length. (Values are in percentage.)
2. Your text should not be lesser than 10 words. (Why would you summarise it anyway?)
3. **Summarize** currently only supports English. (Fingers crossed: we are looking forward to implementing Malay and Chinese.)
4. BART, T5 and Pegasus have limited usage because we are using a free-tier API. (We need to figure out how to cover our costs soon.)

Now you're good to go. Just paste in your text, URL or PDF and click on the green button - voila! Enjoy your snippet.

A guide to the algorithms:

1. Naive: copies all important sentences without changing anything.
2. Textrank: simply explained, it is an advanced version of Naive, but its output format might go haywire sometimes.
3. BART: mild rewrites of the text. Best for news and academia.
4. T5: mild rewrites of the text. Best for news and academia. You can try feeding it a story.
5. Pegasus: a one- or two-liner sentence. Best suited for headlines.