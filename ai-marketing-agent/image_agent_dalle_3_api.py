import openai
import requests
import datetime

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def generate_and_save_image(input_file_path, output_directory):
    # Set your OpenAI API key
    openai.api_key = read_file('openai-key.key')

    try:
        with open(input_file_path, 'r') as file:
            prompt_text = file.read().strip()

        # Generate the output file name based on the first three words and current date-time
        first_three_words = '_'.join(prompt_text.split()[:3])
        current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file_name = f"{first_three_words}_{current_datetime}.png"
        output_file_path = f"{output_directory}/{output_file_name}"

        # Generate image based on the text and save it
        generate_image_from_text(prompt_text, output_file_path)
        print(f"Image generated based on the text in '{input_file_path}' and saved as '{output_file_name}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
    except Exception as e:
        print(f"Error occurred: {e}")

def generate_image_from_text(prompt_text, output_file):
    try:
        # Generate image based on the prompt
        response = openai.Image.create(
            model="dall-e-3",
            prompt=prompt_text,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        # Get the URL of the generated image
        image_url = response['data'][0]['url']

        # Download and save the image from the URL
        image_data = requests.get(image_url).content
        with open(output_file, 'wb') as image_file:
            image_file.write(image_data)

    except Exception as e:
        print(f"An error occurred: {e}")










# # image_generator.py
# import openai
# import requests

# def read_file(file_path):
#     with open(file_path, 'r') as file:
#         return file.read()

# # Set your OpenAI API key
# openai.api_key = read_file('openai-key.key')

# # Function to generate an image based on text prompt and save it to a file
# def generate_image_from_text(prompt_text, output_file):
#     try:
#         # Generate image based on the prompt
#         response = openai.Image.create(
#             model="dall-e-3",
#             prompt=prompt_text,
#             size="1024x1024",
#             quality="standard",
#             n=1,
#         )

#         # Get the URL of the generated image
#         image_url = response['data'][0]['url']

#         # Download and save the image from the URL
#         image_data = requests.get(image_url).content
#         with open(output_file, 'wb') as image_file:
#             image_file.write(image_data)

#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Read the text from the input file
# input_file = "input.txt"  # Replace with your input file name

# try:
#     with open(input_file, 'r') as file:
#         prompt_text = file.read().strip()
#         # Generate image based on the text and save it to 'generated_image.png'
#         output_image_file = "generated_image.png"  # Replace with your desired output file name
#         generate_image_from_text(prompt_text, output_image_file)
#         print(f"Image generated based on the text in '{input_file}' and saved as '{output_image_file}'.")

# except FileNotFoundError:
#     print(f"Error: File '{input_file}' not found.")
# except Exception as e:
#     print(f"Error occurred: {e}")