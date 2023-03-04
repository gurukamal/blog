from __future__ import unicode_literals

OPEN = "OPEN"
INPROGRESS = "INPROGRESS"
CLOSED = "CLOSED"
STATUS_CHOICES = (
    (OPEN, 'Open'),
    (INPROGRESS, 'Inprogress'),
    (CLOSED, 'Closed'),
)

HIGH = "HIGH"
MEDIUM = "MEDIUM"
LOW = "LOW"
PRIORITY_CHOICES = (
    (HIGH, 'High'),
    (MEDIUM, 'Medium'),
    (LOW, 'Low'),
)