from decimal import Decimal
from django.shortcuts import get_object_or_404
from courses.models import Course


def bag_contents(request):

    bag_items = []
    total = 0
    course_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        course = get_object_or_404(Course, pk=item_id)
        total += quantity * course.price
        course_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'course': course,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'course_count': course_count,
        'grand_total': grand_total,
    }

    return context
