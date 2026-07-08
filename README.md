<div align="center">

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║      ░█████╗░██╗░░░░░██████╗░██╗░░██╗░█████╗░                 ║
║      ██╔══██╗██║░░░░░██╔══██╗██║░░██║██╔══██╗                 ║
║      ███████║██║░░░░░██████╔╝███████║███████║                 ║
║      ██╔══██║██║░░░░░██╔═══╝░██╔══██║██╔══██║                 ║
║      ██║░░██║███████╗██║░░░░░██║░░██║██║░░██║                 ║
║      ╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝                 ║
║                                                               ║
║            C  R  E  W                                         ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

# 🤖 Autonomous Stock Research AI

LINK-: https://stock-crew-ai.vercel.app/


### *A multi-agent AI system that researches, analyzes, and recommends stocks — fully autonomously.*

<br/>

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-Latest-FF6B6B?style=for-the-badge&logo=robot&logoColor=white)](https://crewai.com)
[![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-F55036?style=for-the-badge&logo=lightning&logoColor=white)](https://groq.com)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-8B5CF6?style=for-the-badge)](CONTRIBUTING.md)

<br/>

> **"Give me 6 hours to chop down a tree and I will spend the first 4 sharpening the axe."**  
> *— Abraham Lincoln. This AI does both. In seconds.*

<br/>

[**🚀 Quick Start**](#-quick-start) • [**🧠 How It Works**](#-how-it-works) • [**📊 Sample Output**](#-sample-output) • [**🛠 Tech Stack**](#-tech-stack) • [**🤝 Contributing**](#-contributing)

</div>

---

## 🌟 What Is This?

**Alpha Crew** is a fully autonomous, multi-agent AI system that does what a team of Wall Street analysts does — in under 60 seconds.

It wakes up, **searches the web for today's trending stocks**, digs deep into fundamentals and technicals, debates the best pick, and hands you a **beautifully formatted PDF investment report** — all without you lifting a finger.

No hallucinations. No stale training data. **Real-time web search. Real analysis. Real output.**

```
You type: crewai run
AI does: Everything else.
You get:  A professional PDF investment report in your output/ folder.
```

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🔍 **Real-Time Research** | Agents use live web search (Serper API) to find today's trending stocks |
| 🧠 **Multi-Agent Intelligence** | 3 specialized AI agents collaborate — Researcher → Analyst → Report Writer |
| ⚡ **Blazing Fast** | Powered by Groq's LPU inference — fastest LLM inference on the planet |
| 📄 **PDF Reports** | Auto-generates a clean, professional investment report you can share |
| 🏗️ **Structured Output** | Pydantic models ensure clean, validated data passing between agents |
| 🔄 **Sequential Pipeline** | Each agent builds on the last — no information loss between steps |

---

## 🧠 How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                    ALPHA CREW PIPELINE                          │
└─────────────────────────────────────────────────────────────────┘

  🌐 LIVE WEB                                          📄 YOUR DESK
  ──────────                                          ────────────

  Today's News ──►  [AGENT 1]  ──►  [AGENT 2]  ──►  [AGENT 3]  ──► PDF Report
  Earnings Data     Researcher     Analyst          Report Writer
  Market Trends     Finds top      Deep dives       Picks the best
                    3-5 trending   into each        company with
                    companies      company          full justification

  ◄── All powered by LLaMA 3.3 70B on Groq LPU inference ──────────►
```

### The Three Agents

**🔎 Agent 1 — Stock Research Analyst**
> Scours the web right now. Finds companies making headlines today. Returns structured data with tickers, names, and trending reasons.

**📊 Agent 2 — Financial Analyst**
> Takes those companies and digs deeper. Market position, future outlook, investment potential. Sources everything from live web data.

**📝 Agent 3 — Report Generator**
> Synthesizes everything. Picks the single best investment opportunity. Writes a clear, justified recommendation with risk analysis.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- A [Groq API key](https://console.groq.com) (free)
- A [Serper API key](https://serper.dev) (free tier available)

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/Prateek13052003/autonomous-stock-research.git
cd autonomous-stock-research

# 2. Install uv (if you don't have it)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. Install dependencies
uv sync
uv add 'crewai[litellm]' reportlab crewai-tools
```

### Configuration

```bash
# Create your .env file
cp .env.example .env
```

Open `.env` and fill in your keys:

```env
MODEL=groq/llama-3.3-70b-versatile
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

### Run

```bash
crewai run
```

That's it. Check the `output/` folder for your PDF. ☕

---

## 📊 Sample Output

```
╭──────────────────────────────────────────────────────╮
│              📈 Stock Investment Report               │
│         Generated on April 05, 2026 at 11:34 AM      │
╰──────────────────────────────────────────────────────╯

After real-time research across 5 trending companies...

🏆 FINAL RECOMMENDATION: NVIDIA (NVDA)

  ✅ Strong Buy consensus from 38 Wall Street analysts
  ✅ ~50% upside to average price target of $265.97
  ✅ Data center revenue growing 80-90% CAGR through 2027
  ✅ Dominant position in AI infrastructure globally

  ⚠️  Risk: China export restrictions, macro volatility
  ⚠️  Current price: $177 — down from 52-week high of $212
```

---

## 🛠 Tech Stack

```
┌────────────────┬────────────────────────────────────────────┐
│ Layer          │ Technology                                 │
├────────────────┼────────────────────────────────────────────┤
│ Agent Framework│ CrewAI — multi-agent orchestration         │
│ LLM            │ LLaMA 3.3 70B via Groq LPU inference       │
│ Web Search     │ Serper Dev API — real-time Google search   │
│ PDF Generation │ ReportLab — professional PDF output        │
│ Data Validation│ Pydantic v2 — structured agent outputs     │
│ Package Manager│ uv — blazing fast Python package manager   │
│ Language       │ Python 3.11+                               │
└────────────────┴────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
autonomous-stock-research/
│
├── src/stock/
│   ├── config/
│   │   ├── agents.yaml          # Agent roles, goals, backstories
│   │   └── tasks.yaml           # Task descriptions and expectations
│   │
│   ├── crew.py                  # Agent & task definitions + Crew assembly
│   └── main.py                  # Entry point + PDF generation
│
├── output/                      # Generated PDF reports land here
├── pyproject.toml               # Project metadata & dependencies
├── .env.example                 # Environment variable template
└── README.md                    # You are here 👋
```

---

## 🔧 Customization

**Change the sector being analyzed:**
```python
# main.py
inputs = {
    'sector': 'Healthcare',  # Try: 'Energy', 'Finance', 'Healthcare', 'Crypto'
    'current_date': str(datetime.now())
}
```

**Add more agents** (e.g. a Risk Analyst):
```python
# crew.py
@agent
def risk_analyst(self) -> Agent:
    return Agent(
        config=self.agents_config['risk_analyst'],
        tools=[SerperDevTool()],
        verbose=True
    )
```

**Change the LLM** (works with any LiteLLM-supported model):
```env
MODEL=anthropic/claude-3-5-sonnet-20241022
MODEL=openai/gpt-4o
MODEL=groq/llama-3.3-70b-versatile
```

---

## 🗺️ Roadmap

- [ ] 🌐 Web dashboard to view reports in browser
- [ ] 📧 Auto-email report on schedule (daily/weekly)
- [ ] 📈 Add historical backtesting agent
- [ ] 💹 Integrate Yahoo Finance API for live price data
- [ ] 🐳 Docker support for one-command deployment
- [ ] 📱 Telegram/WhatsApp bot integration

---

## 🤝 Contributing

Contributions are what make the open source community incredible.

```bash
# Fork → Clone → Branch → Code → PR

git checkout -b feature/your-amazing-feature
git commit -m "feat: add something incredible"
git push origin feature/your-amazing-feature
```

Then open a Pull Request. All PRs welcome — big or small.

---

## 👨‍💻 Author

**Prateek Choudhary**

[![GitHub](https://img.shields.io/badge/GitHub-Prateek13052003-181717?style=for-the-badge&logo=github)](https://github.com/Prateek13052003)

---

## ⚠️ Disclaimer

> This project is for **educational and research purposes only**.  
> It is **not financial advice**. Always do your own research before investing.  
> Past performance of any AI recommendation does not guarantee future results.

---

<div align="center">

**If this project helped you, drop a ⭐ — it means the world.**

*Built with 🤖 AI, ☕ coffee, and an unhealthy obsession with the stock market.*

</div>
