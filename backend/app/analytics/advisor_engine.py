import json
import os


def _llm_answer(question: str, context: dict) -> str | None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)
        system_prompt = (
            "You are an energy optimization expert. "
            "Answer user questions from the provided JSON context. "
            "If data is missing, explicitly say what is missing.\n"
            f"Context: {json.dumps(context)}"
        )
        completion = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question},
            ],
            temperature=0.2,
        )
        return completion.choices[0].message.content
    except Exception:
        return None


def answer_question(question: str, context: dict):
    llm_response = _llm_answer(question, context)
    if llm_response:
        return llm_response

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
