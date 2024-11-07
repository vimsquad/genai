import click
from openai import OpenAI
import os




@click.command()
@click.option('--role', type=click.Choice(['system', 'assistant', 'user'], case_sensitive=False),
              help='The role of the message sender.')
@click.option('--content', prompt='Message content', help='The content of the message.')
def query_openai(role, content):
    """
    CLI tool to query OpenAI's chat completion endpoint.

    This tool allows you to send a message with a specified role and content
    to OpenAI's API and receive a chat completion response.
    """
    # Basic checks
    if not os.getenv("OPENAI_API_KEY"):
        click.echo("API Key is not set. Please set the OPENAI_API_KEY environment variable.")
        return

    # Prepare the message payload
    message = {
        "role": role,
        "content": content
    }

    # Make the API call
    try:
        client = OpenAI(
            # This is the default and can be omitted
            api_key=os.environ.get("OPENAI_API_KEY"),
        )

        response=client.chat.completions.create(
                model="gpt-3.5-turbo",  # Or any available model
                messages=[message]
        )
        # Print out the assistant's response
        if response and response['choices']:
            choice = response['choices'][0]
            assistant_message = choice['message']['content']
            click.echo(f"Assistant: {assistant_message}")
        else:
            click.echo("No response from model.")
    except Exception as e:
        click.echo(f"Error querying OpenAI: {e}")


if __name__ == '__main__':
    query_openai()
