from jet_bridge import fields
from jet_bridge.serializers.serializer import Serializer


class ModelDescriptionFieldSerializer(Serializer):
    name = fields.CharField()
    field = fields.CharField()
    db_column = fields.CharField()
    filterable = fields.BooleanField()
    editable = fields.BooleanField()
    params = fields.JSONField()

    class Meta:
        fields = (
            'name',
            'db_column',
            'field',
            'filterable',
            'editable',
            'params',
        )


class ModelDescriptionSerializer(Serializer):
    model = fields.CharField()
    db_table = fields.CharField()
    hidden = fields.BooleanField()
    fields = ModelDescriptionFieldSerializer(many=True)

    class Meta:
        fields = (
            'model',
            'db_table',
            'hidden',
            'fields',
        )
