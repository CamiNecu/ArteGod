import requests


def obtener_noticias_api(endpoint: str):
    """Fetch noticias desde la API local; retorna lista o None en error."""
    try:
        response = requests.get(endpoint, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None
