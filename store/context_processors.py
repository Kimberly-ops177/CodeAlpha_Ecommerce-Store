from .models import Cart, Order

def cart_and_orders_context(request):
    """
    Context processor to add cart item count and ongoing orders count to all templates
    """
    context = {
        'cart_count': 0,
        'ongoing_orders_count': 0,
    }

    if request.user.is_authenticated:
        # Get cart item count
        try:
            cart = Cart.objects.get(user=request.user)
            context['cart_count'] = sum(item.quantity for item in cart.items.all())
        except Cart.DoesNotExist:
            context['cart_count'] = 0

        # Get ongoing orders count (pending, processing, ready_for_pickup, shipped)
        ongoing_orders = Order.objects.filter(
            user=request.user,
            status__in=['pending', 'processing', 'ready_for_pickup', 'shipped']
        ).count()
        context['ongoing_orders_count'] = ongoing_orders

    return context
