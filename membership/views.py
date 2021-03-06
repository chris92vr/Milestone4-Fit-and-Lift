from django.shortcuts import render, get_object_or_404
from membership.models import Membership, Subscription, UserMembership
from profiles.models import UserProfile
from django.contrib.auth.decorators import login_required
import datetime as dt


def membership(request):
    """ renders all membership"""
    # Delete expired subscriptions
    date = dt.date.today()
    subscriptions_expired = Subscription.objects.filter(
        expire_date_subscription__lt=date)
    for subscription in subscriptions_expired:
        usermembership = get_object_or_404(
            UserMembership, subscription_number=subscription.user_membership)
        usermembership.delete()
    membership = Membership.objects.all()
    # check if the logged in user is already subscribed
    try:
        profile = UserProfile.objects.get(user=request.user)
        usermembership = get_object_or_404(UserMembership,
                                           member_profile=profile)
        subscription = get_object_or_404(Subscription,
                                         user_membership=usermembership
                                         )
    except BaseException:
        profile = None
        usermembership = None
        subscription = None
    context = {
        'membership': membership,
        'subscription': subscription,
        'date': date,
    }
    return render(request, 'membership/membership.html', context)


@login_required
def edit_subscription(request, subscription_id):
    """ Extends subscription """
    extended_days = 0
    subscription = get_object_or_404(Subscription, pk=subscription_id)
    if request.method == 'GET':
        extended_days = request.GET.get('extended_subscription_days')
        request.session['extended'] = extended_days
    template = 'membership/edit_subscription.html'
    context = {
        'subscription': subscription,
    }
    return render(request, template, context)
