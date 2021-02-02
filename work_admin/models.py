from django.db import models


# # Create your models here.
# class create_course(View):
#     form_class = MyForm
#     initial = {'key': 'value'}
#     template_name = 'form_template.html'

#     def get(request):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})

#     def post(request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             # <process form cleaned data>
#             return HttpResponseRedirect('/success/')

#         return render(request, self.template_name, {'form': form})