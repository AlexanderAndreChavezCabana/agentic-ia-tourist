# 🤖 Arquitectura Agentica - Chatbot Turístico Huaraz

## 📋 Tabla de Contenidos
1. [Introducción](#introducción)
2. [Arquitectura Agentica](#arquitectura-agentica)
3. [Patrón ReAct](#patrón-react)
4. [Herramientas Disponibles](#herramientas-disponibles)
5. [Flujo de Ejecución](#flujo-de-ejecución)
6. [Ejemplos de Uso](#ejemplos-de-uso)
7. [Configuración Avanzada](#configuración-avanzada)
8. [Troubleshooting](#troubleshooting)

---

## 🎯 Introducción

El **Chatbot Turístico de Huaraz** es un **Agente Agentico** impulsado por IA que utiliza Google Gemini 2.5 Flash para:
- Procesar consultas de turismo en lenguaje natural
- Tomar decisiones sobre qué herramientas usar
- Ejecutar herramientas especializadas
- Sintetizar respuestas complejas e informadas

### ¿Qué es un Agente Agentico?
Un agente agentico es un sistema de IA que:
1. **Entiende** la consulta del usuario
2. **Razona** sobre qué acciones tomar
3. **Ejecuta** herramientas especializadas
4. **Itera** basándose en resultados
5. **Responde** con información sintetizada

---

## 🏗️ Arquitectura Agentica

### Componentes Principales

```
┌─────────────────────────────────────────┐
│     Usuario (Consulta en Natural)       │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│   Google Gemini 2.5 Flash (LLM)         │
│  - Procesa la consulta                  │
│  - Decide qué herramientas usar         │
│  - Sintetiza respuestas                 │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│   Agente ReAct (LangGraph)              │
│  - Coordina razonamiento y acciones     │
│  - Gestiona ciclos de iteración         │
│  - Controla flujo de ejecución          │
└──────────────┬──────────────────────────┘
               │
        ┌──────┴────────┐
        │               │
        ▼               ▼
  ┌──────────────┐  ┌──────────────┐
  │ Herramientas │  │ Base de      │
  │ (7 Tools)    │  │ Conocimientos│
  │              │  │ (Huaraz)     │
  └──────────────┘  └──────────────┘
```

### Stack Tecnológico

| Componente | Tecnología |
|-----------|-----------|
| **LLM** | Google Gemini 2.5 Flash |
| **Framework** | LangChain 1.2.3+ |
| **Agente** | LangGraph 1.0.5+ (ReAct) |
| **Lenguaje** | Python 3.9+ |
| **Herramientas** | 7 funciones especializadas |

---

## ⚙️ Patrón ReAct

**ReAct** = **Reasoning + Acting** (Razonamiento + Acción)

### Ciclo ReAct

```
1. OBSERVACIÓN (Observation)
   └─> Agente recibe la consulta del usuario
   └─> Ej: "¿Qué actividades para personas con baja condición física?"

2. RAZONAMIENTO (Reasoning/Thought)
   └─> LLM analiza la consulta
   └─> Determina qué herramientas necesita
   └─> Genera plan de acción
   └─> Ej: "Necesito buscar actividades y filtrar por dificultad"

3. ACCIÓN (Action)
   └─> Agente ejecuta herramientas
   └─> Llama funciones especializadas
   └─> Ej: Ejecuta search_attractions(difficulty="bajo")

4. RESULTADO (Observation)
   └─> Recibe output de herramientas
   └─> Procesa datos
   └─> Ej: "Laguna Llanganuco (bajo), Laguna 69 (medio)..."

5. SÍNTESIS (Final Response)
   └─> LLM crea respuesta final
   └─> Integra contexto y resultados
   └─> Responde al usuario
```

### Ejemplo Real

```
Usuario: "¿Qué debo hacer para evitar el mal de altura?"

OBSERVATION:
  Input: "¿Qué debo hacer para evitar el mal de altura?"

THOUGHT:
  "El usuario pregunta sobre mal de altura. Debo usar la herramienta 
   get_altitude_advice para proporcionar consejos especializados."

ACTION:
  Tool: get_altitude_advice()
  Input: No requiere parámetros

OBSERVATION (Resultado):
  {
    "symptoms": ["dolor de cabeza", "mareos", "fatiga"],
    "prevention": ["Aclimatarse 1-2 días", "Hidratarse", ...],
    "treatment": ["Descansar a altitud menor", ...],
    "when_to_seek_help": [...]
  }

FINAL RESPONSE:
  "Para evitar el mal de altura en Huaraz (3,052m):
   
   Prevención:
   • Aclimatarse 1-2 días antes de actividades de altura
   • Hidratarse abundantemente
   • Evitar alcohol y cafeína
   • Ascender lentamente
   
   Si experimentas síntomas como dolor de cabeza, mareos o 
   dificultad para respirar, descansa a menor altitud..."
```

---

## 🛠️ Herramientas Disponibles

El agente tiene acceso a **7 herramientas especializadas**:

### 1. **search_attractions** 🏔️
Busca atracciones turísticas por nombre o dificultad

**Parámetros:**
- `query` (str): Término de búsqueda
- `difficulty` (str, opcional): "bajo", "medio", "alto"

**Ejemplo:**
```python
search_attractions("laguna", difficulty="medio")
```

**Respuesta:**
```json
[
  {
    "name": "Laguna 69",
    "description": "Laguna glaciar de agua turquesa",
    "altitude": 4500,
    "duration": "6 horas",
    "difficulty": "medio"
  }
]
```

---

### 2. **get_attraction_details** 📍
Obtiene información detallada de una atracción

**Parámetros:**
- `attraction_name` (str): Nombre de la atracción

**Ejemplo:**
```python
get_attraction_details("Laguna Parón")
```

**Respuesta:**
```json
{
  "name": "Laguna Parón",
  "description": "Lago glaciar a 4,185m",
  "location": "Cordillera Blanca",
  "altitude": "4,185m",
  "difficulty": "bajo",
  "duration": "8-10 horas",
  "best_season": ["mayo", "junio", "julio", "agosto"],
  "essentials": ["Bloqueador solar", "Agua", "Poncho"],
  "cost": "$15-20"
}
```

---

### 3. **get_activity_recommendations** 🧗
Recomienda actividades según tipo y dificultad

**Parámetros:**
- `activity_type` (str): "trekking", "climbing", "cultural_tours", etc.
- `difficulty` (str, opcional): Nivel deseado

**Ejemplo:**
```python
get_activity_recommendations("trekking", difficulty="alto")
```

**Respuesta:**
```json
{
  "name": "Trekking Avanzado",
  "description": "Rutas de montaña desafiantes",
  "difficulty": "alto",
  "duration": "5-7 días",
  "cost_per_day": "$30-50"
}
```

---

### 4. **search_accommodations** 🏨
Busca alojamientos por presupuesto

**Parámetros:**
- `budget` (str): "budget", "mid_range", "luxury"
- `location` (str, opcional): Por defecto "Huaraz"

**Ejemplo:**
```python
search_accommodations("mid_range", location="Huaraz")
```

**Respuesta:**
```json
[
  {
    "name": "Hotel Tres Cruces",
    "price_per_night": "$40-60",
    "amenities": ["WiFi", "Desayuno", "Agua caliente"],
    "rating": "4.2 estrellas"
  }
]
```

---

### 5. **get_best_season** 🌤️
Recomienda mejor época para viajar según estilo

**Parámetros:**
- `travel_style` (str): "trekking", "casual", "photography", "cultural"

**Ejemplo:**
```python
get_best_season("photography")
```

**Respuesta:**
```json
{
  "best_months": ["mayo", "junio", "julio", "agosto"],
  "reason": "Máxima claridad atmosférica y cielo azul",
  "considerations": "Temperaturas bajas, llevar protección"
}
```

---

### 6. **get_altitude_advice** ⛰️
Proporciona consejos para evitar mal de altura

**Parámetros:**
Ninguno (función sin parámetros)

**Ejemplo:**
```python
get_altitude_advice()
```

**Respuesta:**
```json
{
  "symptoms": ["dolor de cabeza", "mareos", "fatiga"],
  "prevention": [
    "Aclimatarse 1-2 días",
    "Hidratarse abundantemente",
    "Evitar alcohol",
    "Ascender lentamente"
  ],
  "treatment": [
    "Descansar a altitud menor",
    "Beber agua y té de coca",
    "Considerar oxígeno suplementario"
  ]
}
```

---

### 7. **create_daily_itinerary** 📅
Crea itinerarios diarios personalizados

**Parámetros:**
- `attractions` (List[str]): Lista de atracciones
- `duration_hours` (int): Horas disponibles

**Ejemplo:**
```python
create_daily_itinerary(
  attractions=["Laguna Parón", "Laguna Llanganuco"],
  duration_hours=10
)
```

**Respuesta:**
```json
{
  "day_schedule": [
    {
      "time": "6:00",
      "activity": "Visita a Laguna Parón",
      "duration": "8-10 horas",
      "essentials": ["Agua", "Bloqueador solar"]
    }
  ],
  "total_attractions": 2,
  "estimated_completion": "19:00",
  "tips": ["Llevar suficiente agua", "Usar protector solar"]
}
```

---

## 🔄 Flujo de Ejecución

### Flujo Paso a Paso

```
┌─────────────────────────────────────────┐
│ 1. Usuario hace consulta                │
│    "¿Laguna 69 es apta para mi familia?"│
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│ 2. Cargar variables de entorno          │
│    - API Key de Google                  │
│    - Configuraciones de modelo          │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│ 3. Inicializar LLM (Gemini 2.5 Flash)   │
│    - Conexión a Google AI               │
│    - Verificar disponibilidad           │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│ 4. Crear Agente ReAct                   │
│    - Vincular herramientas              │
│    - Configurar sistema de prompts      │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│ 5. Invocar agente                       │
│    - Input: consulta del usuario        │
│    - Output: respuesta agentica         │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│ 6. Ciclo ReAct (puede iterar)           │
│                                         │
│    a) Gemini analiza la consulta        │
│    b) Decide qué herramientas usar      │
│    c) Ejecuta herramientas              │
│    d) Procesa resultados                │
│    e) Si necesita más info → vuelve a b)│
│    f) Genera respuesta final            │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│ 7. Retornar respuesta al usuario        │
│    "Laguna 69 es apta para familias..."|
└─────────────────────────────────────────┘
```

---

## 💡 Ejemplos de Uso

### Ejemplo 1: Consulta Simple
```python
from main import ChatbotTouristico

# Crear chatbot
chatbot = ChatbotTouristico(llm_provider="google")

# Consulta simple
response = chatbot.process_query(
    "¿Cuáles son las mejores atracciones para principiantes?"
)

print(response)
```

### Ejemplo 2: Con Preferencias de Usuario
```python
# Configurar preferencias
chatbot.user_preferences.update_preferences({
    "budget": "mid_range",
    "fitness_level": "bajo",
    "interests": ["naturaleza", "fotografía"]
})

# Consulta personalizada
response = chatbot.process_query(
    "Recomiendame actividades según mis preferencias"
)

print(response)
```

### Ejemplo 3: Itinerario Completo
```python
# Crear itinerario
response = chatbot.process_query("""
    Tengo 5 días en Huaraz. Presupuesto medio, 
    condición física media, intereso la naturaleza.
    Crea un itinerario detallado con:
    - Atracciones por día
    - Horarios
    - Costo estimado
    - Consejos de seguridad
""")

print(response)
```

### Ejemplo 4: Consulta Especializada
```python
# Problema específico
response = chatbot.process_query(
    "Tengo miedo al mal de altura. ¿Cómo puedo prepararme?"
)

# El agente usará automáticamente get_altitude_advice()
print(response)
```

---

## ⚙️ Configuración Avanzada

### Configurar Iteraciones Máximas
```python
from src.agents.touristic_agent import AgentBuilder

# Crear agente con más iteraciones (para consultas complejas)
agent = AgentBuilder.create_agent(
    llm,
    agent_type="standard",
    max_iterations=15  # Máximo 15 iteraciones
)
```

### Tipos de Agente Disponibles
```python
# Agente estándar
agent = AgentBuilder.create_agent(llm, agent_type="standard")

# Agente experto (más iteraciones)
agent = AgentBuilder.create_agent(llm, agent_type="expert")

# Agente presupuesto (enfocado en opciones económicas)
agent = AgentBuilder.create_agent(llm, agent_type="budget")
```

### Configurar Contexto del Usuario
```python
# Establecer contexto
agent.set_user_context({
    "budget": "mid_range",
    "fitness_level": "medio",
    "interests": ["trekking", "fotografía"],
    "duration_days": 5
})

# El agente considerará este contexto en todas las respuestas
```

### Historial de Conversación
```python
# Obtener historial
history = agent.get_conversation_history()
print(history)

# Limpiar historial
agent.clear_memory()
```

---

## 🔧 Configuración de Modelo

### archivo: `config/model_config.yaml`

```yaml
# Configuración de Modelos LLM
models:
  google:
    provider: "google"
    model_name: "gemini-2.5-flash"
    temperature: 0.7        # 0 = determinista, 1 = creativo
    max_tokens: 2048        # Límite de tokens de salida

# Modelo por defecto
default_model: "google"

# Timeout para llamadas a API
api_timeout: 30
```

### Ajustar Temperatura
```yaml
temperature: 0.3  # Más consistente, menos creativo
temperature: 0.7  # Balanced (recomendado)
temperature: 1.0  # Más creativo, menos consistente
```

---

## 📊 Monitoreo de Agente

### Ver iteraciones del agente
```python
# El agente registra automáticamente cada paso
response = agent.process_query(user_input)

# Ver historial de conversación
print("HISTORIAL DE CONVERSACIÓN:")
print(agent.get_conversation_history())

# Ver contexto del usuario
print("CONTEXTO DEL USUARIO:")
print(agent.user_context)
```

---

## ❌ Troubleshooting

### Error: "API key required"
**Problema:** Google API Key no está configurada

**Solución:**
```bash
# 1. Crear/editar .env
GOOGLE_API_KEY=tu_api_key_aqui

# 2. O establecer variable de entorno
export GOOGLE_API_KEY=tu_api_key_aqui
```

---

### Error: "create_react_agent() got unexpected keyword arguments"
**Problema:** Parámetros incorrectos en inicialización

**Solución:** Use solo parámetros válidos:
```python
# ❌ INCORRECTO
agent = create_react_agent(
    llm, tools, 
    system_prompt="...",  # No soportado
    state_modifier="..."  # No soportado
)

# ✅ CORRECTO
agent = create_react_agent(llm, tools)
```

---

### Error: "contents are required"
**Problema:** Formato incorrecto de entrada al agente

**Solución:** Usar HumanMessage correcto:
```python
# ❌ INCORRECTO
response = agent.invoke({"input": user_input, "messages": []})

# ✅ CORRECTO
from langchain_core.messages import HumanMessage
response = agent.invoke({"messages": [HumanMessage(content=user_input)]})
```

---

### Respuesta muy larga o incompleta
**Problema:** Token limit alcanzado

**Solución:** Reducir max_tokens o dividir consulta:
```yaml
# config/model_config.yaml
max_tokens: 1024  # Reducir de 2048
```

---

### Agente no usa una herramienta específica
**Problema:** El LLM no decide usar esa herramienta

**Solución:** Rephrasear consulta:
```python
# ❌ Poco específico
"¿Altura?"

# ✅ Específico
"Tengo miedo al mal de altura, ¿qué debo hacer para prepararme?"
```

---

## 📈 Mejores Prácticas

### 1. Consultas Claras y Específicas
```python
# ❌ Poco específico
"¿Laguna?"

# ✅ Específico
"¿Cuál es la mejor laguna para visitantes con baja condición física?"
```

### 2. Usar Contexto del Usuario
```python
# Siempre establecer contexto
agent.set_user_context({
    "budget": "mid_range",
    "fitness_level": "medio"
})

# Luego hacer consultas
response = agent.process_query(user_input)
```

### 3. Manejar Errores
```python
try:
    response = agent.process_query(user_input)
    print(response)
except Exception as e:
    print(f"Error: {e}")
    # Reintentar con consulta simplificada
```

### 4. Monitorear Iteraciones
```python
# Ver cuántas veces iteró el agente
history = agent.get_conversation_history()
print(f"Iteraciones totales: {len(history)}")
```

---

## 🎓 Conceptos Clave

### Herramientas vs Acciones
- **Herramientas:** Funciones que el agente puede ejecutar
- **Acciones:** Decisión del agente de usar una herramienta específica

### Observación en ReAct
- **Inicial:** La consulta del usuario
- **Intermedia:** Resultados de herramientas ejecutadas
- **Final:** Integración de toda la información

### Prompting del Agente
El agente usa un **system prompt** implícito que le enseña:
- Qué herramientas tiene disponibles
- Cómo usarlas
- Cuándo usarlas
- Cómo sintetizar respuestas

---

## 📚 Recursos Adicionales

- **LangChain Docs:** https://docs.langchain.com/
- **LangGraph Docs:** https://langchain-ai.github.io/langgraph/
- **Google Gemini API:** https://ai.google.dev/
- **ReAct Paper:** https://arxiv.org/abs/2210.03629

---

## 🎯 Resumen

El **Chatbot Turístico de Huaraz** es un agente agentico que:

✅ **Entiende** consultas complejas en español  
✅ **Razona** sobre qué acciones tomar  
✅ **Ejecuta** 7 herramientas especializadas  
✅ **Itera** para mejores resultados  
✅ **Responde** con información sintetizada y contextualizada  

**Alimentado por Google Gemini 2.5 Flash**

---

## 📞 Soporte

Para más ayuda:
1. Consulta [FINAL_STATUS.md](FINAL_STATUS.md)
2. Revisa [TECHNICAL.md](TECHNICAL.md)
3. Ejecuta los ejemplos en `examples/`

¡Disfruta del Chatbot Turístico! 🏔️
