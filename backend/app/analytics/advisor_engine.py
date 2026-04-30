def answer_question(question: str, context: dict):
    q = question.lower()
    if any(k in q for k in ["most energy", "highest usage", "wasting"]):
        top = context.get("top_machine")
        return f"{top['machine_name']} is currently the highest energy consumer at {top['kwh']:.1f} kWh over the selected period."
    if any(k in q for k in ["spike", "anomaly"]):
        return context.get("anomaly_summary", "No anomalies detected recently.")
    if any(k in q for k in ["save", "reduce cost", "savings"]):
        return context.get("recommendation_summary")
    if "peak" in q:
        return context.get("peak_summary")
    if "line" in q:
        return context.get("line_summary")
    return "I can answer about top energy users, anomalies, peak demand, line-level costs, and savings opportunities."
