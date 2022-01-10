from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, BusinessForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
