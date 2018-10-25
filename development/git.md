---
title: Accessing the FieldTrip source code through Git
layout: default
tags: [development, git]
---

# Accessing the FieldTrip source code through Git

The FieldTrip code is accessible using [git](http://git-scm.com/) at [github](http://github.com/fieldtrip/fieldtrip).

`<note>`
To quickly get access to the code, you would do the following from the command line or the equivalent in a graphical git interface, such as the [GitHub desktop](https://desktop.github.com).

	
	git clone https://github.com/fieldtrip/fieldtrip

Note that all of this goes on a single line, but the link is slightly too long for it being properly displayed here.

This allows you to easily track the changes that we make to the code. If you also want to contribute back, please make an account on github, fork FieldTrip to our own account and read on for a complete tutorial.

</div>

To keep an eye on the changes to the code, you can follow FieldTrip on [Twitter](http://twitter.com/fieldtriptoolbx).
## Development workflow

We use git and github.com (see below) in combination with a [Forking Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows#forking-workflow) for our development. We complement this with code reviews by the core team and quality control using running a set of test scripts. The general procedure is as follow

 1.  The contributor/developer makes the suggested changes in a branch, pushes that branch to his/her own fork (on github) and submits a pull request.
 2.  The core team reviews the code in the pull request. The suggested change should make sense, fit in the larger strategy, should be consistent with other code, and should be documented. 
 3.  The code in the pull request is tested by the core team to ensure that it does not break anything. 
 4.  After successful reviewing and testing, the core team merges the pull request with the master branch.

## How to contribute with git and github.com

We welcome the contribution of external users, even if the changes consist of a few lines of code. The git version control system offers a simple and straightforward way to add your contribution to the FieldTrip toolbox.

### What is git?

[git](http://git-scm.com/) is version control system to keep track of the changes to files and maintain a consistent repository, just like [svn](http://subversion.tigris.org/). While svn follows a linear approach to version, where each user makes some changes to the main code and then a second user can make some other changes, git allows for multiple users to work in parallel and then merge their code in the main repository. This approach scales very well, considering that, for example, the [Linux kernel](http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git) and [ android](https://android.googlesource.com/) use git.
 
There are lots of resources available on the internet to learn more about git. The starting point is [this documentation](http://git-scm.com/documentation). If you have a question, it's most likely already being answered at [Stack Exchange](http://stackoverflow.com/questions/tagged/git). git is extremely powerful and flexible, so the following tutorial will give only the most basic ideas and tools to modify the FieldTrip code.
#### Basic concepts

##### push, pull, clone
git lives on two level
 1.  on your local computer
 2.  on a remote server
Both contain a full repository of the whole code. The basic idea is that you make some changes on your local copy and then send them to the remote server. Sending changes to a remote repository is called [pushing](http://git-scm.com/docs/git-push) and receiving changes from a remote repository to your local machine is called [pulling](http://git-scm.com/docs/git-pull). The first time that you want to copy a complete repository from a remote server to your local machine, you need to [clone](http://git-scm.com/docs/git-clone) the repository.
##### commit

Your local repository is a complete repository of the whole source code. As such, you can modify some files (or even adding some files) and then include these changes to the local repository. This procedure is called [commit](http://git-scm.com/docs/git-commit). The changes that are committed to your local repository are called **commits**.
##### branch, merge

One of the most powerful features of git is the idea of [branching](http://git-scm.com/book/en/Git-Branching): *Branching means you diverge from the main line of development and continue to do work without messing with that main line*. So, from your local repository, you can create a new branch, make some changes, commit them. If you are happy with the changes, you can [merge](http://git-scm.com/docs/git-merge) your new branch with the main development line. Branches are very flexible because they allow you to develop new features without compromising the main repository. You can easily switch between the main branch (often called **master**) and experimental branches.
##### Main commands

To recap, the main commands that you'll need here ar

*  **clone** to create a new local repository based on a remote repository

*  **push** to send your local changes to the remote repository

*  **pull** to receive the remote changes on your local repository (it runs two processes: **fetch**, where the remote changes are downloaded, and **merge**, where the changes are integrated into your local repository)

*  **commit** to add some changes to your local repository

*  **branch** to list the branches

*  **checkout** to switch to an existing branch

*  **checkout -b** to create a new branch

*  **merge** to merge a branch with your main local repository.
You can use any of these commands on the command line, in Linux and Mac, by doin
`git name_of_the_command`
For example, using
`git checkout master`
you will switch from a side branch into the main branch of your repository.

### What is github.com?

[github.com](http://github.com) is a fast, intuitive and popular website to share code. The interface is clean and intuitive, and many projects are hosted there, including [FieldTrip](https://github.com/fieldtrip/fieldtrip). 

### How to add a feature or fix a bug

You only have read permission for the [FieldTrip](https://github.com/fieldtrip/fieldtrip), meaning that you cannot change directly the code of the FieldTrip repository. What you can do, and you will see how to do it here, i
 1.  Copy the FieldTrip repository under your private account on github.com (this is called **forking**).
 2.  This new personal repository will become your __remote repository__. You will need __clone__ the remote repository onto your local machine. 
 3.  You will create a new __branch__, edit some files, __commit__ them to the developmental branch of your __local repository__. 
 4.  Then you can __push__ this developmental __branch__ to your __remote repository__. 
 5.  You will then tell to the developers of FieldTrip to check these changes in your __remote repository__, using a **pull request**.
All the __underlined__ words are the new concepts explained above. **Forking** and **pull request** are two main concepts when working with multiple remote repositories. I will use them throughout the tutorial and are the words that you will need to successfully google possible problems. If they are not clear, refer to the main [documentation](http://git-scm.com/documentation). 

## Tutorial

Now that the main concepts are explained, we will try to add a new feature to FieldTrip using a minimal example. In our case, what we think that FieldTrip really needs is that when you run **[ft_defaults](/reference/ft_defaults)**, you get a text saying *Welcome to FieldTrip*. So we need to create a new function that prints *Welcome to FieldTrip* and modify the existing function **[ft_defaults](/reference/ft_defaults)** to run our new function. We expect that you already have git running on your system (see [installation instructions](http://git-scm.com/book/en/Getting-Started-Installing-Git)) and that you have an account on [http://github.com](http://github.com) (see [set up git](https://help.github.com/articles/set-up-git)). Let's say that your username on github is *USERNAME*.

### 1. Fork the main FieldTrip

Go with your web browser to [https://github.com/fieldtrip/fieldtrip](https://github.com/fieldtrip/fieldtrip) and click on the right-hand side, towards the top, on **fork**. This will create a new remote repository in your github account at the address: https://github.com/USERNAME/fieldtrip. The title of your repository will sa

	
	username / fieldtrip
	forked from fieldtrip/fieldtrip

### 2. Clone your remote repository

Now you can just clone your remote repository. There are two equivalent methods to connect to your remote repository: https (see [setup instructions](https://help.github.com/articles/set-up-git)) or ssh (see [setup instructions](https://help.github.com/articles/generating-ssh-keys)). If you're using https, the

	
	git clone https://github.com/USERNAME/fieldtrip.git

If you're using SSH, us

	
	git clone git@github.com:USERNAME/fieldtrip.git

Now you have a local repository of FieldTrip that you can work on. Then go into the just-created FieldTrip director

	
	cd fieldtrip

### 3. Create an experimental branch

Before you start editing files, create a new branch. We will call our new branch *welcome*. Let's create i

	
	git checkout -b welcome

and it'll tell yo

	
	Switched to a new branch 'welcome'

If you have filed a bug on [Bugzilla](/bugzilla), you could name your new branch *bugXXXX* where XXXX is the number of the bug.

### 4. Add and edit files

Now we need to create a function that says *Welcome to FieldTrip*. Let's call it *ft_welcome.m*, just as you'd create any new Matlab function. 
<div class="important">
When you create a new function or edit an existing one, follow the [code guidelines](/development/guidelines/code) for a consistent and readable code.
</div>
In addition to this function, we will also modify the function **[ft_defaults](/reference/ft_defaults)**. 

### 5. Commit your changes

To see how git reacts to this changes, you can now typ

	
	git status

It will tell yo

	
	# On branch welcome
	# Changes not staged for commi
	#   (use "git add `<file>`..." to update what will be committed)
	#   (use "git checkout -- `<file>`..." to discard changes in working directory)
	#
	#	modified:   ft_defaults.m
	#
	# Untracked file
	#   (use "git add `<file>`..." to include in what will be committed)
	#
	#	ft_welcome.m
	no changes added to commit (use "git add" and/or "git commit -a")

If you want to review the changes you made, you can typ

	
	git diff

Now we add our changes to the commi

	
	git add ft_welcome.m ft_defaults.m

and now *git status* will tell yo

	
	# On branch welcome
	# Changes to be committe
	#   (use "git reset HEAD `<file>`..." to unstage)
	#
	#	modified:   ft_defaults.m
	#	new file:   ft_welcome.m
	#

You can now commit these changes.

	
	git commit -m "print welcome message when executing ft_defaults"

where the option -m allows you to add a log entry.
<div class="important">
Follow these [guidelines](/development/guidelines/code#svn_log_messages) when writing a log entry.
</div>
and git will retur

	
	 1 file changed, 1 insertion(+)
	 create mode 100644 ft_welcome.m

#### Switch to master

While you are working on the developmental branch called *welcome*, you might want to run some analysis on the main branch (called by default *master*). You can easily switch into the main branch wit

	
	git checkout master

and then you go back to the developmental branch with

	
	git checkout welcome

You see on which branch you are with

	
	git branch

Switching between branches is really fast, so do not be afraid of doing it when necessary.

### 6. Push the commits

We modified our local repository but the remote repository has not changed. We need to push our commits to the personal remote repository. By default, the remote repository is called **origin**. You can rename it. If you want more information about remote repository, just typ

	
	git remote -v

The code to push commits i

	
	git push origin welcome

which means that we are pushing the commits in the branch called *welcome* to the remote repository called *origin*. This will create a new branch in your remote repository, as the last line of the output will kindly tell yo

	
	...

	 * [new branch]      welcome -> welcome

### 7. Make a pull request

Go to [github.com](https://github.com) to review the changes. By default on the webpage, you are shown the branch *master*, so you should switch to the newly created branch called *welcome*. Review the commits, by clicking on *commits*. Click on **pull request** in the top middle. The next page will show you the changes that are part of the pull request. 
<div class="important">
You are about to send the changes to the main developers of FieldTrip, so explain in the box what you did and why. Please, review the commits very carefully before sending the pull request. It happens that you have commits that you forgot about and you did not intend to share. 
</div>
Do **not** click on **Send Pull Request** when finishing this tutorial.
### 8. Clean up

When you are done, you can delete the branch *welcome* on the local and remote repository. To delete the branch on your local and remote repository, you can us

	
	git branch -D welcome
	git push origin :welcome

### 9. Keeping up to date

Your suggested contributions to FieldTrip will not be the only changes: the code on the master branch is constantly updated. This means that you should regularly synchronize to benefit from these updates and to ensure that you won't be making changes to an outdated copy of the code. 

<div class="important">
It is important to first pull the changes from others before you start implementing your own changes, otherwise your (new) changes might conflict with already accepted changes to the code.
</div>

Synchronizing between the different repositories is done by using your local (i.e. hard disk) copy as intermediary. By default your personal copy of the repository on github will be called the *origin*. You can check this with

    git remote -v

which will show you
    origin	git@github.com/USERNAME/fieldtrip.git (fetch)
    origin	git@github.com/USERNAME/fieldtrip.git (push)
or the corresponding URL with https instead of git.

To synchronize with the official fieldtrip repository on github, you should also add it as a remote. Best practice is to call it the *upstream* repository. You add it with

    git remote add upstream https://github.com/fieldtrip/fieldtrip.git
    git remote -v

will now show you both remotes

    origin	git@github.com/robertoostenveld/fieldtrip.git (fetch)
    origin	git@github.com/robertoostenveld/fieldtrip.git (push)
    upstream	https://github.com/fieldtrip/fieldtrip.git (fetch)
    upstream	https://github.com/fieldtrip/fieldtrip.git (push)

You can pull (download) from the *upstream* repository and push (upload) to your own *origin* repository.

To pull the changes from the master branch of the (official) *upstream* FieldTrip repository, you would do

    git checkout master
    git pull upstream master

This may (or may not) show changes to files and new files that were added. Subsequently, you can push those changes to the master branch of your *origin* personal github repository with

    git push origin master

After this, both the local copy on your hard drive and your copy on [github.com](http://github.com) will be up to date with the official release.

Troubleshooting: pushing your master branch to your *origin* personal github repository may throw the error "This repository is configured for Git LFS but 'git-lfs' was not found on your path. If you no longer wish to use Git LFS, remove this hook by deleting .git/hooks/pre-push." This .git directory can be found in the local directory of your repository (../fieldtrip/.git).

Working with remotes is explained in more detail in the [Git book](http://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes).

## Want more?

[github.com](http://github.com) offers lots of documentation. In particular, see the detailed instructions to [fork a repository](https://help.github.com/articles/fork-a-repo) and to [create a pull request](https://help.github.com/articles/using-pull-requests). If you plan to continue development, I suggest to set up your remotes with *origin* pointing to your personal remote repository and *upstream* pointing to [https://github.com/fieldtrip/fieldtrip](https://github.com/fieldtrip/fieldtrip), as described in [fork a repository](https://help.github.com/articles/fork-a-repo).
