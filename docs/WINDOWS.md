# Set-up instructions for Windows 10/11

Welcome to **Windows 10/11 set up**!

Your first step in this journey is to **carefully read** the steps in this tutorial. You'll learn how to set up your computer. This section deals with setting up **'Windows Subsystem for Linux'** (WSL) on Windows 10/11, which enables you to run Linux command line inside Windows.

In this course we will be using **'WSL 2'**.

**Step 1:** Follow **[this guide](guides/WSL2_Installation_Guide_for_Windows_10.md#windows-subsystem-for-linux-installation-guide-for-windows-10)** to setup **'WSL 2'** on Windows 10/11.

**<span id="step-2"></span>Step 2:** Open a terminal (remember **[this](guides/WSL2_Installation_Guide_for_Windows_10.md#7-opening-the-wsl-terminal)**!) and run the following command. It will install **'Git'**. **'Git'** is a version control software that facilitates collaboration of people working together on the same code and keeps track of the versions as the code changes. You will learn more about **'Git'** in Week 02 of this course.

```bash
sudo apt update && sudo apt upgrade && sudo apt install git
```

**Step 3:** Also in the terminal check if you already have **'Python3.13'** by using the command below. If your version is `Python 3.13.x` (`x` = any number), you can skip to [step 4](#step-4), otherwise continue with steps 3.1 and 3.2.

```bash
python3.13 --version
```

**Step 3.1:** Let's set up **'Python 3.13'** (if you get an error with the next command, check [this](troubleshooting.md#6-when-setting-up-python-38-i-get-an-error)). First, add the `deadsnakes repository` - a place from where you will download **'Python 3.13'**:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
```

**Step 3.2:** Run the following command to install **'Python 3.13'**:

```bash
sudo apt update && sudo apt install python3.13 -y
```

> ⚠️ **Warning:** If you get this error:
> 
> ![alt text](image.png)
> 
> Run:
> 
> ```bash
> sudo apt update && sudo apt install --fix-broken libc6 -y
> ```
> 
> Then, install Python 3.13 again with:
>
> ```bash
> sudo apt update && sudo apt install python3.13 -y
> ```

> <!-- If necessary, before reinstallation:
>  
> And then:
>
> ```bash
> sudo dpkg --configure -a
> ```
> -->

**<a id="step-4" style="color: black;">Step 4:</a>** Run the following command to get `pip` and `venv`. **'pip'** is a package manager - it will help you easily install software. **'venv'** is a software for creating virtual environments (we will come back to what this means in the next set up step):

```bash
sudo apt update && sudo apt upgrade && sudo apt install python3-pip python3.13-venv -y
```

And you're done! Go back to the main menu and continue with setting up Git and GitHub in [step 3](../README.md#3-setup-git-and-gitHub_).
