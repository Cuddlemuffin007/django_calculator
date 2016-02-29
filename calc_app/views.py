from django.shortcuts import render


def calc_view(request):
    if request.method == 'POST':
        try:
            var1 = float(request.POST.get('var1'))
            var2 = float(request.POST.get('var2'))
        except(ValueError, TypeError):
            return render(request, 'base.html', {
                'result': 'Invalid input. Please enter only digits 0 - 9',
            })

        operator = request.POST.get('operators', None)

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
    else:
        return render(request, 'base.html', {})
