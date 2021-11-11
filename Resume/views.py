from django.shortcuts import render
from Site_settings.models import SiteSettings
from Work_experience.models import WorkExperience


def home_page(request):
    site_settings = SiteSettings.objects.first()
    work_experience = WorkExperience.objects.all()

    context = {
        'site_settings': site_settings,
        'work_experience': work_experience,
    }

    return render(request,'Home_Page/Resume.html',context)