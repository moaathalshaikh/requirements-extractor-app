def extract_requirements(text):
    # This function interacts with the OpenAI GPT-4 API to extract functional and non-functional requirements
    import openai

    # Set up your OpenAI API key
    openai.api_key = 'your-api-key-here'

    # Define the prompt for the GPT-4 model
    prompt = f"Extract functional and non-functional requirements from the following text:\n{text}"

    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the response text
    requirements = response['choices'][0]['message']['content']
    return requirements

def format_requirements(requirements):
    # This function formats the extracted requirements into Markdown
    markdown_output = "# Extracted Requirements\n\n"
    markdown_output += requirements.replace('\n', '\n- ')
    return markdown_output

def main():
    # Example usage
    input_text = "The system should allow users to log in and manage their profiles."
    extracted_requirements = extract_requirements(input_text)
    markdown = format_requirements(extracted_requirements)
    print(markdown)

if __name__ == "__main__":
    main()