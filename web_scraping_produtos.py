from bs4 import BeautifulSoup
import pandas as pd

html = """
<html>
    <body>
        <div class="produto">
            <h2>Notebook Gamer</h2>
            <span class="preco">4500</span>
        </div>

        <div class="produto">
            <h2>Mouse Sem Fio</h2>
            <span class="preco">120</span>
        </div>

        <div class="produto">
            <h2>Teclado Mecânico</h2>
            <span class="preco">350</span>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

produtos = []

for item in soup.find_all("div", class_="produto"):
    nome = item.find("h2").text
    preco = float(item.find("span", class_="preco").text)

    produtos.append({
        "nome": nome,
        "preco": preco
    })

df = pd.DataFrame(produtos)

print(df)

df.to_excel("produtos.xlsx", index=False)

print("Planilha produtos.xlsx criada com sucesso.")