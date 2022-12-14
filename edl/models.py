from django.db import models


EDL_TYPE_CHOICES = [
    ('url', 'URL'),
    ('domain', 'Domain'),
    ('ip_address', 'IP Address')
]


class Edl(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    edl_type = models.CharField(max_length=20, choices=EDL_TYPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'.lower()


class EdlEntry(models.Model):
    edl = models.ForeignKey(Edl, on_delete=models.CASCADE, related_name='entries')
    entry_value = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    valid_until = models.DateTimeField(default=None)

    def __str__(self):
        return f'{self.edl.name} {self.entry_value}'.lower()