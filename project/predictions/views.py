from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import torch
from torchvision import models, transforms
from PIL import Image

model = models.resnet18(pretrained=True)
model.eval()

class PredictView(APIView):
    def get(self, request):
        return Response({'message': 'Please use POST to submit an image for prediction.'}, status=status.HTTP_200_OK)


    def post(self, request):
        try:
            input_data = request.FILES['file']
        
            # if not input_data.content_type.startswith('image/'):
            #     return Response({'error': 'Invalid file type. Please upload an image.'}, status=status.HTTP_400_BAD_REQUEST)

        
            image = Image.open(input_data)
            

            preprocess = transforms.Compose([
                transforms.Resize(256),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ])
            input_tensor = preprocess(image)
            input_batch = input_tensor.unsqueeze(0)

            with torch.no_grad():
                output = model(input_batch)


            _, predicted = torch.max(output, 1)
            image.close()
            return Response({'prediction': predicted.item()}, status=status.HTTP_200_OK)
        except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)