import os
import sys
import argparse
from dotenv import load_dotenv
from google.genai import types

def main():
	parser = argparse.ArgumentParser(description="AI agent script.")
	parser.add_argument('message', help="Message to pass to the AI agent.")
	parser.add_argument('--verbose', action="store_true", help="Enable verbose output")
	args = parser.parse_args()

	if args.message is None:
		print("No prompt was provided.  Exiting program.")
		sys.exit(1)

	messages = [
		types.Content(role="user", parts=[types.Part(text=args.message)]),
	]

	load_dotenv()
	api_key = os.environ.get("GEMINI_API_KEY")

	from google import genai

	client = genai.Client(api_key=api_key)
	system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""
	response = client.models.generate_content(
    model_name = "gemini-1.5-flash",
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)
	print(response.text)
	if args.verbose:
		print(f"User prompt: {args.message}")
		print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
		print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()