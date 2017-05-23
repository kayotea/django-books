# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    
    return render(request, "book_app/index.html")

#test in shell:
    #  title="Harry Potter", author="J.K. Rowling", category="fantasy"
    #  title="Hitchhikder's Guide to the Galazy", author="That Guy", category="SciFi", in_print=True, published_date=
    # pub_date_string = "1978"
    # pub_date = datetime.strptime(pub_date_string, "%Y")
    # Book.objects.create(title="Hitchhikder's Guide to the Galazy", author="That Guy", category="SciFi", in_print=True, published_date=pub_date)
