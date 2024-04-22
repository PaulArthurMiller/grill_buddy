from openai import OpenAI
import streamlit as st
import base64

def main_bg(background_image_path):
    with open(background_image_path, "rb") as image_file:
        # Encode the image to base64 string
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    # CSS to set the background image with styles
    css = f"""
    <style>
    .stApp {{
        background-image: linear-gradient(to right, rgba(255, 255, 255, 0.7) 10%, rgba(255, 255, 255, 0.9) 100%), url("data:image/png;base64,{encoded_image}");
        background-size: cover;
        background-position: left center;
    }}
    </style>
    """

    # Inject CSS with markdown
    st.markdown(css, unsafe_allow_html=True)

# Path to your image
background_image_path = "C:/Users/user/OneDrive/Documents/projects/grill_buddy/elements/grill_buddy.png"
main_bg(background_image_path)

st.title("Grill Buddy")

client = OpenAI()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.write("Hello! I'm Grill Chef, here to discuss the glory of grilling!")
# print("What's on your mind?")

#while True:
syst_instr = "You are an expert outdoor grill chef, with a great sense of humor, who specializes in steaks. You love to tell the story of your grilling in brief, vivid vignettes. Your grandmother was French, and as an homage to her, you season your stories with the occasional French word. The person with whom you are speaking can hear the smile in your voice, even through the written word."
# user_input = st.chat_input("Your question:")

if user_input := st.chat_input("What's cookin'?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_input)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    # if user_input.lower() != "goodbye":
    #     conversation_history.append({"role": "user", "content": user_input})
    # else:
    #     print("Grill Chef: Thanks for discussing the wide world of grilling with me! Stimuler another conversation anytime! Have a great grilling day!")
    #     break

    try :
        #conversation_history.append(f'{user_input}')
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = [
                {"role" : "system", "content" : f"{syst_instr}"},
                {"role" : "user", "content" : f"{user_input}"},
            ],
            temperature=0.7,
            max_tokens = 300,
        )

        model_response = response.choices[0].message.content
        # print(f'Grill Chef: {model_response}')
        # conversation_history.append({"role": "assistant", "content": model_response})

    except Exception as e:
        st.write(f"An error occurred: {e}")

    # if user_input.lower() == "goodbye" :
    #     print("Grill Chef: Thanks for discussing the wide world of grilling with me! Stimuler another conversation anytime! Have a great grilling day!")
    #     break

    st.session_state.messages.append({"role": "assistant", "content": model_response})
    st.write(model_response)

