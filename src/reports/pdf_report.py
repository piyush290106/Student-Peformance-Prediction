from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    filename,
    username,
    math_score,
    reading_score,
    writing_score,
    average,
    category
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Student Performance Prediction Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            f"Student: {username}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Math Score: {math_score}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Reading Score: {reading_score}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Writing Score: {writing_score}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Average Score: {average}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Performance Category: {category}",
            styles["Normal"]
        )
    )

    doc.build(elements)