import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_discount(customer):
    prompt = f"Discount for customer with age {customer.age}, " \
             f"disabled {customer.is_disabled}, medical conditions {customer.medical_conditions}"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50
    )
    discount = float(response.choices[0].text.strip())
    return discount
