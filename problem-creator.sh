#!/bin/bash

echo "Welcome to problem creator, $(whoami)!"
echo "Input the amount of problems to get: "

letters=('A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'J' 'K' 'L')

read amount

if [ $amount -gt 13 ]
then
    echo "err: The amount of problems is too large!"
    exit 0
else
    echo "Generate $amount problems? [Y/n]"
fi

read confirmation

if [ $confirmation != "Y" ]
then
    echo "Nothing has been done."
else
    echo "Starting the generation..."
fi

x=0
while [ $x -le $amount ]
do
    cp $HOME/.config/competitive-template.cpp ./${letters[$x]}.cpp
    echo "Created problem ${letters[$x]}"
    x=$(( $x + 1 ))
done

echo "The problems have been successfully created"
