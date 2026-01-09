# 📖 ÍNDICE DE ARCHIVOS - CHATBOT TURÍSTICO HUARAZ

## 🎯 COMIENZA AQUÍ

### Para Empezar Rápido (5 minutos)
1. **[QUICKSTART.md](QUICKSTART.md)** ← LEE ESTO PRIMERO
   - Instalación rápida paso a paso
   - Obtener API keys
   - Primeros comandos

### Para Entender el Proyecto
2. **[README.md](README.md)** ← DOCUMENTACIÓN COMPLETA
   - Características
   - Uso programático
   - Ejemplos de consultas
   - Troubleshooting

3. **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** ← RESUMEN EJECUTIVO
   - Lo que se creó
   - Características implementadas
   - Métricas del proyecto

### Para Profundizar Técnicamente
4. **[TECHNICAL.md](TECHNICAL.md)** ← ARQUITECTURA DETALLADA
   - Diagramas de arquitectura
   - Flujo de procesamiento
   - Componentes principales
   - Patrones de diseño
   - Extensibilidad

---

## 📂 ESTRUCTURA DE CARPETAS

```
chatbot_turismo_huaraz/
│
├── 📄 ARCHIVOS DE DOCUMENTACIÓN
│   ├── README.md                 ← Documentación principal
│   ├── QUICKSTART.md             ← Guía de instalación rápida
│   ├── TECHNICAL.md              ← Arquitectura técnica
│   ├── PROJECT_SUMMARY.md        ← Resumen del proyecto
│   └── INDEX.md                  ← Este archivo
│
├── 🚀 ARCHIVOS EJECUTABLES
│   ├── main.py                   ← PROGRAMA PRINCIPAL
│   ├── setup.py                  ← Instalación del paquete
│   └── requirements.txt          ← Dependencias
│
├── ⚙️ CONFIGURACIÓN
│   ├── .env.example              ← Template de variables
│   ├── .gitignore                ← Archivos ignorados
│   ├── Dockerfile                ← Containerización
│   └── docker-compose.yml        ← Orquestación Docker
│
├── 📂 config/ - CONFIGURACIONES
│   ├── model_config.yaml         ← Modelos LLM
│   ├── agent_config.yaml         ← Configuración del agente
│   └── __init__.py
│
├── 📂 src/ - CÓDIGO FUENTE PRINCIPAL
│   ├── __init__.py
│   │
│   ├── 🧠 agents/
│   │   ├── touristic_agent.py    ← Agente turístico principal
│   │   └── __init__.py
│   │
│   ├── 🔧 handlers/
│   │   ├── tools.py              ← 7+ herramientas especializadas
│   │   └── __init__.py
│   │
│   ├── 🧠 llm/
│   │   ├── base.py               ← Clientes LLM (OpenAI, Anthropic, Groq)
│   │   └── __init__.py
│   │
│   ├── ✍️ prompt_engineering/
│   │   ├── prompts.py            ← Gestión de prompts
│   │   └── __init__.py
│   │
│   └── 🛠️ utils/
│       ├── config.py             ← Cargador de configuraciones YAML
│       ├── helpers.py            ← Logger, Preferences, Rate Limiter
│       └── __init__.py
│
├── 📂 data/ - BASE DE CONOCIMIENTO
│   ├── __init__.py
│   └── knowledge/
│       ├── huaraz_knowledge.py   ← Datos de Huaraz (atracciones, etc)
│       └── __init__.py
│
├── 📂 examples/ - EJEMPLOS DE USO
│   ├── basic_usage.py            ← Ejemplo 1: Uso básico
│   ├── create_itinerary.py       ← Ejemplo 2: Crear itinerarios
│   └── specialized_queries.py    ← Ejemplo 3: Consultas especializadas
│
└── 📂 notebooks/ - JUPYTER NOTEBOOKS
    └── experimentation.ipynb     ← Para experimentación interactiva
```

---

## 🗂️ DESCRIPCIÓN DE ARCHIVOS PRINCIPALES

### Documentación

| Archivo | Propósito | Tiempo |
|---------|-----------|--------|
| **QUICKSTART.md** | Instalación y primeros pasos | 5 min |
| **README.md** | Documentación completa | 15 min |
| **TECHNICAL.md** | Arquitectura y diseño | 20 min |
| **PROJECT_SUMMARY.md** | Resumen ejecutivo | 5 min |

### Código Principal

| Archivo | Propósito | Líneas |
|---------|-----------|--------|
| **main.py** | Aplicación principal | 180 |
| **src/agents/touristic_agent.py** | Agente inteligente | 150 |
| **src/handlers/tools.py** | Herramientas | 250 |
| **src/llm/base.py** | Clientes LLM | 120 |
| **src/prompt_engineering/prompts.py** | Prompts | 180 |
| **data/knowledge/huaraz_knowledge.py** | Base de datos | 200 |

### Configuración

| Archivo | Propósito |
|---------|-----------|
| **config/model_config.yaml** | Modelos y parámetros LLM |
| **config/agent_config.yaml** | Configuración del agente |
| **.env.example** | Template de variables de entorno |

### Ejemplos

| Archivo | Qué demuestra |
|---------|--------------|
| **examples/basic_usage.py** | Uso básico del chatbot |
| **examples/create_itinerary.py** | Creación de itinerarios personalizados |
| **examples/specialized_queries.py** | Consultas avanzadas |

### Deployment

| Archivo | Propósito |
|---------|-----------|
| **Dockerfile** | Imagen Docker |
| **docker-compose.yml** | Orquestación |
| **requirements.txt** | Dependencias Python |
| **setup.py** | Instalación del paquete |

---

## 🎯 CÓMO USAR ESTE ÍNDICE

### Si quieres...

**Instalar y ejecutar rápidamente**
→ Ve a [QUICKSTART.md](QUICKSTART.md)

**Entender qué se creó**
→ Ve a [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)

**Aprender a usar el chatbot**
→ Ve a [README.md](README.md)

**Entender la arquitectura interna**
→ Ve a [TECHNICAL.md](TECHNICAL.md)

**Ver ejemplos de código**
→ Abre carpeta `examples/`

**Experimentar interactivamente**
→ Abre `notebooks/experimentation.ipynb`

**Personalizar el código**
→ Lee [TECHNICAL.md](TECHNICAL.md) sección "Extensibilidad"

---

## 🚀 FLUJO RECOMENDADO

1. ✅ Lee **QUICKSTART.md** (5 min)
   - Aprenderás a instalar y ejecutar

2. ✅ Ejecuta **main.py**
   - Interactúa con el chatbot

3. ✅ Lee **PROJECT_SUMMARY.md** (5 min)
   - Entenderás qué se creó

4. ✅ Lee **README.md** (15 min)
   - Conocerás todas las características

5. ✅ Ejecuta los **ejemplos** en `examples/`
   - Verás el chatbot en acción

6. ✅ Abre **experimentation.ipynb**
   - Experimentarás con código

7. ✅ Lee **TECHNICAL.md** (20 min)
   - Comprenderás la arquitectura

8. ✅ Personaliza el código
   - Añade tus propias características

---

## 📊 ESTADÍSTICAS DEL PROYECTO

- **Total de archivos**: 25+
- **Líneas de código**: 1,200+
- **Clases implementadas**: 8
- **Herramientas del agente**: 7
- **Modelos LLM soportados**: 3
- **Ejemplos incluidos**: 3
- **Documentación**: 5 archivos
- **Páginas documentación**: 20+

---

## 🔗 ENLACES RÁPIDOS

### Documentación
- [README.md](README.md) - Documentación completa
- [QUICKSTART.md](QUICKSTART.md) - Instalación rápida
- [TECHNICAL.md](TECHNICAL.md) - Arquitectura
- [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Resumen

### Código
- [main.py](main.py) - Programa principal
- [examples/](examples/) - Ejemplos
- [src/](src/) - Código fuente
- [notebooks/experimentation.ipynb](notebooks/experimentation.ipynb) - Jupyter

### Configuración
- [config/model_config.yaml](config/model_config.yaml) - LLMs
- [config/agent_config.yaml](config/agent_config.yaml) - Agente
- [.env.example](.env.example) - Variables de entorno

---

## ❓ PREGUNTAS FRECUENTES

**¿Por dónde comienzo?**
→ [QUICKSTART.md](QUICKSTART.md)

**¿Cómo ejecuto el chatbot?**
→ `python main.py`

**¿Cómo cambio el modelo LLM?**
→ [TECHNICAL.md](TECHNICAL.md) o edita `config/model_config.yaml`

**¿Cómo añado nuevas atracciones?**
→ [TECHNICAL.md](TECHNICAL.md) - sección "Extensibilidad"

**¿Cómo creo nuevas herramientas?**
→ [TECHNICAL.md](TECHNICAL.md) - sección "Agregar una nueva herramienta"

**¿Dónde está el código?**
→ Carpeta `src/`

**¿Hay ejemplos?**
→ Carpeta `examples/`

**¿Cómo experimento?**
→ `notebooks/experimentation.ipynb`

---

## 🎓 CONTENIDO EDUCATIVO

Este proyecto es un excelente ejemplo de:

1. **IA Agéntica**: Cómo crear agentes que razonan y actúan
2. **LangChain**: Integración con LangChain y OpenAI/Anthropic/Groq
3. **Prompt Engineering**: Técnicas avanzadas de prompts
4. **Arquitectura de Software**: Diseño modular y escalable
5. **Python Profesional**: Código production-ready
6. **Documentación**: Cómo documentar correctamente

---

## 📝 NOTAS

- Todos los archivos están comentados en español
- El código es production-ready y bien documentado
- Fácil de extender y personalizar
- Sigue principios SOLID y patrones de diseño
- Incluye manejo de errores robusto

---

**Última actualización**: Enero 2025
**Versión**: 1.0.0
**Status**: ✅ COMPLETADO Y LISTO

---

*Comienza con [QUICKSTART.md](QUICKSTART.md) y ¡disfruta creando!* 🚀
