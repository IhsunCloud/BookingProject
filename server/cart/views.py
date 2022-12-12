from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.views import generic

from booking.models import Booking
from cart.cart import Cart
from cart.forms import CartAddBookingForm


class CartAddView(generic.View):

    def post(self, request, pk, *args, **kwargs):
        cart = Cart(request)
        booking = get_object_or_404(Booking, id = pk)
        form = CartAddBookingForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(
                booking = booking,
                booking_count = cd['booking_count'],
                update_count = cd['update']
            )
        return redirect('cart:cart_detail')


class CartRemoveView(generic.View):

    def post(self, request, booking_id, *args, **kwargs):
        cart = Cart(request)
        booking = get_object_or_404(Booking, id = booking_id)
        cart.remove(booking)
        return redirect('cart:cart_detail')


class CartDetailView(generic.View):
    template_name = 'pages/shop/cart.html'

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        
        for item in cart:
            item['update_booking_count_form'] = CartAddBookingForm(
                initial = {
                    'booking_count': item['booking_count'],
                    'update': True
                }
            )
        return render(request, 'pages/cart/detail.html', {'cart': cart})