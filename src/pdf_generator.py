from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_trip_pdf(
    trip_data,
    filename="trip_report.pdf",
):
    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Agentic Travel Assistant Report",
            styles["Title"],
        )
    )

    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            f"Destination: {trip_data['destination']}",
            styles["BodyText"],
        )
    )

    elements.append(
        Paragraph(
            f"Budget: ₹{trip_data['budget']}",
            styles["BodyText"],
        )
    )

    elements.append(
        Paragraph(
            f"Duration: {trip_data['days']} Days",
            styles["BodyText"],
        )
    )

    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            "Travel Advice",
            styles["Heading2"],
        )
    )

    elements.append(
        Paragraph(
            str(trip_data["travel_advice"]),
            styles["BodyText"],
        )
    )

    doc.build(elements)

    return filename