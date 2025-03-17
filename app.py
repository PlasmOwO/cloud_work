from fastapi import FastAPI
import unidecode
import main

model = main.Main()
app = FastAPI()

@app.post("/testing")
async def testing(input_string):
    return model.predict(input_string)