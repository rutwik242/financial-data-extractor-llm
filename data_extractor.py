from dotenv import load_dotenv
from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model_name="openai/gpt-oss-120b")


def extract(article_text):
    prompt = """
You are a financial data extraction assistant.

Extract the following financial metrics from the article:

1. Revenue
2. EPS
3. Net Income
4. Operating Income
5. Free Cash Flow
6. Gross Margin

Return a valid JSON object containing these keys:

revenue_actual
revenue_expected
eps_actual
eps_expected
net_income_actual
net_income_expected
operating_income_actual
operating_income_expected
free_cash_flow_actual
free_cash_flow_expected
gross_margin_actual
gross_margin_expected

Rules:
1. Extract only information explicitly mentioned in the article.
2. Do not calculate, estimate, or invent missing values.
3. If a value is unavailable, return null.
4. Preserve currencies and units exactly as reported.
5. EPS should include its currency per share when provided.
6. Gross margin should be expressed as a percentage.
7. Expected values must represent analyst estimates or consensus.
8. Do not confuse company guidance with analyst estimates.
9. Return only valid JSON, without markdown or explanations.

Article:
=======
{article}
"""

    pt = PromptTemplate.from_template(prompt)

    global llm  # noqa: PLW0602

    chain = pt | llm
    response = chain.invoke({'article': article_text})
    parser = JsonOutputParser()

    try:
        res = parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")

    return res