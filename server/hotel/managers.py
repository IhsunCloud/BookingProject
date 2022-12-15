from django.db.models import Manager


class ReviewManager(Manager):
	def active(self):
		return self.filter(active=True)