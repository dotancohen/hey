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

$ hey add README.md

$ hey commit -m "Update readme"
[master d23f976] Update readme
 1 file changed, 32 insertions(+), 1 deletion(-)

$ hey push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 983 bytes | 983.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:dotancohen/hey.git
   43dd955..d23f976  master -> master
```
