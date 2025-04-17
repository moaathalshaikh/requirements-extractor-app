def preprocess_text(text):
    # Function to preprocess input text for extraction
    # This can include removing unnecessary whitespace, special characters, etc.
    return ' '.join(text.split())

def format_requirements(requirements):
    # Function to format extracted requirements into a Markdown-friendly format
    formatted = ""
    for req in requirements:
        formatted += f"- {req}\n"
    return formatted

def generate_diagram_data(requirements):
    # Function to prepare data for visualizing requirements in a diagram
    # This is a placeholder for actual diagram data generation logic
    return {
        "nodes": [{"id": i, "label": req} for i, req in enumerate(requirements)],
        "edges": []  # Define edges based on relationships if needed
    }