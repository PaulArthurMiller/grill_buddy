from openai import OpenAI
client = OpenAI()

conversation_history = []

print("Hello! I'm Grill Chef, here to discuss the glory of grilling steaks! Whenever I've answered all your quesions, simply type 'goodbye.'")
print("What's on your mind?")

while True:
    syst_instr = "You are an expert outdoor grill chef, with a great sense of humor, who specializes in steaks. You love to tell the story of your grilling in brief, vivid vignettes. Your grandmother was French, and as an homage to her, you season your stories with the occasional French word. The person with whom you are speaking can hear the smile in your voice, even through the written word."
    user_input = input("User: ")

    if user_input.lower() != "goodbye":
        conversation_history.append({"role": "user", "content": user_input})
    else:
        print("Grill Chef: Thanks for discussing the wide world of grilling with me! Stimuler another conversation anytime! Have a great grilling day!")
        break

    try :
        conversation_history.append(f'{user_input}')
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = [
                {"role" : "system", "content" : f"{syst_instr}"},
                {"role" : "user", "content" : f"{conversation_history}"},
            ],
            temperature=0.7,
            max_tokens = 300,
        )

        model_response = response.choices[0].message.content
        print(f'Grill Chef: {model_response}')
        conversation_history.append({"role": "assistant", "content": model_response})

    except Exception as e:
        print(f"An error occurred: {e}")

    if user_input.lower() == "goodbye" :
        print("Grill Chef: Thanks for discussing the wide world of grilling with me! Stimuler another conversation anytime! Have a great grilling day!")
        break
