import os
import requests

def query_rag(message: str) -> str:
    endpoint = os.getenv("RAG_ENDPOINT")
    token = os.getenv("DATABRICKS_TOKEN")
    resp = requests.post(
        endpoint,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        json={"messages":[{"role":"user","content":message}]}
    )

    if resp.status_code != 200:
        return f"Error {resp.status_code}: {resp.text}"

    jsond = resp.json()
    return jsond["choices"][0]["message"]["content"]
