"use client";

import { TrendingUp } from "lucide-react";

export default function Navbar() {
    return (
        <nav className="sticky top-0 z-50 backdrop-blur-lg bg-slate-950/80 border-b border-slate-800">
            <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">

                <div className="flex items-center gap-3">
                    <div className="p-2 rounded-xl bg-blue-600">
                        <TrendingUp size={24} className="text-white" />
                    </div>

                    <div>
                        <h1 className="font-bold text-xl">
                            Alpha Crew AI
                        </h1>

                        <p className="text-xs text-slate-400">
                            Multi-Agent Stock Research
                        </p>
                    </div>
                </div>

            </div>
        </nav>
    );
}