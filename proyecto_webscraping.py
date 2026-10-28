from bs4 import BeautifulSoup
import requests



# Recorrer las 50 paginas y guardar los titulos de libros con 4 o 5 estrellas.
libros_destacados = []
for page in range(1, 50):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    libros = soup.find_all("article", class_="product_pod")

    for libro in libros:
        rating = libro.find("p",class_="star-rating")
        clases_rating = rating.get("class")

        if "Four" in clases_rating or "Five" in clases_rating:
            titulo = libro.find("h3").find("a").get("title")
            libros_destacados.append(titulo)



print(libros_destacados)




