from django.shortcuts import render
from.forms import NewUserForm, Login, CreateHouse, CreateBudget, CreateBudgetItem
from django.contrib.auth import login, logout, authenticate, models
import datetime as dt


# @login_required(Login_url="registration/login")
def index(response):
    return render(response, "main/index.html")


def register(response):
    if response.method == "POST":
        form = NewUserForm(response.POST)
        if form.is_valid():
            user = models.User()
            user.first_name = form.first_name
            user.last_name = form.last_name
            user.email = form.email
            user.password = form.password1
            user.date_joined = dt.datetime.now()
            user.is_superuser = 0
            email = form.email
            user.username = email.split('@', [0])
    form = NewUserForm()
    return render(response, "registration/register.html", {"form": form})


# def login(response):
#     if response.method == "POST":
#         form = Login(response.POST)
#         if form.is_valid():
#             pass
#         else:
#             form = Login()
#             error_message = "Error authenticating, please contact support for assistance"
#             render(response, "registration/login.html", {"form": form}, {"error": error_message})
#     else:
#         form = Login()
#         render(response, "registration/login.html", {"form": form})



