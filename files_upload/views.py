from django.shortcuts import render
from django.http import HttpResponse
from CNAB.utils.parser import parserCNAB
from donos_loja.serializers import DonoSerializer, Dono_loja
from CNAB.serializers import CNABSerializer, Cnab
from django.forms.models import model_to_dict


def home(req):
    return render(req, "index.html")


def process_form(req):

    txt = req.FILES["file"].readlines()
    decoded_txt = [
        parserCNAB(line.decode("utf-8").replace("\r", "").replace("\n", ""))
        for line in txt
    ]

    for parsed in decoded_txt:
        dono_data = {
            "dono_da_loja": parsed.pop("dono_da_loja"),
            "nome_da_loja": parsed.pop("nome_da_loja"),
        }
        dono = DonoSerializer(data=dono_data)
        dono.is_valid(raise_exception=True)
        dono.save()

        parsed["dono"] = dono.data["id"]
        cnab = CNABSerializer(data=parsed)
        cnab.is_valid(raise_exception=True)
        cnab.save()

    negative_status = [2, 3, 9]

    dono_db = Dono_loja.objects.all()
    list_dono = []

    for dono in dono_db:
        dono_cnabs = Cnab.objects.all().filter(dono_id=dono.id)
        balance = 0
        operations = []
        for cnab in dono_cnabs:
            cnab_dict = model_to_dict(cnab)
            if cnab_dict["tipo"] in negative_status:
                balance -= cnab_dict["valor"]
            else:
                balance += cnab_dict["valor"]
            operations.append(cnab_dict)

        list_dono.append(
            {
                "dono": dono.dono_da_loja,
                "nome_da_loja": dono.nome_da_loja,
                "balance": round(balance, 2),
                "operations": operations,
            }
        )

    return render(req, "status.html", {"list": list_dono})
