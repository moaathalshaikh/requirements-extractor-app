// This file contains JavaScript code for client-side functionality, such as handling user interactions and making API calls to the backend.

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('requirement-form');
    const outputDiv = document.getElementById('output');
    
    form.addEventListener('submit', async function(event) {
        event.preventDefault();
        
        const inputText = document.getElementById('input-text').value;
        
        try {
            const response = await fetch('/extract-requirements', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: inputText }),
            });
            
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            
            const data = await response.json();
            outputDiv.innerHTML = `
                <h3>Extracted Requirements</h3>
                <pre>${data.markdown}</pre>
                <div id="diagram-container">${data.diagram}</div>
            `;
        } catch (error) {
            outputDiv.innerHTML = `<p>Error: ${error.message}</p>`;
        }
    });
});