from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv

try:
    from crewai.memory import LongTermMemory, ShortTermMemory, EntityMemory
except ImportError:
    LongTermMemory = None
    ShortTermMemory = None
    EntityMemory = None

class Source(BaseModel):
    source_name: str = Field(description="News source name")
    source_url: str = Field(description="Source URL")
    publication_date: str = Field(description="Publication date")


class TrendingCompany(BaseModel):
    name: str = Field(description="Company name")
    ticker: str = Field(description="Stock ticker symbol")
    reason: str = Field(description="Reason this company is trending")
    headline: str = Field(description="News headline")
    source: Source = Field(description="Supporting source")


class TrendingCompanyList(BaseModel):
    """List of multiple trending companies that are in the news"""
    companies: List[TrendingCompany] = Field(description="List of companies trending in the news")

class TrendingCompanyResearch(BaseModel):
    name: str = Field(description="Company name")

    ticker: str = Field(
        description="Stock ticker symbol"
    )

    revenue_summary: str = Field(
        description="Latest revenue performance and growth"
    )

    earnings_summary: str = Field(
        description="Latest earnings performance"
    )

    market_position: str = Field(
        description="Competitive position in the industry"
    )

    analyst_sentiment: str = Field(
        description="Analyst ratings and market sentiment"
    )

    growth_catalysts: List[str] = Field(
        description="Major growth drivers"
    )

    risks: List[str] = Field(
        description="Major investment risks"
    )

    future_outlook: str = Field(
        description="Future outlook"
    )

    investment_potential: str = Field(
        description="Overall investment assessment"
    )

    sources: List[Source] = Field(
        description="Supporting sources"
    )


class TrendingCompanyResearchList(BaseModel):
    """A list of detailed research on all the companies"""
    research_list: List[TrendingCompanyResearch] = Field(description="Comprehensive research on all trending companies")


class FinalRecommendation(BaseModel):
    company_name: str = Field(description="Recommended company")
    ticker: str = Field(description="Ticker symbol")
    recommendation_reason: str = Field(
        description="Why this company was selected"
    )
    confidence_score: int = Field(
        description="Confidence score from 1 to 10"
    )
    risks: List[str] = Field(
        description="Key investment risks"
    )
    sources: List[Source] = Field(
        description="Supporting sources"
    )


@CrewBase
class StockPicker():

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    llm = LLM(
    model="gemini/gemini-2.5-flash",
    temperature=0,
    max_tokens=400,
)


    # ── Agents ──────────────────────────────────────────────────────────────

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            llm=self.llm,
            tools=[SerperDevTool()],  # ✅ web search tool added here
            verbose=True,
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'],
            llm=self.llm,
            tools=[SerperDevTool()],  # analyst can also search for deeper research
            verbose=True,
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            llm=self.llm,
            verbose=True,
        )

    # ── Tasks ────────────────────────────────────────────────────────────────

    @task
    def find_trending_companies(self) -> Task:
        return Task(
            config=self.tasks_config['find_trending_companies'],
            output_pydantic=TrendingCompanyList
        )

    @task
    def research_trending_companies(self) -> Task:
        return Task(
            config=self.tasks_config['research_trending_companies'],
            output_pydantic=TrendingCompanyResearchList
        )

    @task
    def pick_best_company(self) -> Task:
        return Task(
            config=self.tasks_config['pick_best_company'],
            output_pydantic=FinalRecommendation
        )
        
    # ── Crew ─────────────────────────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the StockPicker crew"""
        return Crew(
            agents=[
                self.researcher(),
                self.analyst(),
                self.reporting_analyst()
            ],
            tasks=[
                self.find_trending_companies(),
                self.research_trending_companies(),
                self.pick_best_company()
            ],
            process=Process.sequential,
            verbose=True,
        )