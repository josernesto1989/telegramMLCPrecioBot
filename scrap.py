import requests

from bs4 import BeautifulSoup

def getElToqueMLCPrice():
    URL = "https://eltoque.com/tasas-de-cambio-de-moneda-en-cuba-hoy#informal-calc"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="informal-median")

    rows = results.find_all("tr");

    valuesRows = """
        Precios:
    """

    for r in rows:
        [venta, compra] = r.find_all("span", class_="price-text")
        val= f"""
        {(r.find("span",class_="currency")).text.strip()}
        Venta: {(venta).text.strip()}
        Compra:{(compra).text.strip()}
        """
        valuesRows+=(val)

    return (valuesRows)