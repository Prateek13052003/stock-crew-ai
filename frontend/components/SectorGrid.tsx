"use client";

import { motion } from "framer-motion";
import {
    Cpu,
    HeartPulse,
    Landmark,
    GraduationCap,
    ShoppingCart,
    Building2,
    FlaskConical,
    Factory,
    Plane,
    Leaf,
    Car,
    Bitcoin,
} from "lucide-react";

const sectors = [
    { name: "Technology", icon: Cpu },
    { name: "Healthcare", icon: HeartPulse },
    { name: "Banking", icon: Landmark },
    { name: "Education", icon: GraduationCap },
    { name: "E-Commerce", icon: ShoppingCart },
    { name: "Real Estate", icon: Building2 },
    { name: "Pharmaceutical", icon: FlaskConical },
    { name: "Manufacturing", icon: Factory },
    { name: "Travel", icon: Plane },
    { name: "Energy", icon: Leaf },
    { name: "Automobile", icon: Car },
    { name: "Cryptocurrency", icon: Bitcoin },
];

interface Props {
    selected: string;
    onSelect: (sector: string) => void;
}

export default function SectorGrid({
    selected,
    onSelect,
}: Props) {
    return (
        <section className="mt-20">

            <div className="text-center mb-10">
                <h2 className="text-4xl font-bold">
                    Choose Investment Sector
                </h2>

                <p className="text-slate-400 mt-3">
                    Select a sector for comprehensive AI-powered investment analysis.
                </p>
            </div>

            <div className="grid gap-6 md:grid-cols-3 lg:grid-cols-4">

                {sectors.map((sector) => {
                    const Icon = sector.icon;

                    return (
                        <motion.button
                            whileHover={{
                                scale: 1.04,
                            }}
                            whileTap={{
                                scale: 0.97,
                            }}
                            key={sector.name}
                            onClick={() => onSelect(sector.name)}
                            className={`rounded-2xl border p-8 transition-all duration-300

              ${selected === sector.name
                                    ? "border-blue-500 bg-blue-600/20"
                                    : "border-slate-800 bg-slate-900 hover:border-blue-500"
                                }
              
              `}
                        >
                            <Icon
                                size={42}
                                className="mx-auto text-blue-400"
                            />

                            <h3 className="mt-5 font-semibold text-lg">
                                {sector.name}
                            </h3>
                        </motion.button>
                    );
                })}

            </div>
        </section>
    );
}