from django.test import TestCase
from django.utils import timezone

# Create your tests here.
from .models import Course

class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title="Python Regular Expressions",
            description = "Learn to write regular expressions in Python"
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)