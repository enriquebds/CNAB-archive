from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadArchiveForm
from .models import UploadArchive, Cnab

# Create your views here.
def upload(req):

    if req.method == "POST":
        form = UploadArchive(req.POST, req.Files)
        file = req.Files["file"]

        archive = UploadArchive.objects.create(archive=file)
        archive.save()

        list = []
        with open(f"uploads/{str(archive.archive)}", "r", encoding="utf-8") as read:
             for file_line in read:
                list.append(file_line)
            
        for list_line in list:
            type   = list_line[:1]
            year   = list_line[1:5]
            month  = list_line[5:7]
            day    = list_line[7:9]
            value  = list_line[9:19]
            cpf    = list_line[19:30]
            card   = list_line[30:42]
            hour   = list_line[42:44]
            minute = list_line[44:46]
            second = list_line[46:48]
            owner  = list_line[48:62]
            store  = list_line[62:81]
            
            hour  = f"{hour}:{minute}:{second}"
            time  = f"{day}/{month}/{year}"
            value = int(value)/100

            if type == "1":
                type = "Débito"

            elif type == "2":
                type = "Boleto"

            elif type == "3":
                type = "Financiamento"

            elif type == "4":
                type = "Crédito"

            elif type == "5":
                type = "Empréstimo"

            elif type == "6":
                type = "Vendas"

            elif type == "7":
                type = "TED"

            elif type == "8":
                type = "DOC"

            elif type == "9":
                type = "Aluguel"

            reader = Cnab.objects.create(type=type, time=time, value=value, cpf=cpf, card=card, 
            hour=hour, owner=owner, store=store)

            reader.save()