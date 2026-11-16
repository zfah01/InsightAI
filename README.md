# InsightAI – Conversational Business Analytics Assistant

An AI-powered business analytics assistant that allows users to explore business performance through natural-language questions.

InsightAI combines Google's Gemini API with Python-based analytics to turn business data into meaningful insights through a conversational interface.

## Project Overview

InsightAI demonstrates how Large Language Models (LLMs) can be integrated with controlled analytical tools to support conversational business intelligence.

Users can ask questions about sales performance and receive answers generated using actual calculations performed on the underlying dataset.

Rather than relying on the LLM to calculate figures, InsightAI uses Python and Pandas to perform the analytical operations and Gemini to interpret questions and communicate the results.

## Key Features

- **Conversational Analytics:** Ask business questions using natural language.
- **LLM Integration:** Uses Google's Gemini API to interpret user questions.
- **Function Calling:** Gemini selects from approved Python analytics functions.
- **Data Analysis:** Pandas performs calculations against the sales dataset.
- **Conversation Memory:** Supports follow-up questions within a conversation.
- **Business Dashboard:** Displays key performance indicators and revenue breakdowns.
- **AI Evaluation:** Evaluates responses against expected business results.
- **Automated Testing:** Uses Pytest to test analytical functions and metric definitions.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Pandas | Data processing and analytics |
| Google Gemini API | Natural-language understanding and response generation |
| Gemini Function Calling | Connecting the LLM to approved Python functions |
| Streamlit | Interactive dashboard and chat interface |
| Pytest | Automated testing |
| Git and GitHub | Version control and project management |

## Architecture

InsightAI follows a controlled tool-calling architecture.

1. The user submits a natural-language question through Streamlit.
2. Gemini interprets the question and selects an appropriate analytical function.
3. The selected Python function processes the sales dataset using Pandas.
4. The calculated results are returned to Gemini.
5. Gemini generates a natural-language response grounded in the analytical results.
6. Streamlit displays the response to the user.

```text
              USER
                |
                v
       STREAMLIT INTERFACE
                |
                v
          GEMINI API
                |
         Function Calling
                |
                v
        PYTHON ANALYTICS
                |
                v
          PANDAS DATA
                |
         Calculated Results
                |
                v
          GEMINI API
                |
                v
       NATURAL LANGUAGE
             RESPONSE
                |
                v
       STREAMLIT INTERFACE
```

## Available Analytics

InsightAI currently supports:

| Analytical function | Description |
|---|---|
| Total Revenue | Calculates revenue from completed orders |
| Revenue by Region | Breaks down revenue across sales regions |
| Revenue by Product | Compares revenue across products |
| Order Status | Counts completed, cancelled and returned orders |
| Average Order Value | Calculates average revenue per completed order |
| Cancellation Rate | Calculates the percentage of cancelled orders |

## Dataset

The project uses a synthetic sales dataset containing 1,000 orders.

The dataset includes:
- Order ID
- Product
- Region
- Quantity
- Unit price
- Revenue
- Order date
- Customer ID
- Order status

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/zfah01/InsightAI.git
cd InsightAI
```

### 2. Create a virtual environment

```bash
py -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

Obtain an API key through Google AI Studio.

Never commit your `.env` file or expose your API key publicly.

### 5. Run the application

```bash
streamlit run frontend/app.py
```

## Testing

Run the automated unit tests:

```bash
python -m pytest tests/ -v
```

Run the AI evaluation framework:

```bash
python -m evaluation.evaluate_agent
```

The evaluation framework checks whether responses contain expected business results.

## Future Improvements

Potential enhancements include:

- More comprehensive AI evaluation and tool-selection metrics.
- Persistent conversation history.
- Additional analytical tools and business datasets.
- Improved visualisations and interactive reporting.
- API layer and deployment.
- Logging, monitoring and performance evaluation.

## Author

Developed as a personal AI engineering portfolio project to explore conversational analytics, LLM integration, Python development and AI-powered business intelligence.