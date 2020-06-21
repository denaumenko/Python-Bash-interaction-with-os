#!/bin/bash

for (( i = 0; i < 10; i++ )); do
    echo $i;
done


for file in *.txt; do
  name=$(basename "$file" .txt)
  mv "$file" "$name.html"
done