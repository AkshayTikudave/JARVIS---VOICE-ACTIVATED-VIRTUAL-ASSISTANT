from openai import OpenAI

# client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# If you save the key under a different environment variable name, you can do something like:

client = OpenAI(
    api_key = "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"
)


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        { "role": "system", "content": "You are a helpful virtual assistant named jarvis skilled in general tasks like Alexa, Siri, Google assistant." },
        { "role": "user", "content": "what is coding" }
    ]
)

print(completion.choices[0].message.content)

