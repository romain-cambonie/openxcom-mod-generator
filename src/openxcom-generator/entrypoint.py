import yaml
import sys

def update_yaml_files(title, content, resource_file_path):
    # Define the filenames
    en_us_file = 'en-US.yml'
    mod_rul_file = 'mod.rul'

    # Load en-US.yml
    with open(en_us_file, 'r') as file:
        en_us_data = yaml.safe_load(file)

    # Load mod.rul
    with open(mod_rul_file, 'r') as file:
        mod_rul_data = yaml.safe_load(file)

    # Generate IDs
    base_id = title.replace(' ', '_').upper()
    text_id = f'STR_{base_id}_UFOPEDIA'
    image_id = base_id

    # Update en-US.yml
    en_us_data['en-US'][f'STR_{base_id}'] = title
    en_us_data['en-US'][text_id] = content

    # Update mod.rul
    mod_rul_data['ufopaedia'].append({
        'id': f'STR_{base_id}',
        'type_id': 7,
        'section': 'STR_UFO_COMPONENTS',
        'text': text_id,
        'image_id': image_id,
        'text_width': 140
    })
    mod_rul_data['extraSprites'].append({
        'typeSingle': image_id,
        'fileSingle': resource_file_path
    })

    # Write updated data back to en-US.yml
    with open(en_us_file, 'w') as file:
        yaml.dump(en_us_data, file)

    # Write updated data back to mod.rul
    with open(mod_rul_file, 'w') as file:
        yaml.dump(mod_rul_data, file)

# Read arguments from command line
if len(sys.argv) != 4:
    print("Usage: python update_yaml.py <title> <content> <resource_file_path>")
else:
    update_yaml_files(sys.argv[1], sys.argv[2], sys.argv[3])
