def answer(query, context):
    q=query.lower()
    if "understaff" in q or "headcount gap" in q:
        return context["understaffed"]
    if "turnover" in q or "attrition" in q:
        return context["attrition"]
    if "hire" in q:
        return context["hiring"]
    if "budget" in q:
        return context["budget"]
    if "skill" in q or "ai" in q:
        return context["skills"]
    return "Decision-support summary: staffing, attrition, skills, and budget indicators are available. Ask a focused workforce question."
