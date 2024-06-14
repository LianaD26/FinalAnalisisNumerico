from ..gui.taylor_w import ITaylor
from ..gui.ceros_w import ceros_window
from ..gui.sist_ec_lineales_w import IEcLineales
from ..gui.interpolacion_ajuste_w import interp_ajuste_window
from ..gui.ec_diferenciales_w import ecdif_window


def main_controller(opcion: str):
    print(f"Botón presionado: {opcion}")
    if opcion == "Serie de Taylor":
        w_taylor = ITaylor()
    elif opcion == "Ceros de funciones":
        ceros_window()
    elif opcion == "Sistema Ec.Lineales":
        ec_lin = IEcLineales()
    elif opcion == "Interpolacion y ajuste":
        interp_ajuste_window()
    elif opcion == "Sistema Ec.Diferenciales":
        ecdif_window()

