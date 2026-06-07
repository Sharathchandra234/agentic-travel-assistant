import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import streamlit as st
from src.agent import TravelAgent
from src.pdf_generator import generate_trip_pdf

st.set_page_config(page_title="Agentic Travel Assistant")

st.title("🌍 Agentic Travel Assistant")

query = st.text_input(
    "Enter your travel request",
    placeholder="Plan a 3 day trip to Goa under 20000 rupees"
)

if st.button("Plan Trip"):
    try:
        agent = TravelAgent()

        result = agent.plan_trip(query)

        st.success("Trip Plan Generated")

        st.subheader("🌍 Destination")
        st.write(result["destination"])

        st.subheader("💰 Budget")
        st.write(f"₹{result['budget']}")

        st.subheader("📅 Duration")
        st.write(f"{result['days']} Days")

        st.subheader("☀️ Weather")
        st.json(result["weather"])

        st.subheader("🏨 Hotels")

        for hotel in result["hotels"]:
            st.write(
                f"**{hotel['name']}** - ₹{hotel['price']}/night"
            )

        st.subheader("💵 Budget Allocation")

        budget = result["budget_plan"]

        st.write(f"Accommodation: ₹{budget['accommodation']}")
        st.write(f"Food: ₹{budget['food']}")
        st.write(f"Transportation: ₹{budget['transportation']}")
        st.write(f"Activities: ₹{budget['activities']}")

        st.subheader("🗺️ Itinerary")

        st.subheader("🗺️ Itinerary")
        st.markdown(result["itinerary"])

        st.subheader("✈️ AI Travel Advice")
        st.write(result["travel_advice"])

        # PDF Download
        pdf_file = generate_trip_pdf(result)

        with open(pdf_file, "rb") as file:
            st.download_button(
                label="📄 Download Trip Report",
                data=file,
                file_name="trip_report.pdf",
                mime="application/pdf",
            )

    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.divider()
if st.button("Show Previous Trips"):
    agent = TravelAgent()

    history = agent.get_memory_summary()

    st.subheader("🧠 Travel Memory")

    if history:
        st.json(history)
    else:
        st.info("No previous trips found.")