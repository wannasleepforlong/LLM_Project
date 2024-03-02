from fastapi import FastAPI

from langchain.llms import GooglePalm

app = FastAPI()

@api.get("/generate_poem")
def generate_poem():
    api_key = 'AIzaSyA0dtcycpyZIFYKEK-N3UUphgZstk1394A'
    llm = GooglePalm(google_api_key=api_key, temperature=0.2)
    poem = llm("Write a poem on samosa")
    return {"poem": poem}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)