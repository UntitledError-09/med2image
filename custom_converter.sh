#!/bin/bash

cd /mnt/e/ShareFolder/Datasets/PPMI_TI_3D_ControlOnly

no_of_folders=$(ls | wc -l)
echo "$no_of_folders folders found"

for iter in $(ls)
do

    target="$(pwd)/$iter"
    echo "checking $target..."
    while [[ $target != *.nii ]]
    do
        if [[ $(ls $target | wc -l) -eq 0 ]]; then
            break
        fi
        target="$target/$(ls $target)"
    done
    echo "$target found!"
done