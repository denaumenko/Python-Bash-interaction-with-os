#!/bin/bash

n=1
while [ $n -le 5 ] && [ $n -ge 0 ]; do
  echo "Iteration number $n"
  ((n+=1))
done