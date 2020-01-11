from django.shortcuts import render
from feedbackapp.models import FeedbackData
from  feedbackapp.forms import FeedbackForm
from django.http.response import HttpResponse
import datetime as dt
date1=dt.datetime.now()
def feedbackview(request):
    if request.method=="POST":
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name1 = request.POST.get("name")
            rating1= request.POST.get("rating")
            feedback1 = request.POST.get("feedback")

            data=FeedbackData(
            name=name1,
            rating=rating1,
            Feedback=feedback1,
            date=date1
            )
            data.save()
            fform=FeedbackForm()
            feedbacks=FeedbackData.objects.all()
            return render(request,'feedback.html',{'fform':fform,'feedbacks':feedbacks})
        else:
            return HttpResponse("User missing some values")
    else:
        fform=FeedbackForm()
        feedbacks=FeedbackData.objects.all()
        return render(request,'feedback.html',{'fform':fform,'feedbacks':feedbacks})
