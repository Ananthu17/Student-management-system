from django.urls import path
from .views import CreateStudentAPI, StudentListAPI, MarkListAPI, \
                   StudentDetailsUpdateAPI, DeleteStudentAPI, CreateMarksAPI, \
                   MarkDetailsUpdateAPI, DeleteMarkListAPI


app_name = "portal_user"

urlpatterns = [
    # Student Urls
    path('add_students/', CreateStudentAPI.as_view(), name='add-students'),
    path('students_list/', StudentListAPI.as_view(), name='student-list'),
    path('update_student/<id>/', StudentDetailsUpdateAPI.as_view(),
         name="update-student"),
    path('delete_student/<id>/', DeleteStudentAPI.as_view(),
         name='delete-student'),
    # Mark Urls
    path('add_marks/', CreateMarksAPI.as_view(), name='add-marks'),
    path('marks_list/', MarkListAPI.as_view(), name='marks-list'),
    path('update_marks/<id>/', MarkDetailsUpdateAPI.as_view(),
         name='update-marks'),
    path('delete_marklist/<id>/', DeleteMarkListAPI.as_view(),
         name='delete-marks')
]
