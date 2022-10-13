from django.shortcuts import render
from .serializers import FreestyleSerializer, FSerializer
from .models import Freestyle
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def notes(request):
    if request.method == 'GET':
        try:
            notes = Freestyle.objects.filter(author=request.user)
            serializer = FreestyleSerializer(notes, many=True)
            print(serializer.data)
            return Response({
                'notes': serializer.data
                })
        except:
            return Response({
                'detail': 'Oops, something went wrong!-1'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        try:
            serializer = FreestyleSerializer(data=request.data)
            print(serializer)
            if serializer.is_valid():
                note = serializer.save(author=request.user)
                return Response({
                    'note': serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response({
                'details': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({
                'detail': 'Oops, something went wrong!-2'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def notes_remove(request, id):
    if request.method == 'DELETE':
        try:
            if not id:
                return Response({
                    'detail': 'Id field is required'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            note = Freestyle.objects.get(pk=id)

            if note.author != request.user:
                return Response({
                    'detail': 'You are not allowed to do that!'
                }, status=status.HTTP_403_FORBIDDEN)
            else:
                note.delete()
                return Response({
                    'detail': 'Your note has been deleted!'
                })
        except Freestyle.DoesNotExist:
            return Response({
                'detail': 'Object Not Found!'
            }, status=status.HTTP_404_NOT_FOUND) 
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
        fs1 = Freestyle.objects.filter(id=pk)

        # print(type(fs))
        # print("1 =",fs.id)
        # print(type(fs1))
        # print("2 =",fs1)
        # return Response('fs')
    except Freestyle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FreestyleSerializer(fs1, many=True)
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
        fs = Freestyle.objects.get(id=pk, author=request.user)
        serilizer = FSerializer(fs, many=False)
        return Response(serilizer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

 




