# -*- coding: utf-8 -*-

from zope.component import getMultiAdapter
from plone.app.search.browser import Search

class Search(Search):

    # Override: remove elipsis
    def breadcrumbs(self, item):
        obj = item.getObject()
        view = getMultiAdapter((obj, self.request), name='breadcrumbs_view')
        # cut off the item itself
        breadcrumbs = list(view.breadcrumbs())[:-1]
        if len(breadcrumbs) == 0:
            # don't show breadcrumbs if we only have a single element
            return None
        # if len(breadcrumbs) > 3:
        #     # if we have too long breadcrumbs, emit the middle elements
        #     empty = {'absolute_url': '', 'Title': unicode('…', 'utf-8')}
        #     breadcrumbs = [breadcrumbs[0], empty] + breadcrumbs[-2:]
        return breadcrumbs

