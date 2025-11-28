import chainlit as cl
from data_preprocessing import get_vector_db
from dotenv import load_dotenv
from sop_chat_cli import setup_chatbot

@cl.on_chat_start
async def on_chat_start():
    """
    Initializes the chatbot when a new chat session starts.
    """
    load_dotenv()
    retriever = get_vector_db()
    bot = setup_chatbot(retriever)
    cl.user_session.set("agent", bot)
    await cl.Message(content="✅ SYSTEM ONLINE. Ready for compliance queries.").send()

@cl.on_message
async def on_message(message: cl.Message):
    """
    Handles incoming user messages.
    """
    agent = cl.user_session.get("agent")
    thread_id = cl.user_session.get("id")
    
    query_msg = [{'role': 'user', 'content': message.content}]
    config = {'configurable': {'thread_id': thread_id}}

    response = await agent.ainvoke({'messages': query_msg}, config)
    await cl.Message(content=response['messages'][-1].content).send()
