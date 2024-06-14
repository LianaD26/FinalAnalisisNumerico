from ..gui.taylor_w import ITaylor
from ..gui.ceros_w import ICeros
from ..gui.sist_ec_lineales_w import IEcLineales
from ..gui.interpolacion_ajuste_w import IAjuste
from ..gui.ec_diferenciales_w import IEcDiferenciales


def main_controller(opcion: str):
    print(f"Botón presionado: {opcion}")
    if opcion == "Serie de Taylor":
        w_taylor = ITaylor()
    elif opcion == "Ceros de funciones":
        w_ceros = ICeros()
    elif opcion == "Sistema Ec.Lineales":
        w_ec_lin = IEcLineales()
    elif opcion == "Interpolacion y ajuste":
        w_ajuste = IAjuste()
    elif opcion == "Sistema Ec.Diferenciales":
        w_ec_dif = IEcDiferenciales()

