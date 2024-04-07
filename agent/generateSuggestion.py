import openai
import PyPDF2
import os


from openai import OpenAI

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    with open(pdf_path, "rb") as file:
        # Create PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Initialize a variable to store the extracted text
        full_text = ""
        
        # Loop through each page in the PDF
        for page in pdf_reader.pages:
            # Extract text from the page and add it to the full_text variable
            full_text += page.extract_text() + "\n"  # Adding a newline character after each page for better readability
        
    return full_text

# Path to your PDF file
# pdf_path = "./faa-h-8083-25c.pdf"

# Extract text
# extracted_text = extract_text_from_pdf(pdf_path)

prompts = {
    "bad_weather": "Give me a summary in less than 3 sentences in step by step for a pilot when there is a bad weather based on FAA",
    "risky_airport": "Give me a summary in less than 3 sentences in step by step for a pilot when the airport is a high risk airport"
}

# response = client.chat.completions.create(
#    model="gpt-3.5-turbo",
#    messages=[{"role": "user", "content": prompts['risky_airport']}],
#    stream=True,
# )


for chunk in response:
    print(chunk.choices[0].delta.content or "", end="")