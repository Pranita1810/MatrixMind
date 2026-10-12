# --- AUTOMATED WEB SCRAPER ---
from bs4 import BeautifulSoup
import requests
import polars as pl

class Scraper:
    """Automated web scraper to extract country demographic information."""

    def __init__(self):
        self.url = "https://www.scrapethissite.com/pages/simple/"

    def get_raw(self) -> str:
        response = requests.get(self.url, timeout=10)
        response.raise_for_status()
        return response.text

    def html_parser(self) -> BeautifulSoup:
        raw = self.get_raw()
        soup = BeautifulSoup(raw, "html.parser")
        return soup

    def extract_data(self):
        countries = []
        capitals = []
        populations = []
        areas = []
        soup = self.html_parser()

        country_nodes = soup.find_all("h3")
        capital_nodes = soup.find_all("span", class_="country-capital")
        pop_nodes = soup.find_all("span", class_="country-population")
        area_nodes = soup.find_all("span", class_="country-area")

        for c, cap, pop, a in zip(country_nodes, capital_nodes, pop_nodes, area_nodes):
            countries.append(c.get_text(strip=True))
            capitals.append(cap.get_text(strip=True))
            populations.append(pop.get_text(strip=True))
            areas.append(a.get_text(strip=True))

        return countries, capitals, populations, areas

    # Backward compatibility alias
    def extract_(self):
        return self.extract_data()

    def create_df(self) -> pl.DataFrame:
        country, capital, population, area = self.extract_data()
        df = pl.DataFrame({
            "Country": country,
            "Capital": capital,
            "Population": population,
            "Area": area
        })
        return df


if __name__ == "__main__":
    scraper = Scraper()
    df = scraper.create_df()
    print(df.head())

