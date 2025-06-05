import requests
from typing import Any, Callable, List, Optional

# URL tvoje lokalne ili deployane API instance
PAYMAN_API_URL = "http://localhost:3000/ask"


async def call_payman(query: str) -> Optional[str]:
    """Call Payman AI agent via HTTP API."""

    PAYMAN_API_URL = "http://localhost:3000/ask"  # zamijeni ako koristiš ngrok

    payload = {"question": query}

    try:
        response = requests.post(PAYMAN_API_URL, json=payload, timeout=10)
        response.raise_for_status()  # ako HTTP status nije 200 - baca grešku
        data = response.json()

        # Ispiši cijeli JSON za analizu
        print("✅ Backend response:")
        print(data)

        # Ako želiš odmah ispisati sadržaj iz artifacts:
        artifacts = data.get("artifacts", [])
        if artifacts:
            content = artifacts[0].get("content")
            return content
        else:
            print("\nNo artifacts found in response")

    except requests.exceptions.RequestException as e:
        print("❌ Error connecting to Payman backend:")
        print(e)


# Lista toolova koje možeš registrirati u LangChain agentu
TOOLS: List[Callable[..., Any]] = [call_payman]
