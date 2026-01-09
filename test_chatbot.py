#!/usr/bin/env python
"""Script de prueba simple para Google AI"""
import sys
from pathlib import Path
import os

# Cargar variables de entorno
from dotenv import load_dotenv
load_dotenv()

# Agregar raíz al path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

print("="*60)
print("PRUEBA DE CHATBOT TURÍSTICO - GOOGLE AI")
print("="*60 + "\n")

try:
    # Verificar API Key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("✗ ERROR: GOOGLE_API_KEY no está configurada en .env")
        print("\nPor favor, configura tu API key:")
        print("1. Copia .env.example a .env")
        print("2. Edita .env y añade tu Google API Key")
        sys.exit(1)
    
    print("✓ Google API Key encontrada")
    
    # Importar módulos
    print("\n✓ Importando módulos...")
    from src.llm.base import LLMFactory
    print("  ✓ LLMFactory")
    
    from src.agents.touristic_agent import AgentBuilder
    print("  ✓ AgentBuilder")
    
    from src.utils.config import ConfigLoader
    print("  ✓ ConfigLoader")
    
    # Crear instancia de LLM
    print("\n✓ Inicializando Google AI (Gemini)...")
    llm = LLMFactory.get_model(
        "google",
        model_name="gemini-pro",
        temperature=0.7,
        max_tokens=2048
    )
    print("  ✓ Modelo Gemini listo")
    
    # Crear agente
    print("\n✓ Creando agente turístico...")
    agent = AgentBuilder.create_agent(llm, agent_type="standard", max_iterations=5)
    print("  ✓ Agente creado")
    
    # Prueba simple
    print("\n" + "="*60)
    print("PRUEBA DE CONSULTA")
    print("="*60)
    
    query = "¿Cuáles son las 3 mejores atracciones en Huaraz para principiantes?"
    print(f"\nConsulta: {query}\n")
    
    response = agent.process_query(query)
    
    if response["success"]:
        print("RESPUESTA:")
        print("-" * 60)
        print(response["response"])
        print("-" * 60)
        print("\n✓ ¡Funcionando correctamente!")
    else:
        print(f"✗ Error: {response['error']}")
        print(f"Mensaje: {response['response']}")
    
except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
