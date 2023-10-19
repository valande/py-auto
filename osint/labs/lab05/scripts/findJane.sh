#!/bin/bash

>./oldFiles.txt

files="$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)"
prefix="/home/student-00-d5d35fbcb3ed"

for item in $files; do
	#echo "Item is ${item}"
	if test -f ${prefix}${item}; then
		echo ${prefix}${item} >> ./oldFiles.txt
	fi
done

