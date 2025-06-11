from django.shortcuts import render
from .models import Market, Product

def index(request):
    return render(request, 'index.html')

def markets(request):
    markets = Market.objects.all()
    return render(request, 'market/markets.html', {'markets': markets})
 
def markets_detail(request, slug):
    try:
        market = Market.objects.get(slug=slug)
    except Market.DoesNotExist:
        return render(request, 'not_found.html')

    products = Product.objects.filter(market=market)
    return render(request, 'market/market_detail.html', {'market': market, 'products': products})

def product_detail(request, slug, product_id):
    try:
        market = Market.objects.get(slug=slug)
        product = Product.objects.get(id=product_id, market=market)
    except Product.DoesNotExist:
        return render(request, 'not_found.html')
    except Market.DoesNotExist:
        return render(request, 'not_found.html')
    return render(request, 'market/product_detail.html', {'product': product, 'market': market})