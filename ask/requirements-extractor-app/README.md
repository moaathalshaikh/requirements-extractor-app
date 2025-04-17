# Requirements Extractor App

This project is a web application that extracts functional and non-functional requirements from text using OpenAI's GPT-4. It consists of a Flask backend and a React frontend, providing a user-friendly interface for input and output.

## Project Structure

```
requirements-extractor-app
├── backend
│   ├── app.py
│   ├── requirements_extractor
│   │   ├── __init__.py
│   │   ├── extractor.py
│   │   └── utils.py
│   ├── templates
│   │   └── index.html
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── scripts.js
│   ├── tests
│   │   ├── test_extractor.py
│   │   └── test_app.py
│   └── requirements.txt
├── frontend
│   ├── src
│   │   ├── App.js
│   │   ├── components
│   │   │   ├── Diagram.js
│   │   │   └── MarkdownOutput.js
│   │   ├── styles
│   │   │   └── App.css
│   │   └── utils
│   │       └── api.js
│   ├── public
│   │   └── index.html
│   ├── package.json
│   └── webpack.config.js
├── README.md
└── .gitignore
```

## Features

- **Requirement Extraction**: Utilizes GPT-4 to extract both functional and non-functional requirements from user-provided text.
- **Markdown Output**: Displays extracted requirements in a Markdown format for easy readability.
- **Visual Diagram**: Provides a visual representation of the extracted requirements.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd requirements-extractor-app
   ```

2. Set up the backend:
   - Navigate to the `backend` directory.
   - Install the required Python packages:
     ```
     pip install -r requirements.txt
     ```

3. Set up the frontend:
   - Navigate to the `frontend` directory.
   - Install the required Node.js packages:
     ```
     npm install
     ```

## Usage

1. Start the backend server:
   ```
   python app.py
   ```

2. Start the frontend application:
   ```
   npm start
   ```

3. Open your browser and navigate to `http://localhost:3000` to access the application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.