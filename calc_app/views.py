from django.shortcuts import render


def calc_view(request):
    var1 = 0 if request.POST.get('var1') == None else float(request.POST.get('var1'))
    var2 = 0 if request.POST.get('var2') == None else float(request.POST.get('var2'))
    operator = request.POST.get('operators', None)
    result = 0
    operation = ''

    if operator == 'add':
        operation = '+'
        result = var1 + var2
    elif operator == 'sub':
        operation = '-'
        result = var1 - var2
    elif operator == 'mul':
        operation = '*'
        result = var1 * var2
    elif operator == 'div':
        operation = '/'
        result = var1 / var2

    return render(request, 'base.html', {'result': result,
                                         'var1': var1,
                                         'var2': var2,
                                         'operation': operation})
