from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai

# Load your OpenAI API key
with open("D:/react_django/openai_api_key.txt", "r") as file:
    openai_api_key = file.read().strip()

class gptResponse(APIView):
    def get(self, request):
        return Response({'message': 'Please use POST to submit text for a response.'}, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            # Retrieve text input from the request
            input_text = request.data.get('text', None)
            if not input_text:
                return Response({'error': 'No text provided.'}, status=status.HTTP_400_BAD_REQUEST)

            # Instantiate the OpenAI client
            client = openai.OpenAI(api_key=openai_api_key)

            # Make a request to OpenAI with the new chat completion API
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Specify the model you wish to use
                messages=[
                    {"role": "user", "content": input_text}
                ]
            )

            # Extract the response text
            generated_text = response.choices[0].message.content.strip()
            return Response({'response': generated_text}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
