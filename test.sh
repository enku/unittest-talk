#!/bin/sh

filename="$1"

while true
do 
    clear 
    python "${filename}" -v --failfast 
    inotifywait -q -e modify "${filename}"
done
