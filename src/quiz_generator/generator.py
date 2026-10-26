from dotenv import load_dotenv
import sys
import anthropic

load_dotenv()  # Loads variables from .env into system environment variables

client = anthropic.Anthropic()  # Reads ANTHROPIC_API_KEY automatically


def generate(source_text: str):
    response = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=1024,
        system="You are an exam setter.",
        messages=[
            {
                "role": "user",
                "content": "Generate a quiz using the following study material: \n"
                + source_text,
            }
        ],
    )

    for block in response.content:
        if block.type == "text":
            print(block.text)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: generator.py <path/to/source/text.md>")
        sys.exit(1)

    with open(sys.argv[1]) as source_text_file:
        source_text = source_text_file.read()

    generate(source_text)
