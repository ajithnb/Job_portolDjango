
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

# Create your views here.


class Jobportol(View):
    def get(self, request):
        data = {
            "Message": "find Jobs here..!"
        }

        return JsonResponse(data)


class CompanyView(View):
    def get(self, request):
        data = {
            "Company_Name": "Tech Solutions",
            "Location": "Kochi",
            "Contact": "9876543210",
            "Industry": "IT",
            "Status": "Hiring"
        }

        return JsonResponse(data)


class JobView(View):
    def get(self, request):
        data = {
            "Job_Title": "Python Developer",
            "Company": "Tech Solutions",
            "Location": "Kochi",
            "Salary": 30000,
            "Job_Type": "Full Time",
            "Experience": "Fresher",
            "Description": "Looking for a Python Django developer"
        }

        return JsonResponse(data)


class CandidateView(View):
    def get(self, request):
        data = {
            "Name": "Ajith",
            "Qualification": "BCA",
            "Skills": "Python, Django, MySQL",
            "Experience": "Fresher",
            "Location": "Idukki",
            "Mobile": 9876543210,
            "Email": "ajith@gmail.com"
        }

        return JsonResponse(data)


class JobsView(View):
    def get(self, request):
        data = {
            "Jobs": [
                "Python Developer",
                "Java Developer",
                "Frontend Developer",
                "Web Designer",
                "Software Tester"
            ]
        }

        return JsonResponse(data)


class EmployeeView(View):
    def get(self, request):
        data = {
            "id": "1",
            "name": "Rahul",
            "designation": "Python Developer",
            "company": "ABC Technologies",
            "salary": 35000,
            "experience": "2 years",
            "qualification": "BCA",
            "location": "Kochi"
        }

        return JsonResponse(data)


class ApplicationView(View):
    def get(self, request):
        data = {
            "Application_ID": 101,
            "Candidate_Name": "Ajith",
            "Job_Title": "Python Developer",
            "Company": "Tech Solutions",
            "Application_Status": "Pending",
            "Applied_Date": "05/11/2026"
        }

        return JsonResponse(data)


class RecruiterView(View):
    def get(self, request):
        data = {
            "Recruiter_Name": "Arun",
            "Company": "Tech Solutions",
            "Email": "arun@gmail.com",
            "Contact": "9876543210",
            "Location": "Kochi"
        }

        return JsonResponse(data)