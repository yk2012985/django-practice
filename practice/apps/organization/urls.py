from django.conf.urls import url, include
from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, \
    AddFavView, TeachersListView, TeacherDetailView


urlpatterns = [
    url(r'^list$', OrgView.as_view(), name="org_list"),
    url(r'^add_ask$', AddUserAskView.as_view(), name="add_ask"),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="org_home"),
    url(r'^org_course/(?P<org_id>\d+)$', OrgCourseView.as_view(), name="org_course"),
    url(r'^desc/(?P<org_id>\d+)$', OrgDescView.as_view(), name="org_desc"),
    url(r'^teacher/(?P<org_id>\d+)$', OrgTeacherView.as_view(), name="org_teacher"),



    # 机构收藏
    url(r'^add_fav/$', AddFavView.as_view(), name="org_add_fav"),

    # 讲师列表
    url(r'^teachers/list$', TeachersListView.as_view(), name="teachers_list"),
    url(r'^teachers/detail/(?P<teacher_id>\d+)$', TeacherDetailView.as_view(), name="teachers_detail"),

]




























