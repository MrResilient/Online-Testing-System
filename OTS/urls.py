from django.urls import path
from OTS.views import *
app_name='OTS'
urlpatterns = [
    path('',welcome ),
    path('new-candidate', candidateRegistrationform, name='registrationForm'),
    path('store-candidate', candidateRegistration, name='storeCandidate'),
    path('login', loginView, name='login'),
    path('home', candidateHome, name='home'),
    path('test-paper', testPaper, name='testPaper'),
    path('calculate-result', calculateTestResult, name='calculateTest'),
    path('test-history', TestResultHistory, name = 'testHistory'),
    path('result', showTestResult, name='result'),
    path('logout',logoutView, name='logout'),

]