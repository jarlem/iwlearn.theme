  # -*- extra stuff goes here -*- 

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

from Products.feedfeeder.content.item import FeedFeederItem
from Products.feedfeeder.content.item import FeedFeederItem_schema

FeedFeederItem_schema['relatedItems'].widget.visible = {'edit': 'visible', 'view': 'visible'}
FeedFeederItem.schema = FeedFeederItem_schema
