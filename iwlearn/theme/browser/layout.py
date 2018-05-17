""" Override the default Plone layout utility.

http://collective-docs.readthedocs.org/en/latest/templates_css_and_javascripts/css.html#adding-new-css-body-classes
"""

from zope.component import queryUtility
from zope.component import queryMultiAdapter, getMultiAdapter

from plone.i18n.normalizer.interfaces import IIDNormalizer
from plone.app.layout.globals import layout as base

class LayoutPolicy(base.LayoutPolicy):
    """
    Enhanched layout policy helper.

    Extend the Plone standard class to have some more <body> CSS classes
    based on the current context.
    """

    def bodyClass(self, template, view):
        """Returns the CSS class to be used on the body tag.
        """

        # Get contet parent
        body_class = base.LayoutPolicy.bodyClass(self, template, view)

        # Include context and parent ids as CSS classes on <body>
        normalizer = queryUtility(IIDNormalizer)

        body_class += " context-" + normalizer.normalize(self.context.getId())

        parent = self.context.aq_parent

        # Check that we have a valid parent
        if hasattr(parent, "getId"):
            body_class += " parent-" + normalizer.normalize(parent.getId())

        # Get path with "Default content item" wrapping applied
        context_helper = getMultiAdapter((self.context, self.request), name="plone_context_state")
        canonical = context_helper.canonical_object()

        path = canonical.absolute_url_path()

        # Mark site front page with special CSS class
        body_class += " front-page" if path == "/" else ""

        return body_class