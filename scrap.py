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

def getBCCPrice():
    URL = "https://www.bc.gob.cu/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find("div", class_="swiper-container swiper-tasa")

    results = results.find("div", class_="caption")
    results = results.find("tbody")

    rows = results.find_all("tr")

    valuesRows = """
        Precios:
    """

    for r in rows:
        td = r.find_all("td")
        [nombre, siglas, tc, tcPoblacion] = td
        val= f"""
        {siglas.text.strip()}
        total: {(tcPoblacion).text.strip()}
        con impuesto({"8%" if siglas.text.strip()== "USD" else "2%"  }): {float((tcPoblacion).text.strip())*0.92 if siglas.text.strip()== "USD" else float((tcPoblacion).text.strip())*0.98  }
        """
        valuesRows+=(val)

    return (valuesRows)
