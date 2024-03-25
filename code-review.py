#!/Users/krystofrehacek/Repos/code-review/.venv/bin/python3

import os
import anthropic

# Generate git diff with master branch and save it to a temporary file
os.system("git diff -U10 master > temp_diff.txt")

# Read the git diff from the temporary file
with open("temp_diff.txt", "r") as file:
    git_diff = file.read()

# Delete the temporary file
os.remove("temp_diff.txt")

# Prepare the prompt for code review
prompt = f"""Git diff:
{git_diff}

Create a code review of changes in the git diff above. If there is no git diff provided, state that you cannot perform the task due to missing information.

Optimize for reducing complexity in the code. Analyze the solutions used and identify pros and cons. If the solution can be implemented more efficiently or with less complexity, suggest alternative way and provide code example which precisely describes it. Prioritize reducing bug-prone code over performance.

As the codebase is in Python and Typescript, check for the following issues:
1. Leaked tokens
2. Views without login required in improper files
3. Serializing of credentials or other sensitive data in serializers

Evaluate the future impact and potential evolution of the software. Assess the complexity and knowledge required to understand the code. Favor solutions that require coherent knowledge in one place and less overall knowledge to understand.

Estimate the complexity and knowledge values relatively and include them in the review.

Also, try to find bugs and potential issues in the code and address them. Optimize the code where possible using the methods and APIs that are accessible in the current context.

Lastly for each block of code, if there is some standard library API to achieve some functionality more efficiently or on fewer lines, suggest better solution and provide code.

Whenever you suggest change to the code such as refactor something or better solution, provide code example that describes the change on the generic example and specific from the code you have seen.

Don't write feedback for each changed file but think about the overall design and architecture of the codebase and how it can be improved."""

print("Generating code review...")

# Call the Anthropic Opus 3 model for code review
response = anthropic.Anthropic().messages.create(
    model="claude-3-opus-20240229",
    max_tokens=4096,
    system="You are a professional python and typescript fullstack programmer. Here, you are reviewing a merge request. Output in markdown format.",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Extract the code review from the response
code_review = response.content[0].text

# Save the code review to a markdown file
with open("merge-request-review.md", "w") as file:
    file.write(code_review)

print("Code review saved to merge-request-review.md")
