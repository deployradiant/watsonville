from openai import OpenAI

from utils import generate_embedding, cosine_similarity, is_relevant_query


def chat(openai_client: OpenAI, system_prompt: str, system_prompt_embedding: list[float], user_query: str):
    user_query_embedding = generate_embedding(openai_client=openai_client, text=user_query)
    similarity = cosine_similarity(
        system_prompt_embedding, user_query_embedding
    )

    if not is_relevant_query(similarity):
        return "I'm sorry, this isn't a relevant query. Please try again.\n\n Protected by Radiant."

    response = openai_client.chat.completions.create(
        model="notNeeded",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {"role": "user", "content": user_query},
        ],
        n=1,
    )

    return response.choices[0].message.content
