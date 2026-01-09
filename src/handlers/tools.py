"""
Herramientas para el Agente Turístico
"""
from typing import List, Dict, Any, Optional
from langchain_core.tools import tool
from data.knowledge.huaraz_knowledge import HuarazKnowledgeBase, Attraction


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
