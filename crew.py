from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from pydantic import BaseModel, Field
from typing import List

try:
    from crewai.memory import LongTermMemory, ShortTermMemory, EntityMemory
except ImportError:
    LongTermMemory = None
    ShortTermMemory = None
    EntityMemory = None


class TrendingCompany(BaseModel):
    """A company that is in the news and attracting attention"""
    name: str = Field(description="Company name")
    ticker: str = Field(description="Stock ticker symbol")
    reason: str = Field(description="Reason this company is trending in the news")


class TrendingCompanyList(BaseModel):
    """List of multiple trending companies that are in the news"""
    companies: List[TrendingCompany] = Field(description="List of companies trending in the news")


class TrendingCompanyResearch(BaseModel):
    """Detailed research on a company"""
    name: str = Field(description="Company name")
    market_position: str = Field(description="Current market position and competitive analysis")
    future_outlook: str = Field(description="Future outlook and growth prospects")
    investment_potential: str = Field(description="Investment potential and suitability for investment")


class TrendingCompanyResearchList(BaseModel):
    """A list of detailed research on all the companies"""
    research_list: List[TrendingCompanyResearch] = Field(description="Comprehensive research on all trending companies")


@CrewBase
class StockPicker():

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────────────────────────

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[SerperDevTool()],  # ✅ web search tool added here
            verbose=True
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'],
            tools=[SerperDevTool()],  # analyst can also search for deeper research
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
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
            config=self.tasks_config['pick_best_company']
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
            verbose=True
        )