# BatchAssistant

BatchAssistant is a Python-based automation tool designed to generate and execute Windows command prompt batch instructions based on natural language requests. This tool is ideal for automating system administration tasks using simple text prompts, which are then interpreted by an AI model to create actionable batch scripts.

## Features
- Natural language processing to convert user requests into batch script commands.
- Automatic creation and execution of batch files based on user requests.
- Error handling and retry mechanism to correct and re-execute commands if an error occurs.

## Prerequisites
To ensure BatchAssistant works properly, you need to have **Ollama** installed and running locally. Ollama provides the AI model (e.g., `llama3.2`) used to interpret natural language requests and convert them into command prompt instructions.

## Installation
1. **Install Ollama**: Follow the [Ollama installation guide](https://ollama.com) to set up Ollama on your local machine.
2. **Clone the Repository**: Clone this GitHub repository to your local machine.
   ```bash
   git clone https://github.com/timetravel0/BatchAssistant.git
   cd batchgen-automator
   ```
## Usage
1. **Run Ollama**: Ensure Ollama is installed and running locally, accessible at `http://localhost:11434`.
2. **Start the Program**: Run the Python script.
   ```bash
   python BatchAss.py
   ```
3. **Enter Commands**: Provide natural language requests at the prompt to generate and execute batch files.
   ```
   Please enter your request (or type 'exit' to quit): create a folder named "test" and create a file inside called "example.txt" with current date and time
   ```

## Example
When you enter a request like:
```
create a folder named "test" and create a file inside called "example.txt" with current date and time
```
BatchGen Automator will generate a batch file with the appropriate commands, execute it, and automate the requested tasks.

## Error Handling
If an error occurs while executing the batch file, BatchGen Automator will attempt to correct the issue by sending the error details back to Ollama for correction. The updated batch script will then be retried up to 2 times.

## Security Considerations
Please be aware that executing commands via batch files can pose security risks, especially if the input is not sanitized properly. Ensure that your input is trusted to avoid executing malicious commands.

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests to improve the tool.

## License
This project is licensed under the MIT License.
