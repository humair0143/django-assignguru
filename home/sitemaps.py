from django.contrib.sitemaps import Sitemap
from home.models import Subject, Set, Question

class SubjectSitemap(Sitemap):

    def items(self):
        return Subject.objects.all()

class SetSitemap(Sitemap):

    def items(self):
        return Set.objects.all()

class QuestionSitemap(Sitemap):

    def items(self):
        return Question.objects.all()