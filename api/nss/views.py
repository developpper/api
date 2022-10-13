from django.shortcuts import render
from .serializers import AmazonProductsSerializer
from .models import AmazonProducts
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.parsers import JSONParser 
from django.http.response import JsonResponse



# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def amazon_products(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = AmazonProducts.objects.all()
#         serializer = AmazonProductsSerializer(snippets, many=True)
#         return Response({
#                 'amazon': serializer.data
#                 })

#     elif request.method == 'POST':
#         serializer = AmazonProductsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def amazon_products(request):
    if request.method == 'GET':
        try:
            notes = AmazonProducts.objects.all()
            serializer = AmazonProductsSerializer(notes, many=True)
            print(serializer.data)
            # print(serializer.data)
            return Response({
                'amazon': serializer.data
                })
        except:
            return Response({
                'detail': 'Oops, something went wrong!-1'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        print(tutorial_data)
        tutorial_serializer = AmazonProductsSerializer(data=tutorial_data)
    if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

    # elif request.method == 'POST':
    #     try:
    #         serializer = AmazonProductsSerializer(data=request.data)
    #         print(serializer)
    #         if serializer.is_valid():
    #             serializer.save(author=request.user)
    #             return Response({
    #                 'note': serializer.data
    #             }, status=status.HTTP_201_CREATED)
    #         return Response({
    #             'details': serializer.errors
    #         }, status=status.HTTP_400_BAD_REQUEST)
        # except:
        #     return Response({
        #         'detail': 'Oops, something went wrong!-2'
        #     }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def notes_remove(request, id):
    if request.method == 'DELETE':
        try:
            note = AmazonProducts.objects.get(pk=id)
            note.delete()
            return Response({
                'detail': id+'has been deleted'
                }, status=status.HTTP_404_NOT_FOUND) 
        #     if not id:
        #         return Response({
        #             'detail': 'Id field is required'
        #         }, status=status.HTTP_400_BAD_REQUEST)
            
        #     note = AmazonProducts.objects.get(pk=id)

        #     if note.author != request.user:
        #         return Response({
        #             'detail': 'You are not allowed to do that!'
        #         }, status=status.HTTP_403_FORBIDDEN)
        #     else:
        #         note.delete()
        #         return Response({
        #             'detail': 'Your note has been deleted!'
        #         })
        # except AmazonProducts.DoesNotExist:
        #     return Response({
        #         'detail': 'Object Not Found!'
        #     }, status=status.HTTP_404_NOT_FOUND) 
        except:
            return Response({
                'detail': 'Oops, something went wrong!'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def fs_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    # print(pk)
    try:
        # fs = Freestyle.objects.get(id=pk)
        fs1 = AmazonProducts.objects.filter(id=pk)

        # print(type(fs))
        # print("1 =",fs.id)
        # print(type(fs1))
        # print("2 =",fs1)
        # return Response('fs')
    except AmazonProducts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AmazonProductsSerializer(fs1, many=True)
        return Response(serializer.data)

    # elif request.method == 'PUT':
    #     serializer = FreestyleSerializer(fs1, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     fs1.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def showSingleFS(request, pk):
    try:
        fs = AmazonProducts.objects.get(id=pk, author=request.user)
        serilizer = AmazonProductsSerializer(fs, many=False)
        return Response(serilizer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)



@permission_classes([IsAuthenticated])
@api_view(['GET'])
def showSingleAM(request, pk):
    try:
        fs = AmazonProducts.objects.get(id=pk)
        serilizer = AmazonProductsSerializer(fs, many=False)
        print(serilizer.data)
        return Response(serilizer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

 

from selectorlib import Extractor
import requests 
import json 
from time import sleep
import yaml
import os
# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('selectors.yml')

# def scrape(url):  

#     headers = {
#         'dnt': '1',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'sec-fetch-site': 'same-origin',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-user': '?1',
#         'sec-fetch-dest': 'document',
#         'referer': 'https://www.amazon.com/',
#         'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
#     }

#     # Download the page using requests
#     print("Downloading %s"%url)
#     r = requests.get(url, headers=headers)
#     # Simple check to check if page was blocked (Usually 503)
#     if r.status_code > 500:
#         if "To discuss automated access to Amazon data please contact" in r.text:
#             print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
#         else:
#             print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
#         return None
#     # Pass the HTML of the page and create 
#     return e.extract(r.text)

# # product_data = []
# # with open("urls.txt",'r') as urllist, open('output.jsonl','w') as outfile:
#     for url in urllist.read().splitlines():
#         data = scrape(url) 
#         if data:
#             json.dump(data,outfile)
#             outfile.write("\n")
#             # sleep(5)






@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def scrape(request):
    if request.method == 'GET':
        try:
            notes = AmazonProducts.objects.all()
            serializer = AmazonProductsSerializer(notes, many=True)
            print(serializer.data)
            # print(serializer.data)
            return Response({
                'amazon': serializer.data
                })
        except:
            return Response({
                'detail': 'Oops, something went wrong!-1'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        print(tutorial_data)
        tutorial_serializer = AmazonProductsSerializer(data=tutorial_data)
    if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def ap(request):
    if request.method == 'GET':
        try:
            notes = AmazonProducts.objects.all()
            serializer = AmazonProductsSerializer(notes, many=True)
            print(serializer.data)
            # print(serializer.data)
            return Response({
                'amazon': 'yes'
                })
            # with open('selectors.yaml') as file:
            #     data = yaml.safe_load(file)
            #     for key, value in data.items():
            #         print(key, ":", value)
            #         return Response({
            #         'amazon': 'yup'
            #         })
        except:
            return Response({
                'detail': 'Oops, something went wrong!-1'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        print(tutorial_data)
        tutorial_serializer = AmazonProductsSerializer(data=tutorial_data)
    if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @permission_classes([])
def sc(request):
    print('hello')
    return render(request, 'index.html')