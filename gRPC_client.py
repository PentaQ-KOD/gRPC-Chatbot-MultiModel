# client.py
import grpc
import streamlit as st
import llm_service_pb2
import llm_service_pb2_grpc
from google.protobuf.json_format import MessageToDict

# =================================================================================================


def grpc_connect():
    channel = grpc.insecure_channel("localhost:50051")
    stub = llm_service_pb2_grpc.LLMServiceStub(channel)
    return stub


def handshake():
    request = llm_service_pb2.HandshakeRequest(
        json_config='{"client": "streamlit_client"}'
    )
    response = stub.Handshake(request)
    return response.json_config.fields["status"].string_value


# =========================================== Streamlit UI

st.title("--CLIENT--")
stub = grpc_connect()

if "handshake_response" not in st.session_state:
    st.session_state.handshake_response = handshake()

st.sidebar.write("### 🔗 Connection Status")
st.sidebar.success("Connected to gRPC Server")
st.sidebar.info(f"🤝 {st.session_state.handshake_response}")

# =============================================SIDE BAR======================================

with st.sidebar:

    # Sidebar for agent selection
    st.sidebar.title("Settings")
    agent_name = st.sidebar.selectbox(
        "🤖 Select Agent", ["None", "Gemini", "Deepseek", "Llama"], index=0
    )
    # ตรวจจับการเปลี่ยน Agent แล้วลบแชท
    if "previous_agent" not in st.session_state:
        st.session_state["previous_agent"] = agent_name

    if st.session_state["previous_agent"] != agent_name:
        st.session_state["messages"] = []  # เคลียร์ประวัติแชท
        st.session_state["previous_agent"] = agent_name  # อัปเดตค่า agent ล่าสุด
        st.rerun()

    user_id = st.sidebar.text_input("👤 Enter user ID:", "user_123")
    response_type = st.sidebar.radio(
        "🔁 Select Response Type",
        ["Generate Text", "Stream Text"],
        index=0,
    )

    if st.sidebar.button("Clear Chat"):
        st.session_state["messages"] = []  # Clear the chat history
        st.rerun()

    # Delete agent option
    st.divider()
    st.write("### ⚙️ Agent Management")
    if st.button("❌ Delete Agent"):
        delete_request = llm_service_pb2.DeleteAgentRequest(agent_name=agent_name)
        try:
            delete_response = stub.DeleteAgent(delete_request)
            st.warning(f"🗑️ {delete_response.status}")
            if delete_response.success:
                st.success("Agent deleted successfully")
            else:
                st.error("Failed to delete agent")
        except Exception as e:
            st.error(f"Error deleting agent: {str(e)}")

# =================================================================================================

# Initialize chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).markdown(message["content"])

# Handle user input
input_text = st.chat_input("💬 Enter your message...")


if input_text:
    # Add user's message to chat history
    st.session_state["messages"].append({"role": "user", "content": input_text})

    # Send the message to the server based on the selected response type
    if agent_name != "None":

        # สร้างข้อความที่รวมประวัติแชททั้งหมด
        chat_history = "\n".join(
            [f"{msg['role']}: {msg['content']}" for msg in st.session_state["messages"]]
        )
        full_input_text = f"{chat_history}\nUser: {input_text}\nAssistant:"

        if response_type == "Generate Text":
            response = stub.GenerateText(
                llm_service_pb2.TextRequest(
                    input=full_input_text, agent_name=agent_name, user_id=user_id
                )
            )
            if "response" in response.json_config.fields:
                generated_response = response.json_config.fields[
                    "response"
                ].string_value
            else:
                generated_response = "Error: No response from Gemini"

            st.session_state["messages"].append(
                {"role": "assistant", "content": generated_response}
            )

        elif response_type == "Stream Text":
            st.chat_message("user").markdown(input_text)
            placeholder = st.chat_message("assistant").empty()
            streaming_text = ""

            for response in stub.StreamText(
                llm_service_pb2.TextRequest(
                    input=full_input_text, agent_name=agent_name, user_id=user_id
                )
            ):
                if "response" in response.json_config.fields:
                    chunk_response = response.json_config.fields[
                        "response"
                    ].string_value
                    streaming_text += chunk_response
                    placeholder.markdown(streaming_text)

            st.session_state["messages"].append(
                {"role": "assistant", "content": streaming_text}
            )

    # If agent is None, just display the input text as response
    elif agent_name == "None":
        st.session_state["messages"].append(
            {"role": "assistant", "content": input_text}
        )

    st.rerun()
