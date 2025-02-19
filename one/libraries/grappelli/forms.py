from django.forms.widgets import HiddenInput


class GrappelliSortableHiddenMixin:
    """
    Mixin which hides the sortable field with Stacked and Tabular inlines.
    This mixin must precede admin.TabularInline or admin.StackedInline.
    """

    sortable_field_name = "position"

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == self.sortable_field_name:
            kwargs["widget"] = HiddenInput()
        return super().formfield_for_dbfield(db_field, request, **kwargs)  # noqa
