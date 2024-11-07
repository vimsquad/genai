# OpenAI Chat Completion CLI Tool

This Python script is a Command Line Interface (CLI) tool that allows you to query OpenAI's chat completion endpoint by sending a message with a specified role and content and receiving a chat completion response.

## Installation

To install genclai, use pip:

```bash
pip install .
```

## Usage

```bash
export OPENAI_API_KEY="****"

genclai --role <role> --content '<content>'
```

### Options

- `--role`: The role of the message sender. Choices: `system`, `assistant`, `user`.
- `--content`: The content of the message.

### Example

```bash
export OPENAI_API_KEY="****"

genclai --role user --content 'How do you train a dog not to pull on a leash?'
```
