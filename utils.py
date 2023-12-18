from openai import OpenAI
import math


def generate_embedding(openai_client: OpenAI, text: str) -> list[float]:
    return (
        openai_client.embeddings.create(input=[text], model="notNeeded")
        .data[0]
        .embedding
    )


def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))


def magnitude(v):
    return math.sqrt(dot_product(v, v))


def cosine_similarity(v1, v2):
    return dot_product(v1, v2) / (magnitude(v1) * magnitude(v2))


def is_relevant_query(similarity: float) -> bool:
    return similarity > 0.8
