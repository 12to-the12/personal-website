import os
import openai
openai.api_key = "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"


def query(engine="text-davinci-002",prompt="",temperature=0,max_tokens=100,top_p=1,
          frequency_penalty=0,presence_penalty=0,stop=["\n\n>>> "]):

    start_sequence = "\nNPC:"
    restart_sequence = "\n\n>>> "

    response = openai.Completion.create(
    engine=engine,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
    top_p=top_p,
    frequency_penalty=frequency_penalty,
    presence_penalty=presence_penalty,
    stop=stop
    )
    return response['choices'][0]['text']