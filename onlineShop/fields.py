class MoneyField(DecimalField):
    """
    A field for a monetary amount. Provide the default size and
    precision.
    """
    def __init__(self, *args, **kwargs):
        set_locale()
        defaults = {"null": True, "blank": True, "max_digits": 10,
                    "decimal_places": localeconv()["frac_digits"]}
        defaults.update(kwargs)
        super(MoneyField, self).__init__(*args, **defaults)
