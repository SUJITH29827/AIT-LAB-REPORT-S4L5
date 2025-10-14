import openai


openai.api_key = "sk-proj-0RNAEubnq6sXkQ1hX0w6z5Ps07T3BlbkFJvI4FhINaeVlgFSPqRm8G0KkXtXSliKP5cR9MD28CDbijHfmEETQgat-73JRUIMkg5b-ulXQsEA"

messages = []

system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready! Type 'quit' to exit.")

while True:
    message = input("You: ")
    if message.lower() == "quit":
        break
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\nAssistant: " + reply + "\n")
