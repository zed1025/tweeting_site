
from django.shortcuts import render
from django.shortcuts import redirect

from user.forms import AccountUpdateForm
from feed.models import Tweet


def account_update_view(request):
    if not request.user.is_authenticated:
        return redirect('account_login')

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(
            initial={
                'email': request.user.email,
                'username': request.user.username,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
            }
        )

    context['account_form'] = form

    return render(request, 'modify_account.html', context)

