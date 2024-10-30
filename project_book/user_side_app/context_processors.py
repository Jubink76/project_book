from adminside_app.models import CategoryTable
# Create your views here.
def list_category(request):
    categories = CategoryTable.objects.filter(is_available=True, is_deleted=False)
    return {'categories':categories}