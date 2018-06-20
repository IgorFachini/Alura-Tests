#!/bin/bash
cd C:\Users\Cyber10\Desktop\dev\Scripts
echo %date% %time% >> log.txt
git commit -a -m "teste1"
echo %date% %time% >> log.txt
git commit -a -m "teste2"
echo %date% %time% >> log.txt
git commit -a -m "teste3"
echo %date% %time% >> log.txt
git commit -a -m "teste4"

git status
git push origin master
echo "Deu"