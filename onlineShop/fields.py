# A field for a monetary amount. Provide the default size and precision.
from django.db.models import CharField, DecimalField 
from locale import localeconv
# from locale import setlocale, LC_MONETARY, Error as LocaleError

class MoneyField(DecimalField):

    def __init__(self, *args, **kwargs):
        # set_locale()
        defaults = {"null": True, "blank": True, "max_digits": localeconv()["frac_digits"],
                    "decimal_places": localeconv()["frac_digits"]
                    }
        defaults.update(kwargs)
        super(MoneyField, self).__init__(*args, **defaults)
