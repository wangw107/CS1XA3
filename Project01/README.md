# Project Analyze

## Summary

A simple script which can help you analyze your project directory and do variety kinds of common operations conveniently.

## Features

Checked for already done, unchecked for currently working on.

Click each entry to view description.
 - [x] [Friendly command line interface](#command-line-interface)
 - [x] [Generate merge log of repository](#merge-log-generation)
 - [x] [Count files of specific extensions](#file-type-count)
 - [x] [Delete untracked temporary files](#delete-untracked-temporary-files)
 - [ ] Collect all contents of file tagged with #TODO
 - [ ] Try to compile scripts and collect errors
 - [ ] Merge the last working version of a specific file to current branch

## Usage

> Copy the script to the root directory of your project and launch it.

### Command Line Interface

 - Upon launch of the script it will show you a menu of functions. Enter the index number of the function you want to run and press return to start a job.
 - After a job is finished, press any key to return to the menu, where you can start a new job.
 - In order to exit the script you can select "Exit" on the menu, or press Ctrl-C at any time (Not recommended).

### Merge Log Generation

 - Hashes of all commits that message contains "Merge" will be printed to screen, while being written to "merge.log" in the same directory as well.
 - The log file will be overwritten if there is already one.

### File Type Count

 - The script will search for files with these extensions:
     - HTML document (*.html)
     - JavaScript script (*.js)
     - CSS script (*.css)
     - Python script (*.py)
     - Haskell script (*.hs)
     - Bash script (*.sh)
 - The result will be printed to screen.
 - The script will search for files resursively.

### Delete Untracked Temporary Files
 - All file that's untracked by git and has *.tmp extension will be removed.
 - Names of file being removed will be printed to screen.


