import os
import openai

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def generate_unique_filename(base_path, prefix):
    counter = 0
    while True:
        unique_file_name = f"{prefix}_{counter}.txt"
        if not os.path.exists(os.path.join(base_path, unique_file_name)):
            return unique_file_name
        counter += 1

def generate_response(config_file, message_file, output_folder='backup_output_folder'):
    # Load API key
    openai.api_key = read_file('openai-key.key')

    # Read the configuration and input files
    system_prompt = read_file(config_file)
    user_prompt = read_file(message_file)

    # Combine prompts
    prompt = f"{system_prompt}\n\n{user_prompt}"

    try:
        # Call to the OpenAI API for chat completions
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )

        # Generate a unique file name for the output
        first_three_words = '_'.join(user_prompt.split()[:3])
        output_file_name = generate_unique_filename(output_folder, first_three_words)

        # Write the response to the output file in the specified folder
        output_file_path = os.path.join(output_folder, output_file_name)
        write_file(output_file_path, response['choices'][0]['message']['content'].strip())

        # Return the name of the output file
        return output_file_name

    except Exception as e:
        print(f"An error occurred: {e}")
        return None  # Return None in case of an error

# if __name__ == "__main__":
#     # Example usage
#     generate_response('konfiguration.txt', 'input.txt')







# import sys, time, openai, os

# def read_file(file_path):
#     with open(file_path, 'r') as file:
#         return file.read()

# def write_file(file_path, content):
#     with open(file_path, 'w') as file:
#         file.write(content)

# def generate_unique_filename(base_path, prefix):
#     # Generate a unique file name using a timestamp
#     counter = 0
#     while True:
#         unique_file_name = f"{prefix}_{counter}.txt"
#         if not os.path.exists(os.path.join(base_path, unique_file_name)):
#             return unique_file_name
#         counter += 1

# def generate_response(config_file, message_file):
#     # Load API key
#     openai.api_key = read_file('openai-key.key')

#     # Read the configuration and input files
#     system_prompt = read_file(config_file)
#     user_prompt = read_file(message_file)

#     # Combine prompts
#     prompt = f"{system_prompt}\n\n{user_prompt}"

#     try:
#         # Call to the OpenAI API for chat completions
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": system_prompt},
#                 {"role": "user", "content": user_prompt}
#             ],
#             temperature=0.7,
#             max_tokens=500
#         )

#         # Generate a unique file name for the output
#         first_three_words = '_'.join(system_prompt.split()[:3])
#         output_file_name = generate_unique_filename('.', first_three_words)

#         # Write the response to the output file
#         write_file(output_file_name, response['choices'][0]['message']['content'].strip())

#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     # Example usage
#     generate_response('konfiguration.txt', 'input.txt')










# import sys, time, openai, os


# def read_file(file_path):
#     with open(file_path, 'r') as file:
#         return file.read()

# def write_file(file_path, content):
#     with open(file_path, 'w') as file:
#         file.write(content)

# def main():
#     # Load your API key from an environment variable or configuration file
#     openai.api_key = read_file('openai-key.key')

#     # Read the configuration and input files
#     system_prompt = read_file('konfiguration.txt')
#     user_prompt = read_file('input.txt')

#     # Combine prompts
#     prompt = f"{system_prompt}\n\n{user_prompt}"

#     try:
#         # Make a call to the OpenAI API for chat completions
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",  # or "text-davinci-003" for GPT-3.5
#             messages=[
#                 {"role": "system", "content": system_prompt},
#                 {"role": "user", "content": user_prompt}
#             ],
#             temperature=0.7,
#             max_tokens=500
#         )

#         # Write the response to the output file
#         write_file('output', response['choices'][0]['message']['content'].strip())

#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     main()