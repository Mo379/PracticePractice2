import pandas as pd
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.functional import cached_property
from view_breadcrumbs import BaseBreadcrumbMixin
from braces.views import (
        LoginRequiredMixin,
        GroupRequiredMixin,
        SuperuserRequiredMixin,
    )
from content.models import Point, Video, Specification


# Superuser views
class SuperuserMonitorView(
            LoginRequiredMixin,
            SuperuserRequiredMixin,
            BaseBreadcrumbMixin,
            generic.ListView
        ):
    login_url = 'user:login'
    redirect_field_name = False
    template_name = "dashboard/superuser/monitor.html"
    context_object_name = 'context'

    @cached_property
    def crumbs(self):
        return [
                ("dashboard", reverse("dashboard:index")),
                ("traffic", reverse("dashboard:admin_traffic"))
                ]

    def get_queryset(self):
        context = {}
        context['sidebar_active'] = 'superuser/monitor'
        return context


class SuperuserContentManagementView(
            LoginRequiredMixin,
            SuperuserRequiredMixin,
            BaseBreadcrumbMixin,
            generic.ListView
        ):
    login_url = 'user:login'
    redirect_field_name = False
    template_name = "dashboard/superuser/contentmanagement.html"
    context_object_name = 'context'

    @cached_property
    def crumbs(self):
        return [
                ("dashboard", reverse("dashboard:index")),
                ("traffic", reverse("dashboard:admin_traffic"))
                ]

    def get_queryset(self):
        context = {}
        context['sidebar_active'] = 'superuser/contentmanagement'
        context['bad_videos'] = Video.objects.filter(v_health=False)
        return context


class SuperuserSpecificationsView(
            LoginRequiredMixin,
            SuperuserRequiredMixin,
            BaseBreadcrumbMixin,
            generic.ListView
        ):
    login_url = 'user:login'
    redirect_field_name = False
    template_name = "dashboard/superuser/specifications.html"
    context_object_name = 'context'

    @cached_property
    def crumbs(self):
        return [
                ("dashboard", reverse("dashboard:index")),
                ("specifications", reverse("dashboard:superuser_specifications"))
                ]

    def get_queryset(self):
        context = {}
        context['sidebar_active'] = 'superuser/specifications'
        #
        Notes = Specification.objects.values(
                    'spec_level',
                    'spec_subject',
                    'spec_board',
                    'spec_name',
                    'id',
                ).distinct().order_by(
                    'spec_level',
                    'spec_subject',
                    'spec_board',
                    'spec_name',
                )
        Notes_objs = [obj for obj in Notes]
        df = pd.DataFrame(Notes_objs)
        dic = {}
        for le, s, m, c, idd in zip(
                list(df['spec_level']),
                list(df['spec_subject']),
                list(df['spec_board']),
                list(df['spec_name']),
                list(df['id']),
                ):
            if le not in dic:
                dic[le] = {}
            if s not in dic[le]:
                dic[le][s] = {}
            if m not in dic[le][s]:
                dic[le][s][m] = []
            dic[le][s][m].append(Specification.objects.get(pk=idd))
        context['specifications'] = dic
        return context


class SuperuserSpecDesignerView(
            LoginRequiredMixin,
            SuperuserRequiredMixin,
            BaseBreadcrumbMixin,
            generic.ListView
        ):
    login_url = 'user:login'
    redirect_field_name = False
    template_name = "dashboard/superuser/specdesigner.html"
    context_object_name = 'context'

    @cached_property
    def crumbs(self):
        return [
                ("dashboard", reverse("dashboard:index")),
                ("specifications", reverse("dashboard:superuser_specifications")),
                ("designer", '')
                ]

    def get_queryset(self):
        context = {}
        context['sidebar_active'] = 'superuser/specifications'
        #
        level = self.kwargs['level']
        subject = self.kwargs['subject']
        board = self.kwargs['board']
        name = self.kwargs['name']
        spec = Specification.objects.get(
                spec_level=level,
                spec_subject=subject,
                spec_board=board,
                spec_name=name
                )
        moduels = Point.objects.values(
                    'p_level',
                    'p_subject',
                    'p_moduel',
                ).distinct().order_by(
                    'p_level',
                    'p_subject',
                    'p_moduel',
                ).filter(p_level=level, p_subject=subject)
        moduels_objs= [obj for obj in moduels]
        context['spec'] = spec
        context['moduels'] = moduels_objs
        return context




# Create your views here.
class IndexView(
            LoginRequiredMixin,
            BaseBreadcrumbMixin,
            generic.ListView
        ):
    login_url = 'user:login'
    redirect_field_name = ''


    template_name = "dashboard/index.html"
    context_object_name = 'context'

    @cached_property
    def crumbs(self):
        return [
                ("dashboard", reverse("dashboard:index")),
                ("Home", reverse("dashboard:index"))
                ]

    def get_queryset(self):
        context = {}
        context['sidebar_active'] = 'dashboard/index'
        return context


# Admin views
class AdminTrafficView(
            LoginRequiredMixin,
            GroupRequiredMixin,
            BaseBreadcrumbMixin,
            generic.ListView
        ):
    login_url = 'user:login'
    redirect_field_name = False
    group_required = u"Admin"
    template_name = "dashboard/admin/traffic.html"
    context_object_name = 'context'

    @cached_property
    def crumbs(self):
        return [
                ("dashboard", reverse("dashboard:index")),
                ("traffic", reverse("dashboard:admin_traffic"))
                ]

    def get_queryset(self):
        context = {}
        context['sidebar_active'] = 'admin/traffic'
        return context


class StudentPerformanceView(
            LoginRequiredMixin,
            GroupRequiredMixin,
            BaseBreadcrumbMixin,
            generic.ListView
        ):
    login_url = 'user:login'
    redirect_field_name = False
    group_required = u"Student"
    template_name = "dashboard/student/performance.html"
    context_object_name = 'context'

    @cached_property
    def crumbs(self):
        return [
                ("dashboard", reverse("dashboard:index")),
                ("perfromance", reverse("dashboard:student_performance"))
                ]

    def get_queryset(self):
        context = {}
        context['sidebar_active'] = 'student/performance'
        return context


class TeacherClassesView(
            LoginRequiredMixin,
            GroupRequiredMixin,
            BaseBreadcrumbMixin,
            generic.ListView
        ):
    login_url = 'user:login'
    redirect_field_name = False
    group_required = u'Teacher'
    template_name = "dashboard/teacher/classes.html"
    context_object_name = 'context'

    @cached_property
    def crumbs(self):
        return [
                ("dashboard", reverse("dashboard:index")),
                ("classes", reverse("dashboard:teacher_classes"))
                ]

    def get_queryset(self):
        context = {}
        context['sidebar_active'] = 'teacher/classes'
        return context


class TutorClassesView(
            LoginRequiredMixin,
            GroupRequiredMixin,
            BaseBreadcrumbMixin,
            generic.ListView
        ):
    login_url = 'user:login'
    redirect_field_name = False
    group_required = u"PrivateTutor"
    template_name = "dashboard/tutor/classes.html"
    context_object_name = 'context'

    @cached_property
    def crumbs(self):
        return [
                ("dashboard", reverse("dashboard:index")),
                ("classes", reverse("dashboard:tutor_classes"))
                ]

    def get_queryset(self):
        context = {}
        context['sidebar_active'] = 'tutor/classes'
        return context


class SchoolManagementView(
            LoginRequiredMixin,
            GroupRequiredMixin,
            BaseBreadcrumbMixin,
            generic.ListView
        ):
    login_url = 'user:login'
    redirect_field_name = False
    group_required = u"School"
    template_name = "dashboard/school/management.html"
    context_object_name = 'context'

    @cached_property
    def crumbs(self):
        return [
                ("dashboard", reverse("dashboard:index")),
                ("management", reverse("dashboard:school_management"))
                ]

    def get_queryset(self):
        context = {}
        context['sidebar_active'] = 'school/management'
        return context


class CenterManagementView(
            LoginRequiredMixin,
            GroupRequiredMixin,
            BaseBreadcrumbMixin,
            generic.ListView
        ):
    login_url = 'user:login'
    redirect_field_name = False
    group_required = u"TuitionCenter"
    template_name = "dashboard/center/management.html"
    context_object_name = 'context'

    @cached_property
    def crumbs(self):
        return [
                ("dashboard", reverse("dashboard:index")),
                ("management", reverse("dashboard:center_management"))
                ]

    def get_queryset(self):
        context = {}
        context['sidebar_active'] = 'center/management'
        return context


class EditorTasksView(
            LoginRequiredMixin,
            GroupRequiredMixin,
            BaseBreadcrumbMixin,
            generic.ListView
        ):
    login_url = 'user:login'
    redirect_field_name = False
    group_required = u"Editor"
    template_name = "dashboard/editor/tasks.html"
    context_object_name = 'context'

    @cached_property
    def crumbs(self):
        return [
                ("dashboard", reverse("dashboard:index")),
                ("tasks", reverse("dashboard:editor_tasks"))
                ]

    def get_queryset(self):
        context = {}
        context['sidebar_active'] = 'editor/tasks'
        return context


class AffiliateStatisticsView(
            LoginRequiredMixin,
            GroupRequiredMixin,
            BaseBreadcrumbMixin,
            generic.ListView
        ):
    login_url = 'user:login'
    redirect_field_name = False
    group_required = u'Affiliate'
    template_name = "dashboard/affiliate/statistics.html"
    context_object_name = 'context'

    @cached_property
    def crumbs(self):
        return [
                ("dashboard", reverse("dashboard:index")),
                ("statistics", reverse("dashboard:affiliate_statistics"))
                ]

    def get_queryset(self):
        context = {}
        context['sidebar_active'] = 'affiliate/statistics'
        return context


class BlankView(LoginRequiredMixin, BaseBreadcrumbMixin, generic.ListView):
    login_url = 'user:login'
    redirect_field_name = None
    template_name = "dashboard/blank.html"
    context_object_name = 'context'

    @cached_property
    def crumbs(self):
        return [
                ("dashboard", reverse("dashboard:index")),
                ("blank", reverse("dashboard:blank"))
                ]

    def get_queryset(self):
        return "user_index"


class NotFoundView(LoginRequiredMixin, BaseBreadcrumbMixin, generic.ListView):
    login_url = 'user:login'
    redirect_field_name = None
    template_name = "dashboard/404.html"
    context_object_name = 'context'

    @cached_property
    def crumbs(self):
        return [
                ("dashboard", reverse("dashboard:index")),
                ("404", reverse("dashboard:404"))
                ]

    def get_queryset(self):
        return "user_index"
