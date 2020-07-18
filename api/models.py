from django.db import models


class Role(models.Model):
    ROLE_CHOICES = (('admin', 'admin'), ('student', 'student'),
                    ('manager', 'manager'), ('lecture', 'lecture'))
    DEPARTMENT_CHOICES = (('SOFTWARE_DEVELOPMENT', 'SOFTWARE_DEVELOPMENT'),
                          ('COMPUTERSYSTEMSENGINEERING', 'COMPUTERSYSTEMSENGINEERING'),
                          ('INFORMATICS', 'INFORMATICS'), ('COMMUNICATION_NETWORKS', 'COMMUNICATION_NETWORKS'))
    FACULTY_CHOICES = (('INFORMATION_AND_COMMUNICATION_TECHNOLOGY', 'INFORMATION_AND_COMMUNICATION_TECHNOLOGY'),
                       ('ENGINEERING_AND_ENVIRONMENT', 'ENGINEERING_AND_ENVIRONMENT'))
    referenceNumber = models.CharField(max_length=10)
    role = models.CharField(choices=ROLE_CHOICES, max_length=50)
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=50)
    faculty = models.CharField( choices=FACULTY_CHOICES, max_length=50)

    def __str__(self):
        return '{},{},{},{}'.format(self.referenceNumber, self.role, self.department, self.faculty)
