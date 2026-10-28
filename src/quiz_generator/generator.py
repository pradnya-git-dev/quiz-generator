from dotenv import load_dotenv
import sys
import anthropic
from .utils import write_to_file, FileConfig

load_dotenv()  # Loads variables from .env into system environment variables

client = anthropic.Anthropic()  # Reads ANTHROPIC_API_KEY automatically


def generate(source_text: str):

    response = client.messages.create(
        model="claude-sonnet-4-6",
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

    response_data = ""

    for block in response.content:
        if block.type == "text":
            response_data += f"{block.text}\n"

    file_config = FileConfig(name="output-quiz", ext=".md")
    write_to_file(response_data, file_config)


def main():
    if len(sys.argv) < 2:
        print("Missing arg: <path/to/source/text.md>")
        sys.exit(1)

    with open(sys.argv[1]) as source_text_file:
        source_text = source_text_file.read()

    generate(source_text)


if __name__ == "__main__":
    main()