"""
AI service
"""

from openai import OpenAI

client=OpenAI()

def generate_summary(data):
    """
    Generate summary
    """
    
    prompt=f"""

    Release Score:{data['score']}

    Blockers:{data['blockers']}

    Explain release readiness.

    """

    response=client.responses.create(

        model="gpt-4.1",

        input=prompt

    )

    return response.output_text
