import openai
import json
import os

api_key = os.environ.get("API_KEY")
client = openai.OpenAI(api_key=api_key)


def get_ratings(messages):
    prompt = """
    You are an assistant that helps users label various emotional qualities about a conversation. Given the conversation provided by the user under the section called CONVERSATION: that is given with the different parties represented by P1, P2, etc, give three numerical answers as follows:

    First, output a score from 1 to 5 that represents what valence the conversation is.
    1 - Very negative
    2 - Negative
    3 - Neutral
    4 - Positive
    5 - Very positive

    Second, output a score from 1 to 5 that represents how arousing the conversation is.
    1 - Very calm
    2 - Calm
    3 - Neutral
    4 - Energetic
    5 - Very energetic

    Third, output a score from 1 to 3 that represents how literal the conversation is.
    1 - Can be taken literally
    2 - Regular human speech with complexities, mostly straightforward
    3 - Very metaphorical, sarcastic or abstract

    Please respond ONLY as three numbers separated by commas as plain text. For example, "4, 3, 2".

    Then, on the next line, please provide an example of an appropriate response to the conversation that matches the emotion present. This should be a simple line of text.

    On the last line, once again provide the three numberical values described above, but this time for the example response you provided. Again respond only as plain text with the three numbers separated by commas. For example, "4, 3, 2".

    An example response would look like:
    1, 2, 3
    That's interesting!
    4, 3, 2
    """

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"CONVERSATION:\n{messages}"},
        ]
    )

    result = completion.choices[0].message.content
    if result is not None:
        try:
            ratings, response, response_ratings = result.split("\n")
            return (
                [int(num.strip()) for num in ratings.split(",")],
                response,
                [int(num.strip()) for num in response_ratings.split(",")]
            )
        except:
            raise Exception("Wrong format", result)
    else:
        raise Exception("No response", result)


with open("annotated.json") as f:
    llm_annotated = []

    data = json.load(f)
    for conversation in data:
        messages, senders = conversation["messages"], conversation["senders"]
        labeled_conversation = "\n".join(
            [f"{senders[i]}: {messages[i]}" for i in range(len(messages))])
        ratings, response, response_ratings = get_ratings(labeled_conversation)
        llm_annotated.append({
            "messages": messages,
            "senders": senders,
            "ratings": conversation["ratings"],
            "llm_ratings": ratings,
            "response": response,
            "response_ratings": response_ratings
        })

    with open("llm_annotated.json", "w") as f:
        json.dump(llm_annotated, f, indent=2)
