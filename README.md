# Summarize

_Written by: Ling Li Ya_

This is a text summarizing tool written in Python.

## User Guide

### 1. Downloading the project

Either download the `.zip` file in Google Classroom from our GitHub.
![image](https://user-images.githubusercontent.com/68136684/132977151-96da4d56-b1dc-4578-879a-1f7b352f5200.png)

Then unzip the `.zip` file. You will see the file `summarize-main`.
![image](https://user-images.githubusercontent.com/68136684/132977199-44aec6c7-064b-457f-8907-6a59a1ca3d34.png)

### 2. Install prerequisites

You need `Python` and `Node.js` installed. Open up command prompt (cmd) and type in the code below.

To check whether `Python` is installed:
```bsh
$ python
```

You will see this is it is installed. Note that your version might be different.
![image](https://user-images.githubusercontent.com/68136684/132977269-2f92a428-b66c-47e1-99e4-af40bef635bb.png)

Type `exit()` to exit the `Python` shell if it is installed.

To check whether `Node.js` is installed:
```bsh
$ node
```

You will see this is it is installed. Note that your version might be different.
![image](https://user-images.githubusercontent.com/68136684/132977298-1be0494e-b965-45bc-acfd-2f6f6d5e3957.png)

Otherwise, [download `Python`](https://www.python.org/downloads/) and/or [`Node.js`](https://nodejs.org/en/) here. Run the installer and follow its instructions. Verify your installation.

### 3. Install project `Python` dependencies

Double click on `summarize-main`. Single click on the `summarize` folder, hold down your `shift` key, and right click on the folder. Select `Open PowerShell window here`.
![image](https://user-images.githubusercontent.com/68136684/132977426-00e7e749-7bf0-47b2-b7c4-cc0a713c28f5.png)

A `PowerShell` window will pop up. Then right click on the `Makefile` in the file explorer and open it with `Notepad`.
![image](https://user-images.githubusercontent.com/68136684/132977450-e765f1c7-bb64-40fa-97aa-ee9bc3244094.png)

Something like this will pop up:
![image](https://user-images.githubusercontent.com/68136684/132977464-3ff5b6a4-3811-4060-94a3-30e137d3dd96.png)

These are the commands to install all the project `Python` dependencies. Simply copy the command and paste them in the `PowerShell` window. If you encounter this warning message:
![image](https://user-images.githubusercontent.com/68136684/132977519-01c70de3-1a96-46af-a558-e2da387b8112.png)

Simply retype the command with an additional flag `pip install -r requirements.txt --use-feature-in-tree-build`. Then let it run.
![image](https://user-images.githubusercontent.com/68136684/132977559-8e631e01-eaa9-48d5-925a-69bb8f70ba19.png)

### 4. Install our `summarize` library

We have made our application into a `Python` library and you need to install it with the command below:
![image](https://user-images.githubusercontent.com/68136684/132977602-61895d60-a9d5-43c8-a5b6-fd2f4a4cb990.png)

### 5. Run the backend server

Be sure that you select the command under the `server-dev` instead of `server-prod`.
![image](https://user-images.githubusercontent.com/68136684/132977638-63d1670a-cad1-448f-b6bd-cc987f1f7901.png)

### 6. Prepare the frontend client

Open up another `PowerShell` window this time by holding `shift` and right clicking the `server` folder.

After you have installed `Node.js`, run the following command to install `pnpm`.

```bsh
$ npm install -g pnpm
```

After installing `pnpm`, type `cd client` to go into the `client` folder in the new `PowerShell` window.

Then return to your `Notepad` and run the command `pnpm i` in the `PowerShell` window. It will take 10 - 20 seconds to install.
![image](https://user-images.githubusercontent.com/68136684/132977838-09189029-3466-4f98-8200-a9b73010ab11.png)

### 7. Run the frontend client

Lastly, run this command in the `PowerShell` window to launch the application on `localhost:3333`
![image](https://user-images.githubusercontent.com/68136684/132977886-889c69e3-c053-456b-9b2a-74dc40ce38a1.png)

- The application is accessible [here](https://summarize.marcustut.tech/)
- However, due to limited free-tier server resources, the application may crash
- So it is advisable that you clone this project to your desktop and run the commands in the [`Makefile`](https://github.com/marcustut/summarize/blob/main/Makefile)
- You might not be able to run the abstractive models after reaching a character limit in HuggingFace Accelerated Inference API
- Therefore, it is advisable that you use the [`Notebooks`](https://github.com/marcustut/summarize/tree/main/notebooks) for replicating our results in the documentation
- Note that you might not be able to run `Pegasus` on the notebook successfully due to the amount of resources required
- So it is advisable that you run only the `Pegasus` model through the application interface

## Code folders

- `summarize` - The python library for all the algorithm
- `server` - The backend server using FastAPI
- `client` - The frontend app using Vue3

## Misc folders

- `notebooks` - A folder to keep all our jupyter notebooks testground
- `data` - A folder to keep all datasets needed to train or test the algorithm
- `docs` - Keep our documentation files
