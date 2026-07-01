export interface Analysis {
    company_name: string;
    ticker: string;
    recommendation_reason: string;
    confidence_score: number;
    risks: string[];
    sources: any[];
}

export interface AnalyzeResponse {
    success: boolean;
    sector: string;
    generated_at: string;
    execution_time_seconds: number;
    analysis: Analysis;
}