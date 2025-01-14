import axios from 'axios';

const API_URL = 'http://localhost:8000/api/v1';

interface SummaryRequest {
    text: string;
}

interface SummaryResponse {
    summary: string;
}

const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    }
});

export const createSummary = async (text: string): Promise<SummaryResponse> => {
    try {
        const response = await api.post<SummaryResponse>('/summary', {
            text: text
        } as SummaryRequest);
        return response.data;
    } catch (error) {
        console.error('Error creating summary:', error);
        throw error;
    }
};

export const getSummary = async (id: number) => {
    try {
        const response = await axios.get(`${API_URL}/summaries/${id}/`);
        return response.data;
    } catch (error) {
        throw error;
    }
}; 