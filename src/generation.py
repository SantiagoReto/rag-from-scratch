from openai import OpenAI

def generate_response(query, context_text, api_key, model):

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model=model,
        input= [
            {
                "role": "system",
                "content": "You are a helpfull assistant that will receive a user query as well as context for that query. Your job is to help the user get the correct answer. For craft the response you should only use the context and dont create information that dont appear on context. You should also retrieve the page number"
            },
            {
                "role": "user",
                "content": f"Query: {query}\n\n Context: {context_text}"
            }
        ]
    )

    response = response.output_text
    return response