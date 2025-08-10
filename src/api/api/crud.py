from asgiref.sync import sync_to_async
from django.shortcuts import get_object_or_404


class DatabaseCrud:
    """Default class for CRUD operations."""

    def __init__(self, model_class):
        self.model_class = model_class

    async def list(self, **kwargs):
        """Return all objects in the database."""
        queryset = await sync_to_async(list)(
            self.model_class.objects.all().filter(**kwargs)  # noqa
        )
        return queryset

    async def get(self, obj_id: int):
        """Return object by ID."""
        instance = await sync_to_async(get_object_or_404)(self.model_class, id=obj_id)
        return instance

    async def create(self, **payload):
        """Create a new object."""
        instance = await sync_to_async(self.model_class.objects.create)(**payload)
        return instance

    async def check_if_exists(self, **payload):
        return await sync_to_async(self.model_class.objects.filter(**payload).exists)()
