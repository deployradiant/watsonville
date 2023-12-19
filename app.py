import streamlit as st
from openai import OpenAI

from chatbot import chat
from utils import generate_embedding


st.title("Chevrolet of Watsonville")

st.sidebar.header("About")
st.sidebar.markdown(
    """
    Recently someone discovered that they could use the Chevrolet support bot to answer any questions, effectively turning it into a proxy for GPT-4. 

    This is a demo of a chatbot built using the Radiant platform that protects against this kind of abuse.

    Check out radiant at [https://www.radiantai.com](https://www.radiantai.com).
    """
)

openai_client = OpenAI(
    base_url="https://demo.deployradiant.com/watsonville/openai",
    api_key="notNeeded",
)

SYSTEM_PROMPT = "You are a helpful assistant for Chevrolet of Watsonville. You assist customers with their questions about Chevrolet. Be polite and helpful. If you don't know the answer, say you don't know."
# SYSTEM_PROMPT_EMBEDDING = generate_embedding(openai_client=openai_client, text=SYSTEM_PROMPT)

# query = st.text_input("Enter search query:")
# if query:
#     result = chat(
#         openai_client=openai_client,
#         system_prompt=SYSTEM_PROMPT,
#         system_prompt_embedding=SYSTEM_PROMPT_EMBEDDING,
#         user_query=query,
#     )
#
#     if result:
#         st.write(result)
#     else:
#         st.write("No results found")
#

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Say something"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = chat(
        openai_client=openai_client,
        system_prompt=SYSTEM_PROMPT,
        user_query=prompt,
    )

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
