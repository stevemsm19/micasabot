import streamlit as st

def main():
    st.title("MiCasa Bot 🏠")

    if 'messages' not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hola! ¿Como puedo ayudarte?"}]

if __name__ == "__main__":
    main()
