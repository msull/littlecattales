import openai

from .chat_session import ChatSession


def create_image(prompt):
    return openai.images.generate(
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="b64_json",
        model="dall-e-3",
    ).model_dump()


GENERATE_IMAGE_DESCRIPTION_PROMPT = """
Given the following section of a short children's story about two cat siblings, 
write a very brief single-line description summarizing the main plot element. 
Focus on what the **two** cat siblings are doing, mention other major characters, and describe the setting. 
Include any specific objects mentioned. 
The characters should be simply described, not named.

This description will be used to generate a picture to accompany the text. 
Each description should start with "An oil painting of..."

The following characters may also be mentioned in the story:

- **Miss Olive**: An old, wise owl living in a tree near the cats' house.
- **Daisy**: A friendly, talkative squirrel who knows everything happening around.
- **Rusty**: A kind, funny dog who lives with the cats and considers them his best friends.

Only refer to these characters as "owl," "squirrel," and "dog" if they appear in the story section. 
Do not mention them if they are not in the story! 
Do not name the cats.

Example: "An oil painting of two playful cats hiding behind bushes as they prepare to splash a surprised dog with a bucket of water, while a curious squirrel watches from a nearby tree."

Story text begins now:
"""


def create_image_prompt(chat_history: ChatSession):
    story_ending = "\n\n".join(
        [x["content"] for x in chat_history.history if x["role"] != "system"][-3:]
    )

    prompt = f"{GENERATE_IMAGE_DESCRIPTION_PROMPT}\n\n{story_ending}"
    image_chat = ChatSession()
    image_chat.user_says(prompt)
    return image_chat.get_ai_response()
    # return openai.Completion.create(
    #     prompt=prompt, model="text-davinci-003", temperature=0.6,
    # )
