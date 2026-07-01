"use client";

import { motion } from "framer-motion";
import { BrainCircuit, LineChart, Sparkles } from "lucide-react";

export default function Hero() {
    return (
        <section className="py-20">

            <motion.div
                initial={{ opacity: 0, y: 40 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6 }}
                className="text-center"
            >
                <div className="inline-flex items-center gap-2 rounded-full border border-blue-500/30 bg-blue-500/10 px-4 py-2 text-blue-400 text-sm">
                    <Sparkles size={16} />
                    Multi-Agent Stock Intelligence
                </div>

                <h1 className="mt-8 text-6xl font-extrabold leading-tight">
                    Alpha Crew
                    <span className="block bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
                        AI Stock Analyst
                    </span>
                </h1>

                <p className="mx-auto mt-8 max-w-3xl text-lg text-slate-400 leading-8">
                    Autonomous AI agents perform institutional-grade market research,
                    analyze financial statements, evaluate risks, compare competitors,
                    and generate professional investment reports in minutes.
                </p>
            </motion.div>

            <div className="mt-16 grid gap-6 md:grid-cols-3">

                <div className="rounded-2xl border border-slate-800 bg-slate-900 p-8">
                    <BrainCircuit className="text-blue-500 mb-4" size={34} />

                    <h3 className="text-xl font-bold">
                        Multi-Agent Reasoning
                    </h3>

                    <p className="mt-3 text-slate-400">
                        Specialized AI agents collaborate like an institutional research team.
                    </p>
                </div>

                <div className="rounded-2xl border border-slate-800 bg-slate-900 p-8">
                    <LineChart className="text-green-500 mb-4" size={34} />

                    <h3 className="text-xl font-bold">
                        Investment Insights
                    </h3>

                    <p className="mt-3 text-slate-400">
                        Analyze sectors, identify opportunities, and assess investment risks.
                    </p>
                </div>

                <div className="rounded-2xl border border-slate-800 bg-slate-900 p-8">
                    <Sparkles className="text-purple-500 mb-4" size={34} />

                    <h3 className="text-xl font-bold">
                        Executive Reports
                    </h3>

                    <p className="mt-3 text-slate-400">
                        Download beautifully formatted PDF reports ready for investors.
                    </p>
                </div>

            </div>

        </section>
    );
}