# Documentación Técnica - Chatbot Turístico Huaraz

## Arquitectura General

```
┌─────────────────────────────────────────────────────┐
│                  USUARIO (CLI/API)                  │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│           main.py - ChatbotTouristico               │
│    Orquestación principal, interfaz interactiva    │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│      src/agents/touristic_agent.py                  │
│    - TouristicAgent (agente principal)             │
│    - AgentBuilder (constructor)                     │
│    - Gestión de memoria y contexto                  │
└────────────────────────┬────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
┌───────▼───────┐ ┌─────▼────────┐ ┌────▼──────────┐
│   LLM Models  │ │ Herramientas │ │ Prompt Eng.   │
├───────────────┤ ├──────────────┤ ├───────────────┤
│ src/llm/      │ │src/handlers/ │ │src/prompt_eng/│
│  - OpenAI     │ │  - search    │ │ - templates   │
│  - Anthropic  │ │  - get_info  │ │ - few-shot    │
│  - Groq       │ │  - recommend │ │ - routing     │
└───────┬───────┘ └──────┬───────┘ └───────┬───────┘
        │                │                  │
        └────────────────┼──────────────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
┌───────▼──────┐ ┌──────▼─────────┐ ┌───▼──────────┐
│ Knowledge DB │ │ Configuración  │ │ Utilities    │
├──────────────┤ ├────────────────┤ ├──────────────┤
│data/knowledge│ │config/         │ │src/utils/    │
│ - Atracciones│ │ - YAML files   │ │ - Logger     │
│ - Actividades│ │ - Settings     │ │ - Preferences│
│ - Alojamiento│ └────────────────┘ └──────────────┘
└──────────────┘
```

## Flujo de Procesamiento de una Consulta

```
┌─────────────────────────────────────────────────────┐
│  1. Usuario: "¿Cuál es la mejor atracción?"        │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│  2. Chatbot recibe la consulta                      │
│     → Valida entrada                                │
│     → Carga contexto de memoria                     │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│  3. Agente analiza la consulta                      │
│     → Determina herramientas necesarias            │
│     → Planifica iteraciones                         │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│  4. Agente ejecuta herramientas (iteraciones)      │
│     Iteración 1:                                    │
│       → search_attractions()                        │
│       → Procesa resultados                          │
│     Iteración 2:                                    │
│       → get_attraction_details()                    │
│       → Enriquece información                       │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│  5. LLM genera respuesta personalizada              │
│     → Usa prompt system personalizado               │
│     → Incorpora contexto del usuario                │
│     → Estructura respuesta clara                    │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│  6. Chatbot devuelve respuesta al usuario          │
│     → Guarda en memoria conversacional             │
│     → Formatea salida para legibilidad             │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│  Usuario recibe respuesta detallada                │
└─────────────────────────────────────────────────────┘
```

## Componentes Principales

### 1. **LLM Factory** (`src/llm/base.py`)

**Responsabilidad**: Crear y gestionar clientes LLM

```python
# Crear cliente
client = LLMFactory.create_client("openai", model_name="gpt-4", temperature=0.7)

# Obtener modelo directamente
model = LLMFactory.get_model("openai", temperature=0.7)
```

**Clientes soportados**:
- OpenAIClient
- AnthropicClient
- GroqClient

### 2. **Touristic Agent** (`src/agents/touristic_agent.py`)

**Responsabilidad**: Orquestar la lógica agéntica

**Características**:
- Crea un agente con capacidad de tomar decisiones
- Maneja herramientas automáticamente
- Mantiene historial conversacional
- Maneja errores y reintentos

**Métodos clave**:
```python
process_query(user_input) → Dict  # Procesa consulta del usuario
get_conversation_history() → str  # Historial de conversación
clear_memory() → None             # Limpia memoria
set_user_context(context) → None  # Configura contexto del usuario
```

### 3. **Herramientas** (`src/handlers/tools.py`)

**Herramientas disponibles**:

1. **search_attractions**
   - Busca atracciones por término o dificultad
   - Input: query (str), difficulty (str)
   - Output: Lista de atracciones

2. **get_attraction_details**
   - Obtiene información completa de una atracción
   - Input: attraction_name (str)
   - Output: Diccionario con detalles

3. **get_activity_recommendations**
   - Recomienda actividades
   - Input: activity_type (str), difficulty (str)
   - Output: Información de actividad

4. **search_accommodations**
   - Busca alojamientos por presupuesto
   - Input: budget (str), location (str)
   - Output: Lista de alojamientos

5. **get_best_season**
   - Recomienda mejor época para viajar
   - Input: travel_style (str)
   - Output: Información de temporada

6. **get_altitude_advice**
   - Proporciona consejos para mal de altura
   - Input: (ninguno)
   - Output: Síntomas, prevención, tratamiento

7. **create_daily_itinerary**
   - Crea itinerarios personalizados
   - Input: attractions (List), duration_hours (int)
   - Output: Schedule detallado

### 4. **Prompt Engineering** (`src/prompt_engineering/prompts.py`)

**Clases**:

- **PromptManager**: Gestiona prompts de sistema
  - `get_system_prompt()`: Prompt base del sistema
  - `get_tourism_question_prompt()`: Para preguntas turísticas
  - `get_routing_prompt()`: Para enrutamiento de consultas
  - `get_itinerary_prompt()`: Para crear itinerarios

- **PromptEngineer**: Optimiza prompts
  - `add_context_to_prompt()`: Añade contexto
  - `create_few_shot_prompt()`: Crea ejemplos

### 5. **Knowledge Base** (`data/knowledge/huaraz_knowledge.py`)

**Estructura de datos**:
```python
@dataclass
class Attraction:
    name: str                    # Nombre
    description: str             # Descripción
    location: str                # Ubicación
    altitude: int                # Altitud en metros
    difficulty: str              # bajo, medio, alto
    duration: str                # "4-5 horas"
    best_season: List[str]       # Meses recomendados
    essentials: List[str]        # Qué llevar
    estimated_cost: str          # Costo estimado
```

**Métodos de búsqueda**:
```python
get_attraction(key) → Attraction
search_by_difficulty(difficulty) → List[Attraction]
search_by_season(season) → List[Attraction]
get_accommodations_by_budget(budget) → List[Dict]
```

### 6. **Configuración** (`config/`)

**model_config.yaml**:
```yaml
models:
  openai:
    provider: "openai"
    model_name: "gpt-4-turbo"
    temperature: 0.7
    max_tokens: 2048
```

**agent_config.yaml**:
```yaml
agent:
  name: "Guía Turístico Huaraz IA"
  max_iterations: 10
  max_execution_time: 60
```

## Patrones de Diseño

### 1. **Factory Pattern**
```python
# LLMFactory crea clientes específicos
client = LLMFactory.create_client("openai")
```

### 2. **Builder Pattern**
```python
# AgentBuilder construye agentes personalizados
agent = AgentBuilder.create_agent(llm, agent_type="expert")
```

### 3. **Tool Pattern (LangChain)**
```python
# Herramientas decoradas con @tool
@tool
def search_attractions(query: str) -> List:
    ...
```

### 4. **Strategy Pattern**
```python
# Diferentes estrategias de prompt según contexto
prompt = PromptManager.get_routing_prompt()
prompt = PromptManager.get_itinerary_prompt()
```

## Configuración de Iteraciones del Agente

El agente usa "Agent Executor" de LangChain que:

1. **Observa**: Lee la entrada del usuario
2. **Piensa**: Decide qué herramientas usar
3. **Actúa**: Ejecuta las herramientas
4. **Observa**: Lee los resultados
5. **Repite** hasta alcanzar conclusión o límite de iteraciones

```python
# Configuración
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    max_iterations=10,              # Máximo 10 iteraciones
    handle_parsing_errors=True,     # Tolera errores de parseo
    verbose=True                    # Muestra el proceso
)
```

## Gestión de Memoria

```python
# ConversationBufferMemory mantiene historial
memory = ConversationBufferMemory(memory_key="chat_history")

# Guardar contexto
memory.save_context(
    {"input": user_input},
    {"output": agent_response}
)

# Acceder al buffer
print(memory.buffer)
```

## Manejo de Errores

```python
def process_query(user_input: str) -> Dict:
    try:
        response = self.agent_executor.invoke({...})
        return {"success": True, "response": response.get("output")}
    except Exception as e:
        return {"success": False, "error": str(e)}
```

## Extensibilidad

### Agregar una nueva herramienta:

```python
# En src/handlers/tools.py
@tool
def nueva_herramienta(parametro: str) -> Dict:
    """Descripción de la herramienta"""
    return {"resultado": valor}

# En src/agents/touristic_agent.py
def _setup_tools(self):
    return [
        search_attractions,
        ...,
        nueva_herramienta  # Agregar aquí
    ]
```

### Agregar una nueva atracción:

```python
# En data/knowledge/huaraz_knowledge.py
ATTRACTIONS = {
    ...,
    "nueva_atraccion": Attraction(
        name="Nombre",
        description="Descripción",
        # ... otros campos
    )
}
```

### Cambiar configuración:

```yaml
# En config/model_config.yaml
models:
  openai:
    temperature: 0.8  # Más creativo
    max_tokens: 4096  # Respuestas más largas
```

## Optimización de Rendimiento

### 1. Reducir iteraciones
```python
max_iterations=5  # Respuestas más rápidas
```

### 2. Usar modelo más rápido
```python
# Groq es más rápido que OpenAI
ChatbotTouristico(llm_provider="groq")
```

### 3. Limitar tamaño de respuesta
```yaml
max_tokens: 1024  # Reducir de 2048
```

### 4. Caché de prompts
```python
# LangChain cachea automáticamente
```

## Testing

```bash
# Ejecutar ejemplos
python examples/basic_usage.py
python examples/create_itinerary.py
python examples/specialized_queries.py

# Usar notebook
jupyter notebook notebooks/experimentation.ipynb
```

## Métricas Clave

- **Latency**: Tiempo de respuesta (ms)
- **Tool Usage**: Cuántas herramientas se usan por consulta
- **Iterations**: Número de iteraciones por consulta
- **Success Rate**: Porcentaje de respuestas exitosas

## Debugging

```python
# Habilitar modo debug
import os
os.environ["DEBUG"] = "true"

# Ver logs detallados
from src.utils.helpers import Logger
Logger.set_level("DEBUG")

# Ejecutar con verbose
agent_executor = AgentExecutor(..., verbose=True)
```

---

**Última actualización**: Enero 2025
