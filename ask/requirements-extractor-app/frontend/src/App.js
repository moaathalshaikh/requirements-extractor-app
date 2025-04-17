import React, { useState } from 'react';
import './styles/App.css';
import Diagram from './components/Diagram';
import MarkdownOutput from './components/MarkdownOutput';
import { fetchRequirements } from './utils/api';

function App() {
    const [inputText, setInputText] = useState('');
    const [requirements, setRequirements] = useState(null);

    const handleInputChange = (event) => {
        setInputText(event.target.value);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const extractedRequirements = await fetchRequirements(inputText);
        setRequirements(extractedRequirements);
    };

    return (
        <div className="App">
            <h1>Requirements Extractor</h1>
            <form onSubmit={handleSubmit}>
                <textarea
                    value={inputText}
                    onChange={handleInputChange}
                    placeholder="Enter your text here..."
                    rows="10"
                    cols="50"
                />
                <button type="submit">Extract Requirements</button>
            </form>
            {requirements && (
                <div>
                    <MarkdownOutput requirements={requirements} />
                    <Diagram requirements={requirements} />
                </div>
            )}
        </div>
    );
}

export default App;