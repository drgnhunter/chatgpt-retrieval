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
def rename_variables(*variables):
    """Extract the variables"""
    variable_dict = {name: None for name in variables}
    return json.dumps(variable_dict)

def run_conversation():
    # Step 1: send the conversation and available functions to GPT
    question = """Two particles A and B of masses 2m and m respectively, moving towards each other with the
same speed u along a smooth horizontal table collide in a simple collision. Moments after the collision,
particle A comes to rest. Show that the coefficient of restitution = and the magnitude of
the impulse on B due to the collision is 2mu."""

    messages = [{"role": "user", "content": "Don't solve the question.Find the variables in this question and Rename the variables to  the given format  "+question}]
    functions = [
        {
            "name": "get_variables",
            "description": "Extract the variables, Rename all the particle masses to m1,m2,m3,.., Rename initial Velocity of m1 to u1 , initial velcoity of m2 to v1, the final velocity of m1 to x1, final velocity of m2 to y1, Coefficient of restitution to e and put them in the given format. Variable Name : Value .  ",
            "parameters": {
                "type": "object",
                "properties": {
                    "m1": {
                        "type": "string",
                        "description": "Mass of particle m1",
                    },
                    "m2":{
                        "type": "string",
                        "description": "Mass of particle m2",
                    },
                     "m3": {
                        "type": "string",
                        "description": "Mass of particle m3",
                    },
                    "u1":{
                        "type": "string",
                        "description": "Initial velocity of m1",
                    },
                     "v1":{
                        "type": "string",
                        "description": "Initial velocity of m2",
                    },
                      "x1":{
                        "type": "string",
                        "description": "Final velocity of m1",
                    },
                     "y1":{
                        "type": "string",
                        "description": "Final velocity of m2",
                    },
                     "e":{
                        "type": "string",
                        "description": "Coefficient of restitution",
                    }
                },
                "required": ["m1"],
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

        # messages2 = [{"role": "user", "content": "Rename the variables to  the given format "+function_args}]
        # functions2 = [
        # {
        #     "name": "rename_variables",
        #     "description": "All the particle mass names should be m1,m2,m3...  ",
        #     "parameters": {
        #         "type": "object",
        #         "properties": {
        #             "m1": {
        #                 "type": "string",
        #                 "description": "Mass of particle m1",
        #             },
        #             "m2":{
        #                 "type": "string",
        #                 "description": "m2",
        #             },
        #              "Particle C mass": {
        #                 "type": "string",
        #                 "description": "Mass of particle C",
        #             },
        #             "Initial velocity of A":{
        #                 "type": "string",
        #                 "description": "Initial velocity of A",
        #             },
        #              "Coefficient of restitution between A and B":{
        #                 "type": "string",
        #                 "description": "Coefficient of restitution between A and B",
        #             },                   
        #               "Coefficient of restitution between B and C":{
        #                 "type": "string",
        #                 "description": "Coefficient of restitution between B and C",
        #             },
        #         },
        #         "required": ["Particle A mass"],
        #     },
        #     }
        # ]
    
        # response = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo-0613",
        # messages=messages,
        # functions=functions,
        # function_call="auto",  # auto is default, but we'll be explicit
        # )
        # response_message = response["choices"][0]["message"]

        # print(response_message)

        # # Step 2: check if GPT wanted to call a function
        # if response_message.get("function_call"):
        #     # Step 3: call the function
        #     # Note: the JSON response may not always be valid; be sure to handle errors
        #     available_functions = {
        #         "get_variables": get_variables,
        #     }  # only one function in this example, but you can have multiple
        #     function_name = response_message["function_call"]["name"]
        #     fuction_to_call = available_functions[function_name]
        #     function_args = json.loads(response_message["function_call"]["arguments"])
        #     # function_response = fuction_to_call(
        #     #     location=function_args.get("location"),
        #     #     unit=function_args.get("unit"),
        #     # )
        #     print("Variable JSON => ",function_args)


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