from django.db import models
# Create your models here.

class Question(models.Model):
    question_text = models.CharField("Contains question",max_length = 250)
    pub_date = models.DateTimeField("Publish Date")

    def __str__(self):
        return self.question_text
    

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField("Options to the question",max_length=100)
    votes = models.IntegerField("Vote count",default=0)

    def __str__(self):
        return self.choice_text+' - '+str(self.votes)

