from data_preprocessing import get_vector_db
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
import uuid

LLM = "google_genai:gemini-2.5-flash-lite"

def setup_chatbot(retriever):
    model = init_chat_model(LLM)

    @tool('retrieve_context', description="Return related context from the knowledge base")
    def retrieve_context(query: str) -> str:
        context = retriever.invoke(query)
        return context


    checkpointer = InMemorySaver()

    agent = create_agent(
        model=model,
        tools=[retrieve_context],
        system_prompt="You are a helpful assistant that answers questions based *only* on the retrieved context using the 'retrieve_context' tool. If the answer is not available in the context, clearly state that you don't know or cannot find the information. Do not invent answers or use prior knowledge. Always update your knowledge by calling the 'retrieve_context' tool with every query related to the SOP",
        checkpointer=checkpointer
    )

    return agent

def main():
    print("=========================================")
    print("   SOP Chatbot | Internal Tool v1.0")
    print("=========================================\n")
    load_dotenv()
    THREAD = str(uuid.uuid4())

    try:
        # Build the Brain
        retriever = get_vector_db()
        bot = setup_chatbot(retriever)
        print("\n✅ SYSTEM ONLINE. Ready for compliance queries.\n")

        # Interactive Loop
        while True:
            query = input("User Query (or 'exit'): ")
            if query.lower() in ['exit', 'quit', 'q']:
                print("System shutting down.")
                break
            
            if not query.strip():
                continue

            query_msg = [
                {
                    'role': 'user',
                    'content': f'{query}'
                }
            ]

            config =  {
                'thread_id': THREAD
            }

            response = bot.invoke(
                {'messages': query_msg},
                {'configurable': config}
            )
            print(f"\n>> ANSWER: {response['messages'][-1].content}\n")
            print("-" * 50)

    except Exception as e:
        print(f"\n❌ ERROR: {e}")

if __name__ == "__main__":
    main()
