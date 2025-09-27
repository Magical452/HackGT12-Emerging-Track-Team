import openai
# i'm ngl i stole all this code from chatGPT
openai.api_key = "YOUR_API_KEY_HERE" # screw you, you're not getting our API key lol

def get_food_ingredients_from_image(image_url):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # or "gpt-4o" with vision capability if available
        messages=[
            {"role": "system", "content": "You are a helpful assistant specialized in identifying food ingredients in images and generating 5 dishes that can be created with the ingredients. You will include recipes for each dish you create."},
            {"role": "user", "content": "Analyze the image, list all food ingredients you can identify, and generate 5 dishes that can be created with the ingredients from the image."},
            {
                "role": "user",
                "content": {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url
                    }
                }
            }
        ],
        temperature=0.5,
        max_tokens=200,
    )
    return response.choices[0].message['content']

# Example usage
if __name__ == "__main__":
    test_image_url = "https://example.com/path_to_your_food_image.jpg"
    ingredients = get_food_ingredients_from_image(test_image_url)
    print("Detected food ingredients:\n", ingredients)
