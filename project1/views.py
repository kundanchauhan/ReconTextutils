from django.core.files.storage import FileSystemStorage
from django.conf.urls.static import static
from django.conf import settings
from pylovepdf.ilovepdf import ILovePdf
import requests
import json
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render
import http.client
import mimetypes

import ssl
ssl.match_hostname = lambda cert, hostname: True

your_media_root = settings.MEDIA_ROOT

# from django.http import requests


def index(request):
    return render(request, 'homepage.html')


def textutiles(request):
    return render(request, 'index.html')




def analyze(request):
    mera_text = request.POST.get('input_text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    numberremover = request.POST.get('numberremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # print(mera_text)

    if(removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and numberremover != "on" and lowercase !="on"):
        return render(request, 'error.html')
        return render(request, 'analyzed.html', params)

    elif removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        # print(analyzed)
        for char in mera_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyzed.html', params)

    elif(fullcaps == "on"):
        analyzed = ''
        for char in mera_text:
            analyzed = analyzed + char.upper()
            params = {'purpose': 'Upper Case', 'analyzed_text': analyzed}

        return render(request, 'analyzed.html', params)

    elif(lowercase == "on"):
        analyzed = ''
        for char in mera_text:
            analyzed = analyzed + char.lower()
            params = {'purpose': 'lower Case', 'analyzed_text': analyzed}
            print(analyzed)
        return render(request, 'analyzed.html', params)

    elif (newlineremover == "on"):
        analyzed = ''
        for char in mera_text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}

        return render(request, 'analyzed.html', params)

    elif(extraspaceremover == "on"):
        analyzed = ''
        for index, char in enumerate(mera_text):
            if not(mera_text[index] == ' ' and mera_text[index+1] == ' '):
                analyzed = analyzed + char
            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        return render(request, 'analyzed.html', params)

    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in mera_text:
            if char not in numbers:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Number', 'analyzed_text': analyzed}

        return render(request, 'analyzed.html', params)

    else:
        return HttpResponse("Error")


def codebeautifier(request):


    mera_text = request.POST.get('input_text', "")

    style_result = request.POST.get('style',False)
    language_result = request.POST.get('language',False)
    linenos_result= request.POST.get('linenos',"")


    style = request.POST.get('style', 'style_result')
    language = request.POST.get('language', 'language_result')
    # linenos = request.POST.get('linenos', 'linenos_result')


    url = "http://hilite.me/api?code="


    payload = {}
    headers = {}
    response = requests.request("GET", url+mera_text+"&language="+language +
                                "&style="+style+"&linenos="+linenos_result,headers=headers, data=payload)
    pretty = response.text
    foundAt = pretty.find('>')
    pretty = pretty[foundAt+1:]
    final_out = ("<!-- HTML generated using Recon Utility -->"+pretty)
    dictToSend = {'color_text': final_out}
    return render(request, 'codebeautifier.html', dictToSend)


def dashboard(request):
    return render(request, 'dashboard.html')


def mergepdf(request):
    if request.method == 'POST' and request.FILES['pdf1'] and request.FILES['pdf2']:
        pdf1 = request.FILES['pdf1']
        pdf2 = request.FILES['pdf2']
        fs = FileSystemStorage()
        filename = fs.save(pdf1.name, pdf1)
        uploaded_file_url = fs.url(filename)

        fs2 = FileSystemStorage()
        filename = fs2.save(pdf2.name, pdf2)
        uploaded_file_url2 = fs.url(filename)
        print(type(uploaded_file_url))
        ilovepdf = ILovePdf(
            'project_public_770e56f3152d401d6476b9be1800d6c4_4byne2d937ca7d5ea33974126f444d2c1166e', verify_ssl=True)
        task = ilovepdf.new_task('merge')
        task.add_file("/home/kundan/env1/project1"+uploaded_file_url)
        task.add_file("/home/kundan/env1/project1"+uploaded_file_url2)

        task.set_output_folder('/home/kundan/Desktop/CP')
        task.execute()
        task.download()
        task.delete_current_task()
        return render(request, 'mergepdf.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'mergepdf.html')

# /home/kundan/env1/project1/media/08Growth & Development_English_1560506778_roCvcg6.pdf

# def mergepdf(request):
#     ilovepdf = ILovePdf(
#         'project_public_770e56f3152d401d6476b9be1800d6c4_4byne2d937ca7d5ea33974126f444d2c1166e', verify_ssl=True)
#     task = ilovepdf.new_task('compress')
#     print(request.method)
#     if request.method == 'POST' and request.FILES['pdf1']:
#         pdf1 = request.FILES['pdf1']
#         fs = FileSystemStorage()
#         filename = fs.save(pdf1.name, pdf1)
#         print("this is file name  " + filename)
#         uploaded_file_url = fs.url(filename)
#         print("file urls  name    :"+uploaded_file_url)
#         task.add_file(uploaded_file_url)

#         # task.execute()
#         # task.set_output_folder('/home/kundan/Downloads/download_pdffile')
#         # task.execute()
#         # task.download()
#         # task.delete_current_task()
#     return render(request, 'mergepdf.html')


def unlock(request):
    if request.method == 'POST' and request.FILES['pdf1']:
        pdf1 = request.FILES['pdf1']
        fs = FileSystemStorage()
        filename = fs.save(pdf1.name, pdf1)
        uploaded_file_url = fs.url(filename)
        print(type(uploaded_file_url))
        ilovepdf = ILovePdf(
            'project_public_770e56f3152d401d6476b9be1800d6c4_4byne2d937ca7d5ea33974126f444d2c1166e', verify_ssl=True)
        task = ilovepdf.new_task('unlock')
        task.add_file("/home/kundan/env1/project1"+uploaded_file_url)
        task.debug = False
        task.set_output_folder('/home/kundan/Desktop/CP')
        task.execute()
        task.download()
        task.delete_current_task()
        return render(request, 'unlock.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'unlock.html')


def compress(request):
    if request.method == 'POST' and request.FILES['pdf1']:
        pdf1 = request.FILES['pdf1']
        fs = FileSystemStorage()
        filename = fs.save(pdf1.name, pdf1)
        uploaded_file_url = fs.url(filename)

        ilovepdf = ILovePdf(
            'project_public_770e56f3152d401d6476b9be1800d6c4_4byne2d937ca7d5ea33974126f444d2c1166e', verify_ssl=True)
        task = ilovepdf.new_task('compress')
        task.add_file("/home/kundan/env1/project1"+uploaded_file_url)

        task.set_output_folder('/home/kundan/Desktop/CP')
        task.execute()
        task.download()
        task.delete_current_task()
        return render(request, 'compress.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'compress.html')


def lock(request):
    if request.method == 'POST' and request.FILES['pdf1']:
        lock_pdf = request.POST.get('password_text', 'default')
        pdf1 = request.FILES['pdf1']
        fs = FileSystemStorage()
        filename = fs.save(pdf1.name, pdf1)
        uploaded_file_url = fs.url(filename)
        print(type(uploaded_file_url))
        ilovepdf = ILovePdf(
            'project_public_770e56f3152d401d6476b9be1800d6c4_4byne2d937ca7d5ea33974126f444d2c1166e', verify_ssl=True)
        task = ilovepdf.new_task('protect')
        file_my_path = "/home/kundan/env1/project1"+uploaded_file_url
        task.add_file(file_my_path,
                      )
        task.file_encryption_key = 'ciao'

        task.file.password = lock_pdf
        task.set_output_folder('/home/kundan/Desktop/CP')

        task.execute()
        task.download()
        task.delete_current_task()
        return render(request, 'lock.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'lock.html')
