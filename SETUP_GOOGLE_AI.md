# ⚙️ CONFIGURACIÓN GOOGLE AI - PASOS RÁPIDOS

## 1️⃣ Obtener tu Google API Key

### Opción A: Con Google Cloud Console (Recomendado)
1. Ve a https://aistudio.google.com/app/apikey
2. Haz clic en "Create API key in new project"
3. Copia la API key generada

### Opción B: Usar Google AI Studio directamente
1. Accede a https://aistudio.google.com
2. No necesitas pagar (uso gratuito limitado)
3. Obtén tu API key en https://aistudio.google.com/app/apikey

## 2️⃣ Configurar el .env

```bash
# Crear archivo .env basado en el template
cp .env.example .env

# Editar .env y añadir tu API key
# Windows: notepad .env
# Linux/Mac: nano .env
```

Contenido del archivo `.env`:
```
GOOGLE_API_KEY=tu_api_key_aqui
DEBUG=false
LOG_LEVEL=INFO
```

## 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

## 4️⃣ Probar la instalación

```bash
# Prueba básica
python test_imports.py

# Prueba completa con Google AI
python test_chatbot.py

# Ejecutar chatbot interactivo
python main.py
```

## 🔧 Solución de problemas

### Error: GOOGLE_API_KEY not configured
**Solución**: Verifica que el archivo `.env` existe y tiene la API key correcta

### Error: ModuleNotFoundError
**Solución**: 
```bash
pip install --upgrade langchain langchain-google-genai langgraph
```

### Error: rate limit exceeded
**Solución**: Usa Groq o espera un minuto antes de intentar de nuevo

## 📝 Ejemplos de uso

### Ejecutar chatbot interactivo
```bash
python main.py
```

### Ejecutar ejemplos
```bash
python examples/basic_usage.py
python examples/create_itinerary.py
python examples/specialized_queries.py
```

### Experimentar en Jupyter
```bash
jupyter notebook notebooks/experimentation.ipynb
```

## ✅ Checklist

- [ ] API key de Google obtenida
- [ ] Archivo `.env` creado
- [ ] Dependencias instaladas (`pip install -r requirements.txt`)
- [ ] Prueba importada correctamente (`python test_imports.py`)
- [ ] Chatbot ejecutado (`python main.py`)

## 🚀 Próximos pasos

Una vez configurado:
1. Lee [README.md](README.md) para documentación completa
2. Prueba los ejemplos en `examples/`
3. Personaliza según necesites

---

¿Necesitas ayuda? Revisa la documentación completa en [README.md](README.md)
