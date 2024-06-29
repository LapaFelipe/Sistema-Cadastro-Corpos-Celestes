
from django.contrib import admin

from app.models.CatTempCorModel import CatTempCor
from app.models.CategoriaModel import Categoria
from app.models.CiePesqModel import CiePesq
from app.models.CompAtmosferaModel import CompAtmosfera
from app.models.ComponenteModel import Componente
from app.models.ConstelacaoModel import Constelacao
from app.models.CorpoModel import Corpo
from app.models.EstrelaModel import Estrela
from app.models.EstrelaPerifericaModel import EstrPeriferica
from app.models.GalaxiaModel import Galaxia
from app.models.PlanetaModel import Planeta
from app.models.PlanetaTipoModel import PlanetaTipo
from app.models.SatNaturalModel import SatNatural
from app.models.SistemaModel import Sistema
from app.models.TipoGalaxModel import TipoGalax
from django.contrib import admin

admin.site.register(Categoria)
admin.site.register(CatTempCor)
admin.site.register(CiePesq)
admin.site.register(CompAtmosfera)
admin.site.register(Componente)
admin.site.register(Constelacao)
admin.site.register(Corpo)
admin.site.register(Estrela)
admin.site.register(EstrPeriferica)
admin.site.register(Galaxia)
admin.site.register(Planeta)
admin.site.register(PlanetaTipo)
admin.site.register(SatNatural)
admin.site.register(Sistema)
admin.site.register(TipoGalax)