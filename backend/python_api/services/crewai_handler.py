import subprocess

def send_to_crewai(prompt: str):
    """Sends the design prompt to CrewAI for processing."""
    try:
        result = subprocess.run(
            ["python3", "crew_ai_script.py", prompt], capture_output=True, text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error processing with CrewAI: {e}"
