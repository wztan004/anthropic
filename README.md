Based on 13 June 2025 info
# Commands
1. `poetry env activate`
2. `python tutorial/1-basic.py`

# Learnings
- You always send the full conversational history to the API.
- For tool definitions, prioritize descriptions over examples.
- You can force a tool use, i.e. JSON.

# Prompt Engineering
- Prefer prompting to finetuning
- Be explicit. Prefer `Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation.` to `Create an analytics dashboard`.
- Add motivation. Prefer `Your response will be read aloud by a text-to-speech engine, so never use ellipses since the text-to-speech engine will not know how to pronounce them.` to `NEVER use ellipses`
- Tell Claude what to do instead of what not to do
- Use XML format indicators, e.g. `Write the prose sections of your response in <smoothly_flowing_prose_paragraphs> tags.`
- Leverage thinking, `After receiving tool results, carefully reflect on their quality and determine optimal next steps before proceeding. Use your thinking to plan and iterate based on this new information, and then take the best next action.`
- Frontier language models can sometimes focus too heavily on making tests pass at the expense of more general solutions. To prevent this behavior and ensure robustgeneralizable solutions:
`Please write a high quality, general purpose solution. Implement a solution that works correctly for all valid inputs, not just the test cases. Do not hard-code values or create solutions that only work for specific test inputs. Instead, implement the actual logic that solves the problem generally. Focus on understanding the problem requirements and implementing the correct algorithm. Tests are there to verify correctness, not to define the solution. Provide a principled implementation that follows best practices and software design principles. If the task is unreasonable or infeasible, or if any of the tests are incorrect, please tell me. The solution should be robust, maintainable, and extendable.`
- use examples (multi-shot prompting)
- Let Claude think: Use XML tags like <thinking> and <answer> to separate reasoning from the final answer.
- Role prompting
- Prefill response
- Prompt chaining
- Long context: Put longform data at the top. Structure document content and metadata with XML tags: When using multiple documents, wrap each document in <document> tags with <document_content> and <source> (and other metadata) subtags for clarity. Ground responses in quotes: For long document tasks, ask Claude to quote relevant parts of the documents first before carrying out its task. This helps Claude cut through the “noise” of the rest of the document’s contents.
- Have Claude reflect on and check its work for improved consistency and error handling
- Hallucinations:
    - Allow Claude to say “I don’t know”
    - Use direct quotes and citations
- Consistency
    - Specify output format
    - Pre-fill
    - Provide examples
    - 

# Really useful features
- Extended thinking: provides transparency into thought process before it delivers its final answer.
- citations: provide detailed citations when answering questions about documents
- embeddings: for search, recommendations, anomaly detection
- vision: analyze image
- tools: e.g. web search
- prompt generator
- prompt improver


### Not as useful features
- prompt caching
- batch processing
- multilingual support
- token counting
- pdf
- file api: provide input, download output

# Pricing
https://docs.anthropic.com/en/docs/about-claude/pricing

