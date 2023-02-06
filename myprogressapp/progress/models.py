from django.db import models

# Create your models here.

from django.db import models

class Progress(models.Model):
    week = models.PositiveSmallIntegerField()
    number_of_tickets = models.PositiveIntegerField()
    average_resolution_time = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Week {self.week}: {self.number_of_tickets} tickets, average resolution time {self.average_resolution_time} minutes"
    
class Ticket(models.Model):
    progress = models.ForeignKey(Progress, on_delete=models.CASCADE)
    ticket_number = models.PositiveIntegerField()
    resolution_time = models.PositiveSmallIntegerField()
class Ticket(models.Model):
    typele = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


#     def __str__(self):
#         return f"Ticket {self.ticket_number} resolved in {self.resolution_time} minutes"
    
# class Comment(models.Model):
#     ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
#     comment = models.TextField()

#     def __str__(self):
#         return f"Comment on ticket {self.ticket.ticket_number}: {self.comment}"
    
# class User(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)

#     def __str__(self):
#         return f"User {self.username}"
    
# class UserProgress(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     progress = models.ForeignKey(Progress, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"User {self.user.username} has progress {self.progress}"       
     