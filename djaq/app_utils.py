from django.apps import apps
from django.db import models, connections


"""
https://docs.djangoproject.com/en/2.1/ref/models/relations/

In [12]: Book._meta.get_field('publisher').related_model
Out[12]: books.models.Publisher

In [13]: Book._meta.get_field('publisher').related_fields
Out[13]:
[(<django.db.models.fields.related.ForeignKey: publisher>,
  <django.db.models.fields.AutoField: id>)]

"""


def model_path(model):
    """Return the dot path of a model."""
    return f"{model.__module__}.{model._meta.object_name}"


def get_db_type(field, connection):
    """Return a string indicating what kind of database."""
    if isinstance(
        field, (models.PositiveSmallIntegerField, models.PositiveIntegerField)
    ):
        # integer CHECK ("points" >= 0)'
        return field.db_type(connection).split(" ", 1)[0]

    return field.db_type(connection)


def find_model_class(name):
    """Return model class for name, like 'Book'.

    if name has dots, then everything before the last segment
    is an app specifier

    """
    if "." in name:
        class_name = name.split(".")[-1]
        app_name = ".".join(name.split(".")[:-1])
    else:
        class_name = name
        app_name = None

    list_of_apps = list(apps.get_app_configs())
    for a in list_of_apps:
        if app_name and not app_name == a.name:
            continue
        for model_name, model_class in a.models.items():
            if class_name == model_class.__name__:
                return model_class

    raise Exception(f"Could not find model: {name}")


def fieldclass_from_model(field_name, model):
    """Return a field class named field_name."""
    return model._meta.get_field(field_name)


def model_field(model_name, field_name):
    """Return tuple of (model, field).

    like:
       model = 'User'
       field = 'name'

    """

    model_class = find_model_class(model_name)
    if not model_class:
        raise Exception(f"No model class with name: {model_name}")
    return model_class, model_class._meta.get_field(field_name)


def field_ref(ref):
    """Shortcut for field model.

    like 'User.name'

    """
    return model_field(*ref.split("."))


def get_field_details(f, connection):
    d = {}
    d["name"] = f.name
    d["unique"] = f.unique
    d["primary_key"] = f.primary_key
    d["max_length"] = f.max_length
    d["generic_type"] = str(f.description)
    d["db_type"] = str(f.db_type(connection=connection))
    d["default"] = str(f.default)
    d["related_model"] = str(f.related_model)
    d["help_text"] = f.help_text
    return d


def get_model_details(cls, connection):
    fields = {}
    data = {}
    for f in cls._meta.fields:
        fields[f.name] = get_field_details(f, connection)
    data["fields"] = fields
    data["verbose_name"] = cls._meta.verbose_name
    data["label"] = cls._meta.label
    data["pk"] = str(cls._meta.pk)
    data["object_name"] = cls._meta.object_name
    return data


def get_model_classes(whitelist=None):
    """Return all model classes.

    whitelist is a dictionary with appnames and lists of models
    that we are allowed to return.

    """
    list_of_apps = list(apps.get_app_configs())
    models = {}
    for a in list_of_apps:
        if whitelist and a.name not in whitelist:
            continue
        for model_name, model_class in a.models.items():
            models[f"{a.name}.{model_class.__name__}"] = model_class
    return models


def get_schema(connection=None, whitelist=None):
    """Return json that represents all whitelisted app models."""
    connection = connection if connection else connections["default"]
    classes = get_model_classes(whitelist)
    model_data = {}
    for label, cls in classes.items():
        model_data[cls._meta.label] = get_model_details(cls, connection)
    return model_data
