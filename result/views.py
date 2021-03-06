
from django.http import HttpResponse
from django.shortcuts import redirect, render

from result.models.result import ResultProfile
from result.models.initial import Year

# Create your views here.
from django.views import View


# Getting the Result profile

class GetResultView(View):
    def get(self,request):
        if request.is_ajax and request.method == "GET":

            #getRoll = request.GET['roll']
            getRoll = request.GET.get('roll')
            getRegi = request.GET.get('regi')
            className = request.GET.get('class')
            year = request.GET.get('year')

            context = {
                'year':Year.objects.all().order_by('-id'),
            }
            

            match = ResultProfile.objects.filter(rollNumber= getRoll).\
                                        filter(regiNumber=getRegi).\
                                        filter(className=className).\
                                        filter(year__year=year)\
                                        .first()
            
            if match:
                Match_context = {
                    'match':match,
                    
                }
                context.update(Match_context)
            # else :
            #     noMath = match.none()

        else:
            return HttpResponse('No not')
        return render(request,'home.html',context)

    #def post(self,request):
        # getRoll = request.POST.get('roll')

        # match = ResultProfile.objects.filter(rollNumber= getRoll).first()
        
        # if match:
        #     print(match.id)
        #     return redirect ('result')
        #     return HttpResponse('<h2>You Find the Current One</h2>')
        # else:
        #     return HttpResponse('<h2>Query didnt Match</h2>')



def Home(request):
    return render(request,'index.html')