import streamlit as st
from openai import OpenAI

from chatbot import chat
from utils import generate_embedding


st.title("Chevrolet of Watsonville")

openai_client = OpenAI(
    base_url="https://demo.deployradiant.com/watsonville/openai",
    api_key="notNeeded",
)

SYSTEM_PROMPT = "You are a helpful assistant for Chevrolet of Watsonville. You assist customers with their questions about Chevrolet. Be polite and helpful. If you don't know the answer, say you don't know."
SYSTEM_PROMPT_EMBEDDING = generate_embedding(openai_client=openai_client, text=SYSTEM_PROMPT)

query = st.text_input("Enter search query:")
if query:
    result = chat(
        openai_client=openai_client,
        system_prompt=SYSTEM_PROMPT,
        system_prompt_embedding=SYSTEM_PROMPT_EMBEDDING,
        user_query=query,
    )

    if result:
        st.write(result)
    else:
        st.write("No results found")

# st.sidebar.header("About")
# st.sidebar.markdown(
#     """
#     This is a
#     This is a demo of a RAG (Retrieval-Augmented Generation) model for Plasma Physics built using the Radiant platform and MongoDB Atlas.
#     Here is a link to the source code: [GitHub](https://github.com/deployradiant/mongodb-rag-example)
#
#
#     To learn more about Radiant please visit the [Radiant website](https://www.radiantai.com).
#     To learn more about MongoDB Atlas please visit the [MongoDB Atlas website](https://www.mongodb.com/cloud/atlas).
#
#     Email akanekar@radiantai.com for any questions.
#     """
# )
