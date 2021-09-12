# summarize

This is a text summarizing tool written in Python

### User Guide
- The application is accessible [here](https://summarize.marcustut.tech/)
- However, due to limited free-tier server resources, the application may crash
- So it is advisable that you clone this project to your desktop and run the commands in the [`Makefile`](https://github.com/marcustut/summarize/blob/main/Makefile)
- You might not be able to run the abstractive models after reaching a character limit in HuggingFace Accelerated Inference API
- Therefore, it is advisable that you use the [`Notebooks`](https://github.com/marcustut/summarize/tree/main/notebooks) for replicating our results in the documentation
- Note that you might not be able to run `Pegasus` on the notebook successfully due to the amount of resources required
- So it is advisable that you run only the `Pegasus` model through the application interface

### Code folders

- `summarize` - The python library for all the algorithm
- `server` - The backend server using FastAPI
- `client` - The frontend app using Vue3

### Misc folders

- `notebooks` - A folder to keep all our jupyter notebooks testground
- `data` - A folder to keep all datasets needed to train or test the algorithm
- `docs` - Keep our documentation files
