#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ollama import chat

class plaintext_fix(object):
    def __init__(self):
        self.system_prompt = "Tu es un chatbot qui corrige chaque entrée en la rendant concise et claire. Tu réponds uniquement par la correction. Tu ne fais aucun commentaire et n'ajoutes rien d'autre."


    def fix(self,
            plaintext: str
            ) -> str:

        """
        This function takes a string as input and returns a corrected version of the string.
        It uses the Llama 3.2 model to perform the correction.
          You can use the following models:
          # model='llama3.2:3b-instruct-q6_K'
          # model='llama3.2:3b-instruct-q8_0'
          (good results and fast)

        Usage:
        plaintext_fix.fix(plaintext)
        _________________________________________________________
        Args:
            plaintext (str): The input string to be corrected.
        Returns:
            str: The corrected string.

        """

        stream = chat(
            model='llama3.2:3b-instruct-q8_0',
            messages=[
              {'role': 'system', 'content': f'{self.system_prompt}'},
              {'role': 'user', 'content': f'{plaintext}'}
            ],
            stream=True,
            options={
                'temperature': 0.15,
                'top_p': 0.95,
                'top_k': 40,
                'repetition_penalty': 1.1,
                'max_new_tokens': 200,
                'stop': ['\n', '</s>'],
            },
        )

        for chunk in stream:
            yield chunk['message']['content']


if __name__ == "__main__":
    # Example usage
    plaintext = "Bon, La voitur et en panne, le micronde ossi !"
    for chunk in plaintext_fix().fix(plaintext):
        print(chunk, end='', flush=True)

