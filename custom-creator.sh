#!/bin/bash
echo "Starting file generation..."


for var in "$@"
do
    cp $HOME/.config/competitive-template.cpp ./$var.cpp
    echo "Created problem $var.cpp"
done

echo "The problems have been successfully created"
