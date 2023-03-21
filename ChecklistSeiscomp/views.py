from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
 
# relative import of forms
from .models import ChecklistSeiscompModel, OperatorModel
from .forms import InputForm, OperatorForm
 
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    input_form = InputForm(request.POST or None)
    if input_form.is_valid():
        input_form.save()
        input_form = InputForm()
         
    context['input_form']= input_form
    return render(request, "create_view.html", context)

def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = ChecklistSeiscompModel.objects.all()
         
    return render(request, "list_view.html", context)

# pass id attribute from urls
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = ChecklistSeiscompModel.objects.get(id = id)
         
    return render(request, "detail_view.html", context)

# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(ChecklistSeiscompModel, id = id)
 
    # pass the object as instance in form
    form = OperatorForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)

# delete view for details
def operator_delete(request, id):
    ob = OperatorModel.objects.get(id=id)
    ob.delete()
    return HttpResponseRedirect("/operator_view")

def data_delete(request, id):
    ob = ChecklistSeiscompModel.objects.get(id=id)
    ob.delete()
    return HttpResponseRedirect("/list_view")

def operator_update(request, id):
    ob = OperatorModel.objects.get(id=id)
    ob.name = request.POST.get('field1')
    ob.save()
    return HttpResponseRedirect("/operator_view")

def operator_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["operators"] = OperatorModel.objects.all()
    
    add_operator_form = OperatorForm(request.POST or None)
    if add_operator_form.is_valid():
        add_operator_form.save()
        
        # Resetting the form after it has been submitted.
        add_operator_form = OperatorForm() 
         
    context['add_operator_form']= add_operator_form

    return render(request, "operator_view.html", context)

def edit_operator_name(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(OperatorModel, id = id)
 
    # pass the object as instance in form
    form = OperatorForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "operator_view.html", context)