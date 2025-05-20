from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import AccountInfoForm
from .models import AccountInfo
from django.core.mail import send_mail
from .utils import generate_token, verify_token
from django.urls import reverse


def new_account(request):
    if request.method == 'GET':
        form = AccountInfoForm()
        return render(request, 'register.html', {'form': form})

    elif request.method == 'POST':
        form = AccountInfoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data  # gets cleaned form data

            if 'birthdate' in data:
                data['birthdate'] = data['birthdate'].isoformat()
            
            # generate token with all form data
            token = generate_token(data)
            activation_url = request.build_absolute_uri(reverse('activate_account')) + f'?token={token}'

            # send the email
            send_mail(
                'Confirm your registration',
                f'Hello {data["name"]}, click the link to activate your account: {activation_url}',
                'clientemail@gmail.com',
                [data["email"]],
                fail_silently=False,
            )

            return HttpResponse('Check your email to activate your account.')
        else:
            return HttpResponse(f'Errors: {form.errors}')


def activate_account(request):
    token = request.GET.get('token')
    data = verify_token(token)

    if data:
        if AccountInfo.objects.filter(email=data['email']).exists():
            return HttpResponse('This account has already been activated.')

        new_account = AccountInfo(**data)
        new_account.is_active = True
        new_account.save()

        return HttpResponse('Account successfully activated!')
    else:
        return HttpResponse('Invalid or expired token.')