from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Person, Ticket, Movie
from rest_framework import status
from rest_framework.response import Response
from .serializer import PersonSerializer,TicketSerializer,MovieSerializer

from rest_framework import filters
from rest_framework.generics import ListAPIView
# Create your views here.
@csrf_exempt
def submit(request):
    return render(request,'output.html',{})
@csrf_exempt
def Ticket_List(request):

    if request.method == 'GET':
        tickets= Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method=='POST':
        #data = JSONParser().parse(request)
         #serializer=TicketSerializer(data=data)
         # if serializer.is_valid():
         #   serializer.save()
         #   return JsonResponse(serializer.data,status=201)

        form_data = {}
        form_data = JSONParser().parse(request)
        person = Person.objects.get(p_id=form_data["p_id"])
        movie = Movie.objects.get(m_id=form_data["m_id"])
        ticket= Ticket(expired=form_data["expired"],
                       person=person,
                       start_time=form_data["start_time"],
                       movie=movie,
                       end_time=form_data["end_time"])
        ticket.save()
        return HttpResponse(status=201)
@csrf_exempt
def Ticket_details (request, pk):
    try:
        ticket = Ticket.objects.get(pk=pk)
    except Ticket.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TicketSerializer(ticket)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TicketSerializer(ticket, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.data,status=400)

    elif request.method=='DELETE':
        ticket.delete()
        return HttpResponse(status=204)

@csrf_exempt
def Person_List (request):

    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.data,status=400)
@csrf_exempt
def Person_details (request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':

        serializer = PersonSerializer(person)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PersonSerializer(person,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.data,status=400)

    elif request.method == 'DELETE':
        person.delete()
        return HttpResponse(status=204)
@csrf_exempt
def Movie_List(request):

    if request.method =='GET':
        movies= Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method =='POST':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.data,status=400)
@csrf_exempt
def Movie_details (request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(movie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.data,status=400)

    elif request.method == 'DELETE':
        movie.delete()
        return HttpResponse(status=204)
@csrf_exempt
def Ticket_filter (request,id):
    if request.method == 'GET':
        queryset = Ticket.objects.all()
        user_id = int(id)
        queryset2 = queryset.filter(p_id=user_id)
        serializer = PersonSerializer(queryset2, many=True)
    return JsonResponse(serializer.data, safe=False)

















