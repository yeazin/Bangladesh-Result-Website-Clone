
from django.http import HttpResponse
from django.shortcuts import redirect, render

from result.models.result import ResultProfile

# Create your views here.
from django.views import View


# Getting the Result profile

class GetResultView(View):
    def get(self,request):
        getRoll = request.GET['roll']

        match = ResultProfile.objects.filter(rollNumber= getRoll).first()
        context = {}
        if match:
            context = {
                'match':match
            }
        # else :
        #     noMath = match.none()

        return render(request,'index.html',context)

    #def post(self,request):
        # getRoll = request.POST.get('roll')

        # match = ResultProfile.objects.filter(rollNumber= getRoll).first()
        
        # if match:
        #     print(match.id)
        #     return redirect ('result')
        #     return HttpResponse('<h2>You Find the Current One</h2>')
        # else:
        #     return HttpResponse('<h2>Query didnt Match</h2>')
