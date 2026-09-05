"""Utilidades para el frontend"""
import os

def get_icon_path(icon_name):
    """
    Obtiene la ruta correcta de un icono.
    
    Args:
        icon_name: Nombre del icono (ej: 'pdf.png', 'download.png')
    
    Returns:
        str: Ruta absoluta del icono
    """
    # Obtener el directorio de assets (app/frontend/assets)
    frontend_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(frontend_dir, "assets", "icons")
    icon_path = os.path.join(assets_dir, icon_name)
    return icon_path
