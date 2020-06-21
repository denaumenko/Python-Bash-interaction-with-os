#!/bin/bash
line="----------------------------------------------------------------------------------"
echo "Starting at: $(date)"; echo $line

echo "UPTIME"
uptime; echo $line

echo "FREE";free -h;echo $line

echo "WHO";who;echo

echo "Finishing at: $(date)"

echo *