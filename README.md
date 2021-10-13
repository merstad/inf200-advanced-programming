# INF200 Course Materials

This repository provides teaching materials for INF200 at NMBU in the academic year 2021/22.

From week 41 onward, all teaching material except for videos will only be made available via this repository.

## How to get this repository onto your computer

You only need to perform the following steps once.

1. Open Anaconda Powershell Prompt (Windows) or Terminal (macOS, Linux).
1. Activate the `inf200` conda environment.
1. Use `cd` to navigate to the directory in which you keep your INF200 materials.
1. Run
```sh
git clone https://gitlab.com/nmbu.no/emner/inf200/h2021/inf200-course-materials.git
```

You should now have a directory `inf200-course-materials` directory containing all currently available materials.

## Keeping course materials up to date

To keep the course material up to date on your computer, proceed as follows:

1. Open Anaconda Powershell Prompt (Windows) or Terminal (macOS, Linux).
1. Activate the `inf200` conda environment.
1. Use `cd` to navigate *into* the `inf200-course-materials` folder.
1. Run
```sh
git pull
```

If you receive an error message, it is probably because you made changes to files in this directory that "collide" with updates I made to the same files. In that case, you can clean up you repository by running

```sh
git reset --hard
```

**This will delete all changes you have made to files in the course materials repository!**

## Working with the course materials

To avoid the risk of "collisions" between changes you make to files in the course materials repository and changes I may make during or after the lecture, **you should only work on copies of files**, either inside the `inf200-course-materials` directory or outside.

## Alternative access to material in the repository

You can always access the material in the course material repository through the GitLab website at https://gitlab.com/nmbu.no/emner/inf200/h2021/inf200-course-materials.

If you have any questions, please contact your TA.
