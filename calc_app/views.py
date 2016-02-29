from django.shortcuts import render


def calc_view(request):
    try:
        var1 = 0 if not request.POST.get('var1') else float(request.POST.get('var1'))
        var2 = 0 if not request.POST.get('var2') else float(request.POST.get('var2'))
    except(ValueError, TypeError):
        return render(request, 'base.html', {
            'result': 'Invalid input. Please enter only digits 0 - 9'
        })

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
    next_val = result

    return render(request, 'base.html', {'result': result,
                                         'var1': var1,
                                         'var2': var2,
                                         'next_val': next_val,
                                         'operation': operation})
