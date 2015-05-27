from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone


from .forms import UserForm, ReportForm

from .models import Report

#class IndexView(generic.ListView):
#    template_name = 'daily_report/index.html'
#    context_object_name = 'latest_daily_report'
    
def get_queryset(request):
    repo = Report.objects.order_by('-edit_date')[:5]
    context = {'repo': repo}
    return render(request, 'daily_report/index.html',context)


def register(request):
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() :
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        else:
            print(user_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        
    # Render the template depending on the context.
    return render(request,
            'daily_report/register.html',
            {'user_form': user_form, 'registered': registered} )



def user_login(request):

    login_flag = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/daily_report/')
            else:
                print("Your account is disabled.")
        else:
            user_form = UserForm(data=request.POST)
            if user_form.is_valid():
                login_flag = True
                print("入力が正しくありません")
            else:
                print(user_form.errors)
    else:
        user_form = UserForm()
    
    return render(request,
       'daily_report/login.html',
           {'user_form': user_form, 'login_flag': login_flag} )

def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/daily_report/')

def write_report(request):

    report_flag = False


    if request.method == 'POST':
        report_form = ReportForm(data=request.POST)
        
        if report_form.is_valid():
            report = report_form.save(commit=False)
            report.edit_date = timezone.now()
            report.user_id = request.user
            report.save()
            report_flag = True
        else:
            print(report_form.errors)
    else:
        report_form = ReportForm()

    return render(request, 'daily_report/write.html', {'report_form': report_form, 'report_flag': report_flag})

# Create your views here.
