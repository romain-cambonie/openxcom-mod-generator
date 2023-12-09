#!/bin/bash

# Define the source and destination directories
DIST_DIRECTORY="/home/yandros/workspace/openxcom/openxcom-generator/dist"
SOURCES_DEV_DIRECTORY="/home/yandros/workspace/openxcom/openxcom-generator/src"
MOD_FILES_DEV_DIRECTORY="/home/yandros/workspace/openxcom/openxcom-generator/data/TheCrew"
MOD_FILES_INSTALLATION_DIRECTORY="/home/yandros/Games/OpenXcom/share/openxcom/user/mods/TheCrew"

# Release executable and copy to data mod files
poetry run pyinstaller --onefile "$SOURCES_DEV_DIRECTORY/openxcomgenerator/main.py"
cp "$DIST_DIRECTORY/main" "$MOD_FILES_DEV_DIRECTORY/Bin/main"
chmod +x "$MOD_FILES_DEV_DIRECTORY/Bin/main"

# Copy script to data mod files
cp "$SOURCES_DEV_DIRECTORY/openxcomgenerator/main.py" "$MOD_FILES_DEV_DIRECTORY/Scripts/main.py"

# Replace files in installed game directory for quick testing
cp -r "$MOD_FILES_DEV_DIRECTORY/"* "$MOD_FILES_INSTALLATION_DIRECTORY/"
