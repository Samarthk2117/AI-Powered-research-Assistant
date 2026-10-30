import logging
import os
import time
from google import genai

logger = logging.getLogger("task_automation_agent")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

def create_research_brief(topic: str) -> dict:
    """Generate a concise three-point research brief with the Gemini API."""
    if not topic or not topic.strip():
        raise ValueError("Please enter a research topic.")

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured.")

    start = time.perf_counter()
    logger.info("Research request received")

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=(
                "You are a helpful research assistant. Create exactly three concise, "
                "useful bullet points about the topic below. Be clear and factual. "
                "If the topic requires current information, be transparent that this "
                "answer is a general AI-generated overview and should be verified.\n\n"
                f"Topic: {topic.strip()}"
            ),
        )
        text = (response.text or "").strip()
        points = []
        for line in text.splitlines():
            cleaned = line.strip().lstrip("-•*0123456789. )")
            if cleaned:
                points.append(cleaned)
        if not points and text:
            points = [text]
        points = points[:3]
        while len(points) < 3:
            points.append("Explore this topic further using reliable and up-to-date sources.")
        duration = time.perf_counter() - start
        logger.info("Research request completed in %.2f seconds", duration)
        return {"points": points, "duration_seconds": duration}
    except Exception:
        logger.exception("Research request failed")
        raise
