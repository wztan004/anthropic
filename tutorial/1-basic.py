# Basic usage

import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)
response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ],
    temperature=0,
    system="You are a helpful assistant that can answer questions and help with tasks.",
)

# [TextBlock(citations=None, text="Hello! It's nice to meet you. How can I assist you today?", type='text')]
print(response.content)

# [TextBlock(citations=None, text="Hello! It's nice to meet you. How can I assist you today?", type='text')]
# Message(id='msg_01BgRhwkx4VgHJvPPzjqCydq', content=[TextBlock(citations=None, text="Hello! It's nice to meet you. How can I assist you today?", type='text')], model='claude-3-haiku-20240307', role='assistant', stop_reason='end_turn', stop_sequence=None, type='message', usage=Usage(cache_creation_input_tokens=0, cache_read_input_tokens=0, input_tokens=24, output_tokens=19, server_tool_use=None, service_tier='standard'))
print(response)