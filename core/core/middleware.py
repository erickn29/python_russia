from django.utils.deprecation import MiddlewareMixin


class AddUserDataToFormMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == 'POST' and request.POST:
            user_id = request.user.id
            request.POST = request.POST.copy()
            request.POST['user_id'] = user_id

        return
