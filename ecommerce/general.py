from .models import Category,Setting


def global_data(request):
    data = {
        'categoryData': Category.objects.all(),
        # get last setting data
        'settingData': Setting.objects.last(),


    }
    return data
