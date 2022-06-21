#!/bin/bash

PREFIX=475

listDir=$(ls)

for entry in $listDir
do
  ext=$(echo $entry | cut -d"." -f2)
  if [[ "$ext" == 'logs' ]]
  then
    num=${entry%_*}
    num=${num%_*}
    num=${num%_*}
    newNum=$((num-PREFIX))
    fileName=${entry#*_}
    echo "[i] num: $num, newNum: $newNum, fileName: $fileName"
    mv "./$entry" "./${newNum}_${fileName}"
  fi
done