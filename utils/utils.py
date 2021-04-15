from rest_framework.exceptions import ParseError, ValidationError

class ModelValidationMixin:
    """
    This Mixin is used to call clean method of model in serializer.
    """
    def validate(self, attrs):
        instance = self.Meta.model(**attrs)
        instance.clean()
        return attrs

class IdInValidationMixin(ModelValidationMixin):
    """
    This is extension of ModelValidationMixin. id can be read in clean method.
    This Mixin contain Meta class. Manually inherit Meta class in Inheriting Class.

    example:

        class SomeClass(IdInValidationMixin):
            class Meta(IdInValidationMixin.Meta):
                ...
    """
    class Meta:
        extra_kwargs = {'id': {'read_only': False,}}

    def validate(self, attrs):
        if self.context['request'].method == 'POST': # to delete id when post is there(used for fees model)
            if attrs.get('id', None):
                attrs.pop('id')
        return ModelValidationMixin.validate(self, attrs)

def validate_date_range(from_date, to_date):
    """
    raises validation error if from_date is greater than to_date.
    """
    if from_date > to_date:
        # raise ValidationError(detail="from_date must be less than to_date") 
        raise ParseError(detail="from_date must be less than to_date") 