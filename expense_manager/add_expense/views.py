from django.shortcuts import render


from .models import AddExpense



def home(request):

    if request.method == 'POST':
        user_exp = AddExpense(data=request.POST)
        user = user_exp.save()

    return render(request, 'based/expense.html', context={'user_exp':user_exp})
