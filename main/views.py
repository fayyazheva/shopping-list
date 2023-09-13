from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Fayya Salwa Azheva', # Nama kamu
        'class': 'PBP B', # Kelas PBP kamu
        'products': products
    }

    return render(request, "main.html", context)

# Fungsi Product.objects.all() digunakan untuk mengambil seluruh object Product yang tersimpan pada database.

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)\

def show_xml(request):
    data = Product.objects.all()

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# from django.shortcuts import render berguna untuk mengimpor fungsi render dari modul django.shortcuts. Fungsi render digunakan untuk me-render tampilan HTML dengan menggunakan data yang diberikan.
# def show_main(request) merupakan deklarasi fungsi show_main, yang menerima parameter request. Fungsi ini akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai.

# context adalah dictionary yang berisi data yang akan dikirimkan ke tampilan. Pada konteks ini, dua data disertakan, yaitu:

# name: Data nama.
# class: Data kelas.
# return render(request, "main.html", context) berguna untuk me-render tampilan main.html dengan menggunakan fungsi render. Fungsi render mengambil tiga argumen:

# request: Ini adalah objek permintaan HTTP yang dikirim oleh pengguna.
# main.html: Ini adalah nama berkas template yang akan digunakan untuk me-render tampilan.
# context: Ini adalah dictionary yang berisi data yang akan diteruskan ke tampilan untuk digunakan dalam penampilan dinamis.

# form = ProductForm(request.POST or None) digunakan untuk membuat ProductForm baru dengan memasukkan QueryDict berdasarkan input dari user pada request.POST.
# form.is_valid() digunakan untuk memvalidasi isi input dari form tersebut.
# form.save() digunakan untuk membuat dan menyimpan data dari form tersebut.
# return HttpResponseRedirect(reverse('main:show_main')) digunakan untuk melakukan redirect setelah data form berhasil disimpan.

# serializers digunakan untuk translate objek model menjadi format lain seperti dalam fungsi ini adalah XML.