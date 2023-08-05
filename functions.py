import openai
import json
import traceback
import sys

import os
import sys
import constants

openai.api_key = "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"
# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
def get_variables(*variables):
    """Extract the variables"""
    variable_dict = {name: None for name in variables}
    return json.dumps(variable_dict)


def run_conversation():
    # Step 1: send the conversation and available functions to GPT
    question = """Three particles A, B and C, each of mass m, are placed in that
order, in a straight line on a smooth horizontal table. The particle A is given a velocity 'u' such
that it collides directly with the particle B. After colliding with the particle A, the particle B
moves and collides directly with the particle C. The coefficient of restitution between A and B is e.
Find the velocity of B after the first collision.

The coefficient of restitution between B and C is also e. Write down the velocity of C after its
collision with B."""

    messages = [{"role": "user", "content": "Don't solve the question.What are the variables in this question? "+question}]
    functions = [
        {
            "name": "get_variables",
            "description": "Extract the variables and put them in the given format. Variable Name : Value",
            "parameters": {
                "type": "object",
                "properties": {
                    "Particle A mass": {
                        "type": "string",
                        "description": "Mass of particle A",
                    },
                    "Particle B mass":{
                        "type": "string",
                        "description": "Mass of particle B",
                    },
                     "Particle C mass": {
                        "type": "string",
                        "description": "Mass of particle C",
                    },
                    "Initial velocity of A":{
                        "type": "string",
                        "description": "Initial velocity of A",
                    },
                     "Coefficient of restitution between A and B":{
                        "type": "string",
                        "description": "Coefficient of restitution between A and B",
                    },                   
                      "Coefficient of restitution between B and C":{
                        "type": "string",
                        "description": "Coefficient of restitution between B and C",
                    },
                },
                "required": ["Particle A mass"],
            },
        }
    ]
    
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=messages,
    functions=functions,
    function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]

    print(response_message)

    # Step 2: check if GPT wanted to call a function
    if response_message.get("function_call"):
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "get_variables": get_variables,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        # function_response = fuction_to_call(
        #     location=function_args.get("location"),
        #     unit=function_args.get("unit"),
        # )
        print("Variable JSON => ",function_args)

        # # Step 4: send the info on the function call and function response to GPT
        # messages.append(response_message)  # extend conversation with assistant's reply
        # messages.append(
        #     {
        #         "role": "function",
        #         "name": function_name,
        #         "content": function_response,
        #     }
        # )  # extend conversation with function response
        # second_response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo-0613",
        #     messages=messages,
        # )  # get a new response from GPT where it can see the function response
        # return second_response

# run_conversation()
print(run_conversation())