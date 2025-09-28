from openai import OpenAI
# i'm ngl i stole all this code from chatGPT
# openai.api_key = "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" # screw you, you're not getting our API key lol
client = OpenAI(
    api_key="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"
)
def get_food_ingredients_from_image(image_url):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "user",
             "content": [
                 {"type": "input_text", "text" : "Analyze the image, list all food ingredients you can identify."},
                 {"type": "input_image", "image_url": image_url},
                 ]
            },
        ],
        #temperature=0.5,
        #max_tokens=200,
    )
    return response.output_text

# Example usage
if __name__ == "__main__":
    test_image_url = "https://media.discordapp.net/attachments/1418046345482338360/1421337514345496757/table-laid-with-ingredients-and-utensils-manuel-sulzer.png?ex=68d8ab36&is=68d759b6&hm=68fbef511b15188fca4bdd6028c5cc407c28002cbed58afc5c2fa685916091e7&=&format=webp&quality=lossless&width=1350&height=617"
    ingredients = get_food_ingredients_from_image(test_image_url)
    print("Detected food ingredients:\n", ingredients)