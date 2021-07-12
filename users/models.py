from django.db import models
from django.contrib.auth.models import User

x = {{User.last_name}}
y=''
z=''
for i in range(4):
    y=y+x[i]
for i in range(6):
    if(i>3):
        z=z+x[i]


class Profile(models.Model):
    DEP_CHOICE =(
    ("01","Computer Science and Engineering"),
    ("02","Electronics and Communications Engineering"),
    ("03","Mechanical Engineering"),
    ("04","Chemical Engineering"),
    ("05","Design"),
    ("06","Biosciences and Bioengineering"),
    ("07","Civil Engineering"),
    ("08","Electronics and Electrical Engineering"),
    ("21","Engineering Physics"),
    ("22","Chemimal Science and Technology"),
    ("23","Mathematics and Computing"),
    ("","Humanities and Social Sciences"),
    )
    BAT_CHOICE = (
        ("2001", "B.Tech 20"),
        ("1901", "B.Tech 19"),
        ("1801", "B.Tech 18"),
        ("1701", "B.Tech 17"),
        ("1601", "B.Tech 16"),
        ("2002", "B.Des 20"),
        ("1902", "B.Des 19"),
        ("1802", "B.Des 18"),
        ("1702", "B.Des 17"),
        ("1602", "B.Des 16"),
        ("2041", "M.Tech 20"),
        ("1941", "M.Tech 19"),
        ("1841", "M.Tech 18"),
        ("1741", "M.Tech 17"),
        ("1641", "M.Tech 16"),
        ("2061", "PhD 20"),
        ("1961", "PhD 19"),
        ("1861", "PhD 18"),
        ("1761", "PhD 17"),
        ("1661", "PhD 16"),
    )
    SEM_CHOICE = (
    ("0", "select"),
    ("1st", "1st"),
    ("2nd", "2nd"),
    ("3rd", "3rd"),
    ("4th", "4th"),
    ("5th", "5th"),
    ("6th", "6th"),
    ("7th", "7th"),
    ("8th", "8th"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default=User.first_name)
    roll = models.CharField(max_length=9,default=User.last_name)
    batch = models.CharField(max_length=13,choices = BAT_CHOICE,default=y)
    semester = models.CharField(max_length=3,choices = SEM_CHOICE,default="0")
    department = models.CharField(max_length=50,choices = DEP_CHOICE,default=z)

    def __str__(self):
        return f'{self.user.first_name} profile'
    