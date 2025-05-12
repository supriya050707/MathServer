from django.shortcuts import render
from django.shortcuts import render

def lamp_power(request):
    context = {}
    context['p'] = "0"
    context['i'] = "0"
    context['r'] = "0"

    if request.method == 'POST':
        print("POST method is used")
        i = request.POST.get('intensity', '0')
        r = request.POST.get('resistance', '0')
        print("Intensity =", i)
        print("Resistance =", r)
        
        try:
            power = float(i) ** 2 * float(r)
        except ValueError:
            power = "Invalid input"

        context['p'] = power
        context['i'] = i
        context['r'] = r
        print("Power =", power)

    return render(request, 'mathapp/math.html', context)
