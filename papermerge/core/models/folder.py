from django.utils.translation import ugettext_lazy as _
from papermerge.core import mixins
from papermerge.core.models.kvstore import KVCompNode, KVNode
from papermerge.core.models.node import BaseTreeNode
from papermerge.search import index


class Folder(mixins.ExtractIds, BaseTreeNode):

    search_fields = [
        index.SearchField('title'),
        index.SearchField('text', partial_match=True, boost=2),
        index.SearchField('notes')
    ]

    @property
    def kv(self):
        return KVNode(instance=self)

    @property
    def kvcomp(self):
        return KVCompNode(instance=self)

    class Meta:
        verbose_name = _("Folder")
        verbose_name_plural = _("Folders")

    def __str__(self):
        return self.title
