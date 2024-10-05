import requests
import os
import subprocess
import json

def generate_instructions(prompt):
    try:
        # Replace with your Ollama endpoint
        api_url = "http://localhost:11434/api/generate"
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "prompt": f"You are a blackbelt Windows sysadmin. Translate the user's request into pure Windows command prompt batch instructions. Do not use any third-party software. Make sure the commands are complete and can be executed step-by-step without errors. Provide only the command(s) to: {prompt}, do not write anything else but the command prompt batch instructions. Start from the current directory.",
            "model": "llama3.2"
        }

        response = requests.post(api_url, json=data, headers=headers, stream=True)

        if response.status_code == 200:
            full_response = ""
            for line in response.iter_lines():
                if line:
                    try:
                        json_line = json.loads(line.decode('utf-8'))
                        if "response" in json_line:
                            full_response += json_line["response"]
                    except json.JSONDecodeError as e:
                        print(f"JSON decoding error: {e}")
                        continue
            return full_response.strip()
        else:
            print(f"Failed to generate instructions. Status code: {response.status_code}")
            return ""

    except Exception as e:
        print(f"An error occurred while generating instructions: {e}")
        return ""

def execute_instructions(instructions, retry_count=0, max_retries=2):
    try:
        # Create a batch file with the instructions
        bat_file_path = "instructions.bat"
        with open(bat_file_path, 'w') as bat_file:
            bat_file.write(instructions)
        
        # Execute the batch file securely by avoiding shell=True
        print(f"Executing batch file: {bat_file_path}")
        subprocess.run(["cmd.exe", "/c", bat_file_path], check=True)
        print("All instructions executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing instructions: {e}")
        if retry_count < max_retries:
            error_message = str(e)
            # Send the error details back to Ollama to generate a new batch file
            retry_prompt = f"The following error occurred while executing the batch file: {error_message}. Please correct the batch script based on this error. The original instructions were: {instructions}"
            corrected_instructions = generate_instructions(retry_prompt)
            if corrected_instructions:
                print("Retrying with corrected instructions...")
                execute_instructions(corrected_instructions, retry_count=retry_count + 1, max_retries=max_retries)
    finally:
        # Clean up the batch file
        if os.path.exists(bat_file_path):
            try:
                os.remove(bat_file_path)
            except OSError as e:
                print(f"Error deleting the batch file: {e}")

def main():
    while True:
        user_input = input("Please enter your request (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        
        instructions = generate_instructions(user_input)
        
        if instructions:
            execute_instructions(instructions)

if __name__ == "__main__":
    main()