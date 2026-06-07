# Agentic Travel Assistant 🌍

An AI-powered travel planning application built using Python, Streamlit, LangChain, Google Gemini, and OpenWeather API.

## Features

* AI-generated travel itineraries
* Budget planning and allocation
* Real-time weather information
* Travel recommendations and tips
* Memory of previous trip requests
* PDF trip report generation
* Interactive Streamlit web interface

## Technologies Used

* Python
* Streamlit
* LangChain
* Google Gemini API
* OpenWeather API
* ReportLab
* Requests
* Python Dotenv

## Project Structure

```text
agentic_travel_assistant/
│
├── app/
│   └── streamlit_app.py
│
├── src/
│   ├── agent.py
│   ├── config.py
│   ├── memory.py
│   ├── pdf_generator.py
│   ├── planner.py
│   └── tools.py
│
├── screenshots/
├── requirements.txt
├── README.md
└── .env.example
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/Sharathchandra234/agentic-travel-assistant.git
cd agentic-travel-assistant
```

2. Create a virtual environment

```bash
python -m venv .venv
```

3. Activate virtual environment

Windows:

```bash
.venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Configure environment variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
OPENWEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY
GEMINI_MODEL=gemini-2.5-flash
```

6. Run the application

```bash
streamlit run app/streamlit_app.py
```

## Example Query

```text
Plan a 3 day trip to Chennai under 20000 rupees
```

## Future Improvements

* Real hotel booking APIs
* Multi-agent architecture
* Flight recommendations
* Interactive maps
* Public deployment
* User authentication

## Author

Sharath Chandra
B.Tech Graduate | Machine Learning & AI Enthusiast
