# What does this do
It create a 320x200 file from another file and convert the color for the resource to be used as is in game.

Current limitations:
- only square raws are well processed
- only one 'result template' a Ufopedia template which consist of a black 120x200 rectangle followed by the 200x200 resized raw.

# Installation
```shell
git clone openxcom-conversion
```

# Dependencies Installation
```shell
sudo apt update
sudo apt install imagemagick gimp
```

If the "process_image_to_resource" script is not allowed to run as executable you must change the permission.
in the same folder
```
sudo chmod +x process_image_to_resource.sh
```

# Setup

## Add color palettes to GIMP
- Open GIMP
- Edit > Preferences > Folder (at the bottom, clic to expand) > Palettes
- Click on add a new folder and add the repository "gimp_palettes" folder
- Alternatively you can copy paste the palettes files in any directory listed

## Add script to GIMP

- Edit > Preferences > Folder (at the bottom, clic to expand) > Scripts
- Click on add a new folder and add the repository "gimp_script" folder

## Examples Usage

### Create an ufopedia ready resource 
```shell
./process_image_to_resource.sh input.png XCOM-Ufopaedia output.png
```

### Batch process a directory
```shell
find /path/to/input/directory -name "*.png" -print0 | xargs -0 -I {} bash -c 'filename=$(basename "{}"); ./process_image_to_resource.sh "{}" "XCOM-Ufopaedia" "/path/to/output/directory/$filename"'
```

eg with the examples folders in the repository (keeps the original filenames for outputs)
```shell
find examples_raw -name "*.png" -print0 | xargs -0 -I {} bash -c 'filename=$(basename "{}"); ./process_image_to_resource.sh "{}" "XCOM-Ufopaedia" "examples_output/$filename"'
```
