# [Hey](https://github.com/dotancohen/hey/)

Human-oriented UI for git.


## What is meant by "Human-oriented UI for git"?

Git is easy, right? No, actually, [git is](https://news.ycombinator.com/item?id=25121416) [hard](https://ohshitgit.com/). This application should make git more intuitive to use.


## Why the funny name?

If we transpose the keypresses of `git` on a QWERTY keyboard from the right hand to the left and vice versa, we get `hey`. Also, `hey` is an informal greeting in many languages, and this application is intended to be an informal interface to `git`.


## How does it work?

`hey` is just a Python wrapper for git, with more intuitive commands inspired by common git complaints.


## How do I use it?

As a git wrapper, all output created by `hey` comes directly from git:

```
$ hey status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

$ hey diff
diff --git a/README.md b/README.md
index c7d25f5..4250fda 100644
--- a/README.md
+++ b/README.md
@@ -1,4 +1,4 @@
-# Hey
+# [Hey](https://github.com/dotancohen/hey/)
```
