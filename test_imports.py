#!/usr/bin/env python
"""Script de prueba simple"""
import sys
from pathlib import Path

# Agregar raíz al path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

print("✓ Importando módulos...")

try:
    from src.llm.base import LLMFactory
    print("✓ LLMFactory importado correctamente")
    
    from src.agents.touristic_agent import TouristicAgent, AgentBuilder
    print("✓ Agente importado correctamente")
    
    from src.utils.helpers import Logger
    print("✓ Helpers importados correctamente")
    
    from src.utils.config import ConfigLoader
    print("✓ ConfigLoader importado correctamente")
    
    print("\n✓ ¡Todos los módulos cargados correctamente!")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
