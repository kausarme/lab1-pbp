from django.shortcuts import render
from wishlist.models import BarangWishlist

# Create your views here.
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': barangwishlist,
        'nama': 'Kausar Meutuwah'
    }
    return render(request, "wishlist.html", context)


