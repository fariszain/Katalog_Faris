from django.shortcuts import render, Http404

# Data Produk (Hardcoded)
DATA_PRODUK = [
    {'id': 1, 'nama': 'Laptop Gaming', 'harga': 'Rp 15.000.000', 'deskripsi': 'Laptop spek dewa untuk gaming.'},
    {'id': 2, 'nama': 'Mouse Wireless', 'harga': 'Rp 250.000', 'deskripsi': 'Mouse responsif tanpa kabel.'},
    {'id': 3, 'nama': 'Keyboard Mekanik', 'harga': 'Rp 800.000', 'deskripsi': 'Keyboard dengan switch biru yang clicky.'},
]

def home(request):
    return render(request, 'home.html')

def produk_list(request):
    context = {'produk': DATA_PRODUK}
    return render(request, 'produk_list.html', context)

def produk_detail(request, id):
    # Mencari produk berdasarkan ID
    produk = next((item for item in DATA_PRODUK if item['id'] == id), None)
    if produk:
        return render(request, 'produk_detail.html', {'produk': produk})
    raise Http404("Produk tidak ditemukan")

def kontak(request):
    return render(request, 'kontak.html')