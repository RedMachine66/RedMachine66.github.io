import openai
import requests
import datetime
import os

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def generate_and_save_image(input_file_path, output_directory):
    openai.api_key = read_file('openai-key.key')

    try:
        with open(input_file_path, 'r') as file:
            # Skip the first line if it's "Prompt:" and then read the rest of the file
            lines = file.readlines()
            prompt_text = ' '.join(lines[1:]).strip() if lines[0].startswith("Prompt:") else ' '.join(lines).strip()

        # Generate a valid filename
        sanitized_prompt = ''.join(char for char in prompt_text if char.isalnum() or char in [' ', '_']).strip()
        first_three_words = '_'.join(sanitized_prompt.split()[:3])
        current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file_name = f"{first_three_words}_{current_datetime}.png"
        output_file_path = os.path.join(output_directory, output_file_name)

        generate_image_from_text(prompt_text, output_file_path)
        print(f"Image generated based on the text in '{input_file_path}' and saved as '{output_file_name}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
    except Exception as e:
        print(f"Error occurred: {e}")

def generate_image_from_text(prompt_text, output_file):
    try:
        response = openai.Image.create(
            model="dall-e-3",
            prompt=prompt_text,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response['data'][0]['url']

        image_data = requests.get(image_url).content
        with open(output_file, 'wb') as image_file:
            image_file.write(image_data)

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file_path = "image_prompts/a_soap_product_6.txt"
output_directory = "desired_output_directory"
generate_and_save_image(input_file_path, output_directory)
