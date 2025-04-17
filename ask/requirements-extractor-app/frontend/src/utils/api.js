import axios from 'axios';

const API_URL = 'http://localhost:5000/api/extract-requirements';

export const extractRequirements = async (inputText) => {
    try {
        const response = await axios.post(API_URL, { text: inputText });
        return response.data;
    } catch (error) {
        console.error('Error extracting requirements:', error);
        throw error;
    }
};