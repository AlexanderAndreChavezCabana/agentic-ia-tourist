"""
Herramientas para el Agente Turístico
"""
from typing import List, Dict, Any, Optional
from langchain_core.tools import tool
from data.knowledge.huaraz_knowledge import HuarazKnowledgeBase, Attraction
import requests
import os
from datetime import datetime


@tool
def search_attractions(query: str, difficulty: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Buscar atracciones turísticas en Huaraz.
    
    Args:
        query: Término de búsqueda
        difficulty: Nivel de dificultad (bajo, medio, alto)
    
    Returns:
        Lista de atracciones relevantes
    """
    kb = HuarazKnowledgeBase()
    
    if difficulty:
        attractions = kb.search_by_difficulty(difficulty)
    else:
        attractions = list(kb.get_all_attractions().values())
    
    # Filtrar por query
    query_lower = query.lower()
    results = [
        {
            "name": attr.name,
            "description": attr.description,
            "altitude": attr.altitude,
            "duration": attr.duration,
            "difficulty": attr.difficulty
        }
        for attr in attractions
        if query_lower in attr.name.lower() or query_lower in attr.description.lower()
    ]
    
    return results or [{"message": "No se encontraron atracciones para tu búsqueda"}]


@tool
def get_attraction_details(attraction_name: str) -> Dict[str, Any]:
    """
    Obtener detalles completos de una atracción.
    
    Args:
        attraction_name: Nombre de la atracción
    
    Returns:
        Detalles completos de la atracción
    """
    kb = HuarazKnowledgeBase()
    attractions = kb.get_all_attractions()
    
    # Buscar por coincidencia aproximada
    for key, attr in attractions.items():
        if attraction_name.lower() in attr.name.lower() or attr.name.lower() in attraction_name.lower():
            return {
                "name": attr.name,
                "description": attr.description,
                "location": attr.location,
                "altitude": f"{attr.altitude}m",
                "difficulty": attr.difficulty,
                "duration": attr.duration,
                "best_season": ", ".join(attr.best_season),
                "essentials": attr.essentials,
                "cost": attr.estimated_cost
            }
    
    return {"error": f"No se encontraron detalles para {attraction_name}"}


@tool
def get_activity_recommendations(activity_type: str, difficulty: Optional[str] = None) -> Dict[str, Any]:
    """
    Obtener recomendaciones de actividades.
    
    Args:
        activity_type: Tipo de actividad (trekking, climbing, cultural_tours, etc.)
        difficulty: Nivel de dificultad deseado
    
    Returns:
        Detalles de la actividad recomendada
    """
    kb = HuarazKnowledgeBase()
    activities = kb.ACTIVITIES
    
    # Buscar actividad
    for key, activity in activities.items():
        if activity_type.lower() in key.lower() or activity_type.lower() in activity.get("name", "").lower():
            if difficulty and activity.get("difficulty").lower() != difficulty.lower():
                continue
            return activity
    
    return {"error": f"No se encontraron actividades del tipo {activity_type}"}


@tool
def search_accommodations(budget: str, location: str = "Huaraz") -> List[Dict[str, str]]:
    """
    Buscar alojamientos según presupuesto.
    
    Args:
        budget: Presupuesto (budget, mid_range, luxury)
        location: Ubicación
    
    Returns:
        Lista de alojamientos disponibles
    """
    kb = HuarazKnowledgeBase()
    accommodations = kb.get_accommodations_by_budget(budget)
    
    if not accommodations:
        return [{"message": f"No hay alojamientos disponibles para presupuesto: {budget}"}]
    
    return accommodations


@tool
def get_best_season(travel_style: str) -> Dict[str, Any]:
    """
    Obtener la mejor época para viajar según estilo de viaje.
    
    Args:
        travel_style: Estilo de viaje (trekking, casual, photography)
    
    Returns:
        Recomendación de temporada
    """
    recommendations = {
        "trekking": {
            "best_months": ["mayo", "junio", "julio", "agosto"],
            "reason": "Cielo claro y poco riesgo de lluvia",
            "considerations": "Frío intenso, especialmente por las noches"
        },
        "casual": {
            "best_months": ["mayo", "junio", "julio", "agosto", "septiembre"],
            "reason": "Clima estable y buena visibilidad",
            "considerations": "Evitar noviembre a marzo por lluvia"
        },
        "photography": {
            "best_months": ["mayo", "junio", "julio", "agosto"],
            "reason": "Máxima claridad atmosférica y cielo azul",
            "considerations": "Temperaturas bajas, llevar protección"
        },
        "cultural": {
            "best_months": ["todo el año"],
            "reason": "Las festividades ocurren durante el año",
            "considerations": "Verificar fechas de festivales locales"
        }
    }
    
    return recommendations.get(
        travel_style.lower(),
        {"message": f"Estilo de viaje no reconocido: {travel_style}"}
    )


@tool
def get_altitude_advice() -> Dict[str, Any]:
    """
    Obtener consejos para evitar el mal de altura.
    
    Returns:
        Consejos y recomendaciones
    """
    return {
        "symptoms": ["dolor de cabeza", "mareos", "fatiga", "dificultad para respirar"],
        "prevention": [
            "Aclimatarse 1-2 días en Huaraz antes de actividades de altura",
            "Hidratarse abundantemente",
            "Evitar alcohol y cafeína en exceso",
            "Comer carbohidratos",
            "Ascender lentamente"
        ],
        "treatment": [
            "Descansar a una altitud menor",
            "Beber agua y té de coca",
            "Si empeora, descender inmediatamente",
            "Considerar oxígeno suplementario"
        ],
        "when_to_seek_help": [
            "Síntomas que empeoran después de 24 horas",
            "Dificultad extrema para respirar",
            "Confusión mental"
        ]
    }


@tool
def create_daily_itinerary(attractions: List[str], duration_hours: int) -> Dict[str, Any]:
    """
    Crear un itinerario diario basado en atracciones.
    
    Args:
        attractions: Lista de atracciones a visitar
        duration_hours: Horas disponibles para la actividad
    
    Returns:
        Itinerario sugerido
    """
    kb = HuarazKnowledgeBase()
    schedule = []
    
    start_time = 6  # 6 AM
    
    for attraction_name in attractions:
        attraction = None
        for attr in kb.get_all_attractions().values():
            if attraction_name.lower() in attr.name.lower():
                attraction = attr
                break
        
        if attraction:
            schedule.append({
                "time": f"{start_time}:00",
                "activity": f"Visita a {attraction.name}",
                "duration": attraction.duration,
                "essentials": attraction.essentials
            })
            # Incrementar tiempo (simplificado)
            start_time += 3
    
    return {
        "day_schedule": schedule,
        "total_attractions": len(schedule),
        "estimated_completion": f"{start_time}:00 aproximadamente",
        "tips": ["Llevar suficiente agua", "Usar protector solar", "Llevar snacks energéticos"]
    }


@tool
def get_current_weather(location: str = "Huaraz") -> str:
    """
    Obtiene el clima actual en tiempo real de Huaraz, Perú.
    Incluye temperatura, sensación térmica, humedad, viento, y descripción del clima.
    
    Args:
        location: Ciudad (default: "Huaraz")
    
    Returns:
        Información detallada del clima actual
    """
    try:
        # API Key de OpenWeatherMap (requiere configuración en .env)
        api_key = os.getenv("OPENWEATHER_API_KEY")
        
        if not api_key:
            # Información estática si no hay API key
            return """🌤️ **Clima en Huaraz, Perú**

📍 **Ubicación**: 3,052 msnm
🌡️ **Temperatura promedio**: 
   - Día: 18-22°C
   - Noche: 5-8°C

📅 **Temporadas**:
- **Temporada Seca** (Mayo - Octubre): ☀️ Días soleados, noches frías. Ideal para trekking.
- **Temporada de Lluvias** (Noviembre - Abril): 🌧️ Lluvias frecuentes, principalmente por las tardes.

💡 **Recomendación**: Para clima actual en tiempo real, consulta weather.com o configura OPENWEATHER_API_KEY.

⚠️ **Importante**: Por la altitud, la diferencia térmica entre día y noche es significativa. Siempre lleva ropa abrigada."""
        
        # Consultar API de OpenWeatherMap
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": f"{location},PE",  # PE = Perú
            "appid": api_key,
            "units": "metric",  # Celsius
            "lang": "es"
        }
        
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Extraer información
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        temp_min = data["main"]["temp_min"]
        temp_max = data["main"]["temp_max"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        description = data["weather"][0]["description"].capitalize()
        wind_speed = data["wind"]["speed"]
        clouds = data["clouds"]["all"]
        
        # Obtener hora local
        now = datetime.now().strftime("%H:%M")
        
        # Formatear respuesta
        weather_info = f"""🌤️ **Clima Actual en {location}, Perú**

⏰ **Hora**: {now}
🌡️ **Temperatura**: {temp}°C (sensación térmica: {feels_like}°C)
📊 **Rango**: Min {temp_min}°C / Max {temp_max}°C
☁️ **Condición**: {description}
💧 **Humedad**: {humidity}%
💨 **Viento**: {wind_speed} m/s
☁️ **Nubosidad**: {clouds}%
🏔️ **Presión atmosférica**: {pressure} hPa

📍 **Altitud**: 3,052 msnm
💡 **Consejo**: Por la altitud, lleva siempre ropa abrigada para la noche, incluso si el día está cálido.

🧥 **Qué llevar**:
{'- Protector solar (radiación UV alta en altura)' if clouds < 50 else '- Impermeable o poncho'}
- Gorro y bloqueador labial
- Capas de ropa (sistema de 3 capas)
- Hidratación constante
"""
        
        return weather_info
        
    except requests.exceptions.RequestException as e:
        return f"""⚠️ No pude obtener el clima en tiempo real. 

🌤️ **Clima Típico en Huaraz**:
- **Mayo-Oct** (Seco): ☀️ Días soleados 18-22°C, noches frías 5-8°C
- **Nov-Abr** (Lluvias): 🌧️ Lluvias por la tarde, 15-20°C

💡 Para clima actual, consulta: weather.com o accuweather.com

Error técnico: {str(e)}"""
    except Exception as e:
        return f"Error al consultar clima: {str(e)}"


@tool 
def get_weather_forecast(days: int = 3) -> str:
    """
    Obtiene el pronóstico del clima para los próximos días en Huaraz.
    
    Args:
        days: Número de días del pronóstico (1-5)
    
    Returns:
        Pronóstico del clima
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    if not api_key:
        return """📅 **Pronóstico General para Huaraz**

**Temporada Seca** (Mayo - Octubre):
- ☀️ Días: Soleado, 18-22°C
- 🌙 Noches: Frío, 5-8°C
- 💧 Lluvias: Mínimas

**Temporada de Lluvias** (Noviembre - Abril):
- 🌤️ Mañanas: Despejado, 15-18°C
- 🌧️ Tardes: Lluvias frecuentes
- ⛈️ Noche: Frío con posible lluvia

💡 Configura OPENWEATHER_API_KEY para pronósticos en tiempo real."""
    
    try:
        base_url = "http://api.openweathermap.org/data/2.5/forecast"
        params = {
            "q": "Huaraz,PE",
            "appid": api_key,
            "units": "metric",
            "lang": "es",
            "cnt": min(days * 8, 40)  # 8 mediciones por día
        }
        
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        forecast_text = "📅 **Pronóstico del Clima - Huaraz**\n\n"
        
        # Agrupar por día
        current_date = None
        for item in data["list"][:days*8]:
            date = datetime.fromtimestamp(item["dt"]).strftime("%Y-%m-%d")
            time = datetime.fromtimestamp(item["dt"]).strftime("%H:%M")
            
            if date != current_date:
                current_date = date
                day_name = datetime.fromtimestamp(item["dt"]).strftime("%A, %d de %B")
                forecast_text += f"\n**{day_name}**\n"
            
            temp = item["main"]["temp"]
            desc = item["weather"][0]["description"]
            forecast_text += f"   • {time}: {temp}°C - {desc}\n"
        
        forecast_text += "\n💡 **Tip**: En Huaraz el clima puede cambiar rápidamente. Lleva ropa por capas."
        
        return forecast_text
        
    except Exception as e:
        return f"Error al obtener pronóstico: {str(e)}"
