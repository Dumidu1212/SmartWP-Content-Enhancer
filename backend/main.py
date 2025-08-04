
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class PromptRequest(BaseModel):
    text: str
    instruction: str

@app.post("/rewrite")
async def rewrite_text(req: PromptRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You are an AI assistant that helps rewrite content. Follow this instruction: {req.instruction}"},
                {"role": "user", "content": req.text}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return {"rewritten_text": response.choices[0].message.content.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
