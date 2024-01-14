from copy_agent_gpt_35_turbo_api import generate_response  # Replace with the actual name of your script
from image_agent_dalle_3_api import generate_and_save_image
import os, datetime

headline_copy_config = 'headline_copy_config.txt'
primary_copy_config = 'primary_copy_config.txt'
image_engineering_config = 'image_engineering_config.txt'
campaign_info = 'campaign_info.txt'

# Create folder for marketing content with timestamp in the name.
def create_unique_folder(base_path="."):
    # Get the current date and time in a specific format
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = f"content_{timestamp}"

    # Create the full path for the new folder
    full_path = os.path.join(base_path, folder_name)

    # Check if the folder already exists, although it's highly unlikely
    if not os.path.exists(full_path):
        os.makedirs(full_path)
        print(f"Folder created: {full_path}")
    else:
        print("A folder with this name already exists.")

    return full_path

# Example usage
folder_path = create_unique_folder()





# Call the function with the paths to your config and message files
# your_script_name.generate_response('path/to/config_file.txt', 'path/to/message_file.txt', 'path/to/output/folder)


# Headline generator
generate_response(headline_copy_config, campaign_info, folder_path)

# Primary copy generator
generate_response(primary_copy_config, campaign_info, folder_path)

# Image generator + prompt generation
image_prompt = generate_response(image_engineering_config, campaign_info, 'image_prompts')
if image_prompt:
    print(f"Output file generated: {image_prompt}")
else:
    print("Error generating output file.")

generate_and_save_image('image_prompts/'+image_prompt, folder_path)