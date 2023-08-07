import random
import datetime
from datetime import timezone
from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


# Create your views here.

class csrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return


class ShowMyBooks(APIView):
    def get(self, request):
        books = Book.objects.all()
        print(books)
        books = ListBookSerializer(books, many=True)
        return Response(books.data)


class ListBooks(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (csrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request):
        response = JSONParser().parse(request)
        serilizer = ListBookSerializer(data=response)

        if serilizer.is_valid():
            serilizer.save()

            return Response({
                "message": "Adding book Successful !",
                "code": 200
            }, status=status.HTTP_200_OK)

        return Response({
            "message": "An error occured !",
            "code": 400
        }, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return render(request, "index.html")


class AddBook(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (csrfExemptSessionAuthentication, BasicAuthentication)

    # def get(self,request):
    #
    #     issued=Book.objects.all()
    #     issued=ListBookSerializer(issued,many=True)
    #     return Response(issued.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ListBookSerializer(data=data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()

            return Response({
                "message": "post successfull !",
                "code": 200
            }, status=status.HTTP_200_OK)

        return Response({
            "message": "An error occured !",
            "code": 400
        }, status=status.HTTP_400_BAD_REQUEST)


class IssueBook(APIView):
    authentication_classes = (csrfExemptSessionAuthentication, BasicAuthentication)

    def getRandomID(self):
        return random.randint(10000, 99999)

    # Display all Books

    def get(self, request, studentid=None):

        if not studentid:
            issuedbooks = Issue.objects.all()

            books = BookSerializer(issuedbooks, many=True)

            return Response(books.data, status=status.HTTP_200_OK)

        # Return student record

        issuedbooks = Issue.objects.filter(studentid=studentid)

        if (len(issuedbooks) > 0):
            books = BookSerializer(issuedbooks, many=True)

            return Response(books.data, status=status.HTTP_200_OK)

        # Throw error when no books are issued

        return Response({
            "message": "Record not found",
            "status": 400
        }, status=status.HTTP_400_BAD_REQUEST)

    # def getDetails(self,studentid):
    #
    #     return Response(status=status.HTTP_200_OK)

    # Issue a Book

    def post(self, request):

        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.validated_data["studentid"] = self.getRandomID()
            serializer.save()

            return Response({
                "message": "Book Issued successfully !",
                "code": 200,
                "ID": self.getRandomID()
            }, status=status.HTTP_200_OK)

        return Response({
            "message": "An error occured !",
            "code": 400
        }, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):

        response = JSONParser().parse(request)

        issue = BookSerializer(data=response)

        if issue.is_valid():

            studentid = issue.data["studentid"]

            student = Issue.objects.filter(studentid=studentid)

            if (len(student) > 0):
                student = Issue.objects.filter(studentid=studentid)[0]

                student.name = issue.data["name"]
                student.isbn = issue.data["isbn"]
                student.branch = issue.data["branch"]
                student.rollno = issue.data["rollno"]
                student.issued = issue.data["issued"]
                student.submitdate = issue.data["submitdate"]

                student.save()
                return Response(status=status.HTTP_200_OK)

            return Response({
                "message": "Record not found",
                "status": 400
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):

        response = JSONParser().parse(request)

        issue = BookSerializer(data=response)

        if issue.is_valid():

            studentid = issue.data["studentid"]

            student = Issue.objects.filter(studentid=studentid)

            if (len(student) > 0):
                student = Issue.objects.filter(studentid=studentid)[0]

                student.delete()

                return Response(status=status.HTTP_200_OK)

            return Response({
                "message": "Record not found",
                "status": 400
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "message": "Bad request",
            "status": 400
        }, status=status.HTTP_400_BAD_REQUEST)


class SubmitBook(APIView):
    authentication_classes = (csrfExemptSessionAuthentication, BasicAuthentication,)

    def get(self, request):

        submitted = submit.objects.all()

        submitted = SubmitBookSerializer(submitted, many=True)

        return Response(submitted.data)

    def post(self, request):

        data = JSONParser().parse(request)

        data = SubmitBookSerializer(data=data)

        if data.is_valid():

            studentid = data.validated_data["studentid"]

            student = Issue.objects.filter(studentid=studentid)

            print(studentid)

            if (len(student) > 0):

                # student.delete()

                fine = 0

                print(datetime.datetime.now(timezone.utc).date(), data.validated_data["submitdate"].date())
                diff = (datetime.datetime.now(timezone.utc).date() - data.validated_data["submitdate"].date()).days

                if diff > 0:
                    fine = diff * 10

                data.validated_data["fine"] = fine

                data.save()

                return Response({
                    "message": "Book submitted successfully !",
                    "code": 200
                }, status=status.HTTP_200_OK)

            return Response({
                "message": "Record not found",
                "code": "400"
            }, status=status.HTTP_400_BAD_REQUEST)
