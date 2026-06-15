def generate_insights(
    lunch,
    prep,
    average
):

    insights = []

    if prep == "completed":
        insights.append(
            "Student completed preparation course."
        )

    if lunch == "standard":
        insights.append(
            "Standard lunch often correlates with higher scores."
        )

    if average >= 80:
        insights.append(
            "Strong academic performance predicted."
        )

    elif average >= 65:
        insights.append(
            "Student likely to pass."
        )

    else:
        insights.append(
            "Student may need additional support."
        )

    return insights