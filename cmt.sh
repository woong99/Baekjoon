#!/bin/bash

echo -e "메세지를 입력하세요: "
read msg
git add .
git commit -m "$msg"
git push origin master
