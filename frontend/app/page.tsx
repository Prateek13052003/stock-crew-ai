"use client";

import { useState } from "react";
import Navbar from "@/components/Navbar";
import Hero from "@/components/Hero";
import SectorGrid from "@/components/SectorGrid";
import api, { downloadPDF } from "@/services/api";

import { AnalyzeResponse } from "@/types/stock";

export default function Home() {
  const [selectedSector, setSelectedSector] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<AnalyzeResponse | null>(null);

  const analyzeSector = async () => {
    if (!selectedSector) {
      alert("Please select a sector.");
      return;
    }

    try {
      setLoading(true);

      const response = await api.post<AnalyzeResponse>("/analyze", {
        sector: selectedSector,
      });

      setResult(response.data);
    } catch (err) {
      console.error(err);
      alert("Analysis failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <Navbar />

      <div className="max-w-7xl mx-auto px-6">
        <Hero />

        <SectorGrid
          selected={selectedSector}
          onSelect={setSelectedSector}
        />

        <div className="mt-10 flex justify-center">
          <button
            onClick={analyzeSector}
            disabled={loading}
            className="rounded-xl bg-blue-600 hover:bg-blue-700 px-8 py-4 font-semibold transition"
          >
            {loading ? "Analyzing..." : "Analyze Sector"}
          </button>
        </div>

        {loading && (
          <div className="mt-10 text-center text-lg">
            🤖 AI Agents are analyzing the sector...
          </div>
        )}

        {result && (
          <div className="mt-12 rounded-2xl bg-slate-900 border border-slate-700 p-8">

            <div className="flex justify-between mb-8">
              <div>
                <h2 className="text-3xl font-bold">
                  {result.sector} Report
                </h2>

                <p className="text-slate-400">
                  Generated on{" "}
                  {new Date(result.generated_at).toLocaleString()}
                </p>
              </div>

              <div className="text-right">
                <p className="text-slate-400">Execution Time</p>

                <h3 className="text-green-400 text-2xl font-bold">
                  {result.execution_time_seconds}s
                </h3>
              </div>
            </div>

            <div className="space-y-6">

              <div>
                <h3 className="text-xl font-semibold text-blue-400">
                  Recommended Company
                </h3>
                <p className="text-2xl font-bold">
                  {result.analysis.company_name} ({result.analysis.ticker})
                </p>
              </div>

              <div>
                <h3 className="text-xl font-semibold text-blue-400">
                  Recommendation
                </h3>

                <p className="leading-8 text-slate-300">
                  {result.analysis.recommendation_reason}
                </p>
              </div>

              <div>
                <h3 className="text-xl font-semibold text-blue-400">
                  Confidence Score
                </h3>

                <p className="text-green-400 text-3xl font-bold">
                  {result.analysis.confidence_score}/10
                </p>
              </div>
              <div>
                <h3 className="text-xl font-semibold text-red-400">
                  Risks
                </h3>

                <ul className="list-disc ml-6 mt-3 space-y-2">
                  {result.analysis.risks.map((risk: string, index: number) => (
                    <li key={index}>{risk}</li>
                  ))}
                </ul>

                <div className="mt-10 flex justify-center">
                  <button
                    onClick={downloadPDF}
                    className="rounded-xl bg-green-600 hover:bg-green-700 px-8 py-4 text-lg font-semibold transition-all duration-300 shadow-lg hover:scale-105"
                  >
                    📄 Download PDF Report
                  </button>
                </div>
              </div>

            </div>

          </div>
        )}
      </div>
    </main>
  );
}