from unittest import result
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

class Sde:
    _sdeBase = automap_base()
    _SDEengine = create_engine("sqlite:///sqlite-latest.sqlite") # file from https://www.fuzzwork.co.uk/dump/sqlite-latest.sqlite.bz2
    _sdeBase.prepare(_SDEengine, reflect=True)

    _regions = _sdeBase.classes.mapRegions # browse db with http://sqlitebrowser.org/

    _sde_session = Session(_SDEengine)

    @classmethod
    def get_regions(cls) -> list[str]:
        result = cls._sde_session.query(cls._regions).all()
        return [row.regionName for row in result]
