# 3. Setup *Git* and *GitHub*

**'Git'** is a distributed version-control system for tracking changes in source code. A **'repository'** is where code lives, and the code from the prep course will live at [ds-prep-course-2025](https://github.com/LDSSA/ds-prep-course-2025) repository (basically where you are right now, reading this). All the learning materials and exercises will be released (made available) on this repository. You will learn more about **'Git'** in the learning units 3 and 6.

### 3.1 Sign up for GitHub

**Step 1:** [Sign up](https://github.com/join) for a **'GitHub'** account and follow the instructions.

**'GitHub'** is a web-based platform used for version control and collaboration on software development projects providing tools for hosting and managing **'Git'** repositories.

**Step 2:** Open a **'terminal'**. Configure your email and username by running the 3 commands below. (**replace** `mig.dias.1212@gmail.com` below with the same email you used for github and `buedaswag` with your **'GitHub'** username).

```bash
git config --global user.email "mig.dias.1212@gmail.com"
git config --global user.username "buedaswag"
git config --global user.name "Bueda Swag"
```

### 3.2 Setup your workspace repository

The **'workspace directory/repository'** is where you will place everything you are working on, solve exercises, make changes to files, etc.

**Step 1:** Log into **'GitHub'**.

**Step 2:** In the upper-right corner of the page, click the "+" button and select **'New repository'**:

<div style="text-align: center;">
  <img src='media/menu_create_repository.png' alt='New repository'  width="75%" />
</div>

**Step 3:** Create a new **private** repository called `ds-prep-workspace`.

1. You need to explicitly select `Private` - this is your private work environment where nobody else will have access but you.

2. Initialize with a `README`.

3. Add a Python `.gitignore`. This file does exactly what it sounds like - it tells **'Git'** which files to ignore when transfering files between your computer and **'GitHub'**.

<div style="text-align: center;">
  <img src="https://user-images.githubusercontent.com/19359518/112880653-9ef76280-90c2-11eb-8768-00b2153756d5.png" alt='Finder' width="75%">
</div>

You can also check [Creating a new repository](https://help.github.com/en/articles/creating-a-new-repository) on GitHub for help.

**Step 4:** Create your GitHub **Personal Access Token** (**PAT**)

Go to <https://github.com/settings/tokens> (or manually through your _user menu_ in the top right most circle in the page $\rightarrow$ _Settings_ $\rightarrow$ _Developer settings_ (last option in the list) $\rightarrow$ _Personal access tokens_ $\rightarrow$ _Tokens (classic)_), and click on **'Generate new token'**. You can give it a name in the note field, such as `ldsa-token`. Then select `repo` in the scopes and click on **'Generate token'**. You will be shown a **'token'** you **should save** - ❗ **IMPORTANT:** **You will not be able to see it again after leaving that window**.


<div style="text-align: center;">
  <img src='media//personal_access_token.PNG' width="75%" />
</div>












### 3.3 Clone your workspace repository

Your **'workspace repository'** now exists on **'GitHub'**, but you also need a local copy (clone) on your computer. You will be working in the **'local workspace repository'** and then transfer your work to your **'remote workspace repository'** on **'GitHub'**.

**Step 1:** Open a terminal (or use one you've already opened).

**Step 2:** Create a directory named `projects` by using the `mkdir` command. Don't feel intimidated by these commands. They are simply `bash` - a language to communicate with your operating system. `mkdir` essentially stands for **m**a**k**e **dir**ectory. The tilde symbol `~` is a shortcut address for your home directory.

```bash
mkdir ~/projects
```

**Step 3:** Enter the directory by using the `cd` command. Did you know that `cd` means **c**hange **d**irectory? So basically changing to a different directory.

```bash
cd ~/projects
```

**Step 4:** You can now **clone** (create a local copy of) the `ds-prep-workspace` repository you created on **'GitHub'**.
Replace `<username>` and `<personal access token>` below with your **'GitHub'** **username** and **personal access token**, respectively: 

```bash
git clone https://<username>:<personal access token>@github.com/<username>/ds-prep-workspace.git
```

> 📝 **Note:** GitHub Personal Access Tokens are sequences of characters that begin with `ghp_` which **is also part of the token**

> 📝 **Note:** You have to replace `<username>` twice in the command

> 📝 **Note**: If you have had a **'GitHub'** account since before this course and you are using **'SSH keys'** instead of **'tokens'**, first make sure that you have completed the steps starting [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys), then clone your repository like this:
> 
> ```bash
> git clone git@github.com:<username>/ds-prep-workspace.git
> ```

> 📝 **Note**: When performing this step, if you're prompted for your **'GitHub'** username, type it and press <kbd>enter</kbd>. If you're prompted for your git password, **use your token instead** and press <kbd>enter</kbd>, as passwords no longer work for **'GitHub'** CLI access.

If the cloning worked out, you should now have a local copy of the content of your `ds-prep-workspace` repository inside your `~/projects/ds-prep-workspace` directory, which you can check using:

```bash
ls ~/projects
```

If it lists `ds-prep-workspace`, you're good to go!

### 3.4 Clone the `ds-prep-course-2025` repository

Let's clone the [ds-prep-course-2025](https://github.com/LDSSA/ds-prep-course-2025) repository. This is where all of the learning materials will be made available as the prep course progresses. You will be getting them (pulling) from there.

**Step 1:** Open a **'terminal'** (or use one you've already opened) and enter the `projects` directory:

```bash
cd ~/projects
```

**Step 2:** Clone the Prep Course repository (it's the same that contains the README you're reading right now!):

```bash
git clone https://github.com/LDSSA/ds-prep-course-2025.git
```

If you are using **'SSH keys'** for **'GitHub'**, use this command:

```bash
git clone git@github.com:LDSSA/ds-prep-course-2025.git
```

If the cloning worked out, you should see the cloned repository directory `ds-prep-course-2025` in your `projects` directory. You can see if it's there by listing its contents:

```bash
ls ~/projects
```

**Step 3:** Copy the `requirements.txt` file from the **'prep course repository'** to your **'local workspace repository'**. The `cp` bash command means **c**o**p**y. Then you have the address of the file that is being copied and to where it is copied.

```bash
cp ~/projects/ds-prep-course-2025/requirements.txt ~/projects/ds-prep-workspace
```
You can check if the copying worked out by listing the contents of the `ds-prep-workspace` directory. The `requirements.txt` file should be there.

```bash
ls ~/projects/ds-prep-workspace
```

And you're done with setting **'Git'** and **'GitHub'**! Go back to the main menu and continue with [step 4](../README.md#4-Setup-for-all-operating-systems-python-virtual-environment), setting up your Python virtual environment.
