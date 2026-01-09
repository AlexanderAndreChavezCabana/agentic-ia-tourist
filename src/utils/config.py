"""
Módulo para cargar y gestionar configuraciones
"""
import yaml
from typing import Dict, Any
from pathlib import Path


class ConfigLoader:
    """Cargador de configuraciones YAML"""
    
    def __init__(self, config_dir: str = "config"):
        self.config_dir = Path(config_dir)
    
    def load_config(self, filename: str) -> Dict[str, Any]:
        """Cargar configuración YAML"""
        config_path = self.config_dir / filename
        
        if not config_path.exists():
            raise FileNotFoundError(f"Archivo de configuración no encontrado: {config_path}")
        
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        return config
    
    def load_model_config(self) -> Dict[str, Any]:
        """Cargar configuración de modelos"""
        return self.load_config("model_config.yaml")
    
    def load_agent_config(self) -> Dict[str, Any]:
        """Cargar configuración del agente"""
        return self.load_config("agent_config.yaml")
