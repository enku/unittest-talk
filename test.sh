#!/bin/sh

directory="$(dirname $0)"

while true
do 
    clear 
    python -m unittest discover "${directory}"/tests --failfast 
    inotifywait -q -e modify "${directory}" "${directory}"/tests
done
