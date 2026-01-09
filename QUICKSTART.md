# 🚀 GUÍA DE INSTALACIÓN RÁPIDA

## Pasos Rápidos (5 minutos)

### 1. Prerequisitos
- Python 3.9 o superior
- pip (viene con Python)
- Una API key de OpenAI, Anthropic o Groq

### 2. Configuración

```bash
# Navega a la carpeta del proyecto
cd chatbot_turismo_huaraz

# Crea un entorno virtual (RECOMENDADO)
python -m venv venv

# Activa el entorno virtual
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate

# Instala las dependencias
pip install -r requirements.txt
```

### 3. Configurar API Key

**Opción A: Archivo .env (RECOMENDADO)**

```bash
# Copia el archivo de ejemplo
cp .env.example .env

# Edita .env y añade tu API key:
# OPENAI_API_KEY=sk-tu-clave-aqui
# O
# ANTHROPIC_API_KEY=tu-clave-aqui
# O  
# GROQ_API_KEY=tu-clave-aqui
```

**Opción B: Variables de entorno del sistema**

```bash
# Windows (PowerShell)
$env:OPENAI_API_KEY="sk-tu-clave"

# Mac/Linux
export OPENAI_API_KEY="sk-tu-clave"
```

### 4. ¡Ejecutar!

```bash
# Modo interactivo
python main.py

# O ejecuta un ejemplo
python examples/basic_usage.py
```

---

## Obtener API Keys

### OpenAI
1. Ve a https://platform.openai.com/api-keys
2. Crea una nueva API key
3. Cópiala en tu archivo .env

### Anthropic (Claude)
1. Ve a https://console.anthropic.com/
2. Crea una nueva API key
3. Cópiala en tu archivo .env

### Groq (Rápido y Gratuito)
1. Ve a https://console.groq.com/
2. Crea una nueva API key
3. Cópiala en tu archivo .env

---

## Primer Uso

```bash
# Inicia el chatbot
python main.py

# En el prompt, intenta:
> ¿Cuáles son las mejores atracciones en Huaraz?
> Quiero visitar Laguna 69, ¿cuándo debo ir?
> Dame un itinerario de 3 días
> Cómo evitar el mal de altura

# Para salir:
> salir
```

---

## Solución de Problemas Comunes

### ❌ Error: "No module named 'langchain'"
```bash
# Solución: Reinstala las dependencias
pip install -r requirements.txt --upgrade
```

### ❌ Error: "OPENAI_API_KEY not configured"
- Verifica que tu archivo .env existe en la raíz del proyecto
- Verifica que la API key sea correcta
- Asegúrate de que el archivo .env no está vacío

### ❌ Error: "Max tokens exceeded"
- Edita `config/model_config.yaml`
- Reduce el valor de `max_tokens` (ej: 1024)

### ❌ Respuestas muy lentas
- Usa Groq en lugar de OpenAI (más rápido)
- Cambia en `main.py`: `ChatbotTouristico(llm_provider="groq")`

---

## Estructura de Archivos Importantes

```
chatbot_turismo_huaraz/
├── .env                 ← Tu archivo de configuración (CRÉALO)
├── main.py             ← Ejecutable principal
├── requirements.txt    ← Dependencias
├── config/            ← Configuraciones YAML
├── src/              ← Código fuente
└── examples/         ← Scripts de ejemplo
```

---

## Próximos Pasos

1. ✅ Abre el README.md para documentación completa
2. ✅ Explora los archivos en `examples/` para ver capacidades
3. ✅ Personaliza `config/agent_config.yaml`
4. ✅ Añade más atracciones en `data/knowledge/huaraz_knowledge.py`

---

## Comandos Útiles

```bash
# Ver estructura del proyecto
tree

# Ejecutar un ejemplo específico
python examples/basic_usage.py

# Ejecutar en modo Docker
docker-compose up

# Ver logs
tail -f logs/chatbot.log

# Actualizar dependencias
pip install -r requirements.txt --upgrade
```

---

## 💡 Tips

- Usa Groq para pruebas (gratis y rápido)
- Personaliza los prompts en `src/prompt_engineering/prompts.py`
- Añade datos en `data/knowledge/huaraz_knowledge.py`
- Lee el código comentado para entender la arquitectura

---

¡Listo! Ahora puedes conversar con tu chatbot turístico. 🎉
