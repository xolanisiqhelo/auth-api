from django.db import models


class Role(models.Model):
    ROLE_CHOICES = (('admin', 'admin'), ('student', 'student'),
                    ('manager', 'manager'), ('lecture', 'lecture'))
    student_no = models.CharField(max_length=10)
    role = models.CharField(choices=ROLE_CHOICES, max_length=10)


    def __str__(self):
        return '{},{}'.format(self.student_no, self.role)