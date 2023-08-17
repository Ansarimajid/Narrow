from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect


class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user  # Who is the current user ?
        if user.is_authenticated:
            if user.user_type == '1':  # Is it the HOD/Admin
                if modulename == 'main_app.student_views':
                    return redirect(reverse('admin_home'))
            elif user.user_type == '2':  # Staff :-/ ?
                if modulename == 'main_app.student_views' or \
                      modulename == 'main_app.hod_views':
                    return redirect(reverse('staff_home'))
            elif user.user_type == '3':  # ... or Student ?
                if modulename == 'main_app.hod_views' or \
                      modulename == 'main_app.staff_views':
                    return redirect(reverse('student_home'))
            else:  # None of the aforementioned ?
                return redirect(reverse('login_page'))
        else:
            if request.path == reverse('login_page') or \
                modulename == 'django.contrib.auth.views' or \
                    request.path == reverse('user_login'):
                # If the path to do with authentication, pass
                pass
            else:
                return redirect(reverse('login_page'))


# from django.utils.deprecation import MiddlewareMixin
# from django.urls import reverse
# from django.shortcuts import redirect


# class FeePaymentMiddleware(MiddlewareMixin):
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         modulename = view_func.__module__
#         user = request.user

#         if user.is_authenticated and user.user_type == '3':
# # Assuming 'user_type' identifies a student
#             if modulename == 'main_app.views' and \
#                   not user.has_paid_fees() and user.payment_required:
#                 user.payment_required = False
# # Reset the payment_required flag
#                 user.save()
#                 return redirect(reverse('payment_required'))
# # Redirect to a payment page or an error page

#         return None
