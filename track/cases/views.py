from django.shortcuts import render
from django.http import HttpResponse
import re

def index(request):
    return render(request, "cases/index.html")

def track(request):

    global l

    n = request.POST['c1']

    lst = re.findall("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", n)

    l = set(lst)

    no_of_cases = len(l)

    my_context = {
        'result': l,
        'msg': 'Here are the cases in your bin:',
        'msg1': '# NOTE: Please note down the above cases in NOTEPAD so you can use them at the next time to have the track of such cases.',
        'msg2': no_of_cases
    }

    return render(request, 'cases/result.html', my_context)

def compare(request):
    return render(request, 'cases/compare.html')

def final(request):

    # l is the latest list and l1 is the previous list.

    n1 = request.POST['c2']
    lst = n1.split()

    l1 = set(lst)

    if l == l1:
        my_context1 = {
        'msg1': 'Congratulations! No leakage in your cases.'
        }

    elif l != l1:
        if len(l) < len(l1):
            my_context1 = {
                'result': set(l1).difference(l),
                'msg': 'Here are the leaked(Moved/ Closed/ Open) cases:-'
            }
            # result = ", ".join(n) We can also use it if we need he cases separated by comma and not the table.
        if len(l) > len(l1):
            if (all(x in l for x in l1)):
                my_context1 = {
                    'result': set(l).difference(l1),
                    'msg': 'Hurray!!! NO LEAKAGE but more cases are added in your bin which are:-'
                }

            else:
                my_context1 = {
                    'result': set(l1).difference(l),
                    'msg': 'Here are the cases which are leaked(Moved/ Closed/ Open):-'
                }

        if len(l) == len(l1):
            my_context1 = {
                'result': set(l1).difference(l),
                'msg': 'Here are the leaked(Moved/ Closed/ Open) cases:-'
            }

    else:
        my_context1 = {
            'msg1': 'Please enter the list of VALID Cases.'
        }

    return render(request, 'cases/final.html', my_context1)








