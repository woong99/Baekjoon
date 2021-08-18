#!/bin/bash
msg="$(date +%y).$(date +%m).$(date +%d) Baekjoon solution"
git add .
git commit -m "$msg"
git push origin master
