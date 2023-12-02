#!/bin/bash

# Check the input arguments
if [ "$#" -ne 3 ]; then
    echo "Usage: ./process_image.sh <input_image> <palette_name_in_gimp> <output_image>"
    echo "Eg: ./process_image.sh source/my-raw.png XCOM-Ufopaedia output/my-resource-ready-file.png"
    exit 1
fi

# Assign arguments to variables
input_image="$1"
palette_name_in_gimp="$2"
output_image="$3"

# Step 1: Append a black rectangle to the left of the resized image
convert \
\( -size 120x200 xc:black \) \
\( "$input_image" -resize 200x200 -depth 8 \) \
+append intermediate_resized.png

# Step 2: Remap the colors of the intermediate image to the provided palette
gimp -i -b "(script-fu-indexed \"intermediate_resized.png\" \"$output_image\" \"$palette_name_in_gimp\" 256)" -b "(gimp-quit 0)"

# Clean up the intermediate image
rm intermediate_resized.png

echo "The image has been processed and saved as $output_image"

