from django.template.defaulttags import url
from django.urls import path
from rest_framework.routers import DefaultRouter
from app.views.viewCategoria import CategoriaViewSet
from app.views.viewCatTempCor import CatTempCorViewSet
from app.views.viewCiePesq import CiePesqViewSet
from app.views.viewCompAtm import CompAtmViewSet
from app.views.viewComponente import ComponenteViewSet
from app.views.viewConstelacao import ConstelacaoViewSet
from app.views.viewCorpo import CorpoViewSet
from app.views.viewEstrPeriferica import EstrPerifericaViewSet
from app.views.viewEstrela import EstrelaViewSet
from app.views.viewGalax import GalaxiaViewSet
from app.views.viewPlaneta import PlanetaViewSet
from app.views.viewPlanetaTipo import PlanetaTipoViewSet
from app.views.viewSatNatural import SatNaturalViewSet
from app.views.viewSistema import SistemaViewSet
from app.views.viewTipoGalax import TipoGalaxViewSet

router = DefaultRouter()
router.register(r"categoria", CategoriaViewSet)
router.register(r"ciepesq", CiePesqViewSet)
router.register(r"cattempcor", CatTempCorViewSet)
router.register(r"compatm", CompAtmViewSet)
router.register(r"componente", ComponenteViewSet)
router.register(r"constelacao", ConstelacaoViewSet)
router.register(r"corpo", CorpoViewSet)
router.register(r"estrela", EstrelaViewSet)
router.register(r"estrperiferica", EstrPerifericaViewSet)
router.register(r"galaxia", GalaxiaViewSet)
router.register(r"planeta", PlanetaViewSet)
router.register(r"planetatipo", PlanetaTipoViewSet)
router.register(r"satnatural", SatNaturalViewSet)
router.register(r"sistema", SistemaViewSet)
router.register(r"tiposgalax", TipoGalaxViewSet)

urlpatterns = router.urls



