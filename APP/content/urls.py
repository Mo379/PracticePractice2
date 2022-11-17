from django.urls import path
from content import views


# App name
app_name = 'content'
urlpatterns = [
    path('content', views.ContentView.as_view(), name='content'),
    path('content/questions', views.QuestionsView.as_view(), name='questions'),
    path(
        'content/question/<level>/<subject>/<board>/<specification>/<module>/<chapter>/',
        views.QuestionView.as_view(),
        name='question'
        ),
    path('content/notes', views.NotesView.as_view(), name='notes'),
    path(
        'content/note-article/<level>/<subject>/<board>/<specification>/<module>/<chapter>/',
        views.NoteArticleView.as_view(),
        name='notearticle'
    ),
    path('content/papers', views.PapersView.as_view(), name='papers'),
    path('content/paper/<subject>/<board>/<board_moduel>/<exam_year>/<exam_month>/', views.PaperView.as_view(), name='paper'),
    #
    path(
        'content/_inheritfromspec',
        views._inheritfromspec,
        name='_inheritfromspec'
    ),
    path(
        'content/_ordermoduels',
        views._ordermoduels,
        name='_ordermoduels'
    ),
    path(
        'content/_orderchapters',
        views._orderchapters,
        name='_orderchapters'
    ),
    path(
        'content/_ordertopics',
        views._ordertopics,
        name='_ordertopics'
    ),
    path(
        'content/_orderpoints',
        views._orderpoints,
        name='_orderpoints'
    ),
    path(
        'content/_createspec/',
        views._createspec,
        name='_createspec'
    ),
    path(
        'content/_deletespec/',
        views._deletespec,
        name='_deletespec'
    ),
    path(
        'content/_renamespec/',
        views._renamespec,
        name='_renamespec'
    ),
    path(
        'content/_createmoduel/',
        views._createmoduel,
        name='_createmoduel'
    ),
    path(
        'content/_deletemoduel/',
        views._deletemoduel,
        name='_deletemoduel'
    ),
    path(
        'content/_renamemodule/',
        views._renamemodule,
        name='_renamemodule'
    ),
    path(
        'content/_createchapter/',
        views._createchapter,
        name='_createchapter'
    ),
    path(
        'content/_deletechpter/',
        views._deletechapter,
        name='_deletechapter'
    ),
    path(
        'content/_renamechapter/',
        views._renamechapter,
        name='_renamechapter'
    ),
    path(
        'content/_createtopic/',
        views._createtopic,
        name='_createtopic'
    ),
    path(
        'content/_deletetopic/',
        views._deletetopic,
        name='_deletetopic'
    ),
    path(
        'content/_renametopic/',
        views._renametopic,
        name='_renametopic'
    ),
    path(
        'content/_createpoint/',
        views._createpoint,
        name='_createpoint'
    ),
    path(
        'content/_deletepoint/',
        views._deletepoint,
        name='_deletepoint'
    ),
]
