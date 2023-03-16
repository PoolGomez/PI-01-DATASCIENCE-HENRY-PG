from fastapi import FastAPI
import pandas as pd
#from numpy import numpy

app = FastAPI()

titles = pd.read_csv(r"datasets/titles.csv")
#titles = pd.read_csv("https://github.com/PoolGomez/PI-01-DATASCIENCE-HENRY-PG/blob/main/datasets/titles.csv")
    
#http://127.0.0.1:8000
@app.get("/")
def index():
    return {"mensaje":"Hello word"}

##Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
@app.get('/keyword/{plataforma}/{keyword}') #Segunda ruta
async def get_word_count(plataforma, keyword):
    canal= titles[titles['id'].str.contains(plataforma[0], case= False)]
    cantidad= canal[canal['title'].str.contains(keyword, case= False)]
    return {'plataforma':plataforma, 'cantidad':len(cantidad)}