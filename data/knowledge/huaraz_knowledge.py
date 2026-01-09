"""
Base de datos de conocimiento sobre Huaraz
"""
from typing import List, Dict, Any
from dataclasses import dataclass


@dataclass
class Attraction:
    """Modelo de atracción turística"""
    name: str
    description: str
    location: str
    altitude: int
    difficulty: str  # bajo, medio, alto
    duration: str
    best_season: List[str]
    essentials: List[str]
    estimated_cost: str
    contact_info: str = ""


class HuarazKnowledgeBase:
    """Base de conocimiento sobre Huaraz"""
    
    ATTRACTIONS = {
        "laguna_paron": Attraction(
            name="Laguna Parón",
            description="Laguna alpina de agua turquesa ubicada en la Cordillera Blanca con vistas espectaculares al Nevado Piramide.",
            location="Pariac, Huaraz",
            altitude=4185,
            difficulty="medio",
            duration="8-10 horas",
            best_season=["mayo", "junio", "julio", "agosto", "septiembre"],
            essentials=["protector solar", "bloqueador labial", "gafas de sol", "agua", "snacks", "chaqueta"],
            estimated_cost="S/. 50-100 por persona (entrada + transporte)"
        ),
        "laguna_69": Attraction(
            name="Laguna 69",
            description="Laguna de color azul verdoso rodeada de montañas nevadas. Una de las más visitadas de Huaraz.",
            location="Quisma, Carhuaz",
            altitude=4600,
            difficulty="medio",
            duration="6-8 horas",
            best_season=["mayo", "junio", "julio", "agosto", "septiembre"],
            essentials=["agua abundante", "snacks energéticos", "protector solar", "chaqueta", "zapatos deportivos"],
            estimated_cost="S/. 80-150 por persona"
        ),
        "nevado_pastoruri": Attraction(
            name="Nevado Pastoruri",
            description="Glaciar accesible con vistas panorámicas. Ideal para quienes quieren experimentar nieve sin alpinismo técnico.",
            location="Ticapampa",
            altitude=5240,
            difficulty="medio-alto",
            duration="10-12 horas",
            best_season=["mayo", "junio", "julio", "agosto"],
            essentials=["ropa térmica", "protector solar fuerte", "bloqueador labial", "agua", "snacks", "gafas de sol oscuras"],
            estimated_cost="S/. 100-200 por persona"
        ),
        "laguna_llanganuco": Attraction(
            name="Laguna Llanganuco",
            description="Dos lagunas conectadas (Orcon y Ngorongoro) con impresionantes vistas de nevados.",
            location="Yungay",
            altitude=3850,
            difficulty="bajo",
            duration="6 horas",
            best_season=["todo el año"],
            essentials=["agua", "snacks", "protector solar", "chaqueta", "cámara"],
            estimated_cost="S/. 50-80 por persona"
        ),
        "chavin_de_huantar": Attraction(
            name="Chavín de Huántar",
            description="Sitio arqueológico importante de la cultura Chavín con túneles subterráneos y plazas ceremoniales.",
            location="Chavín de Huántar",
            altitude=3180,
            difficulty="bajo",
            duration="4-5 horas",
            best_season=["todo el año"],
            essentials=["cámara", "agua", "linterna o frontal"],
            estimated_cost="S/. 30-50 entrada + transporte"
        )
    }
    
    ACTIVITIES = {
        "trekking_cordillera": {
            "name": "Trekking en Cordillera Blanca",
            "types": ["Santa Cruz Trek (4-5 días)", "Alpamayo Trek (7 días)", "Inca Trail alternativo"],
            "difficulty": "medio-alto",
            "best_for": "aventureros con experiencia",
            "cost": "S/. 1500-3000 por persona"
        },
        "mountain_biking": {
            "name": "Mountain Biking",
            "types": ["Circuito Valle de Huaraz", "Downhill desde Laguna Parón"],
            "difficulty": "medio",
            "best_for": "ciclistas experimentados",
            "cost": "S/. 150-300 por día"
        },
        "rock_climbing": {
            "name": "Escalada en Roca",
            "types": ["Crags cercanos", "Grandes paredes"],
            "difficulty": "variable",
            "best_for": "escaladores",
            "cost": "S/. 300-500 por día con guía"
        },
        "cultural_tours": {
            "name": "Tours Culturales",
            "types": ["Mercado tradicional", "Pueblos indígenas", "Artesanías locales"],
            "difficulty": "bajo",
            "best_for": "todos",
            "cost": "S/. 50-150 por persona"
        }
    }
    
    ACCOMMODATIONS = {
        "budget": [
            {"name": "Casa de Nuestros Amigos", "price": "S/. 30-50 noche", "location": "Centro"},
            {"name": "Albergue Perla de Los Andes", "price": "S/. 40-60 noche", "location": "Jr. Comercio"},
            {"name": "Hostel Churup", "price": "S/. 35-55 noche", "location": "Jirón Fitzcarrald"}
        ],
        "mid_range": [
            {"name": "Hotel Huaraz", "price": "S/. 100-150 noche", "location": "Plaza de Armas"},
            {"name": "Hotel Andino", "price": "S/. 80-120 noche", "location": "Centro"},
            {"name": "Dreamers Hostel", "price": "S/. 90-130 noche", "location": "Jr. Comercio"}
        ],
        "luxury": [
            {"name": "Gran Hotel Huaraz", "price": "S/. 200-300 noche", "location": "Plaza de Armas"},
            {"name": "Hotel El Tejada", "price": "S/. 180-250 noche", "location": "Centro"}
        ]
    }
    
    @classmethod
    def get_attraction(cls, attraction_key: str) -> Attraction:
        """Obtener información de una atracción"""
        return cls.ATTRACTIONS.get(attraction_key)
    
    @classmethod
    def get_all_attractions(cls) -> Dict[str, Attraction]:
        """Obtener todas las atracciones"""
        return cls.ATTRACTIONS
    
    @classmethod
    def get_activity(cls, activity_key: str) -> Dict[str, Any]:
        """Obtener información de una actividad"""
        return cls.ACTIVITIES.get(activity_key)
    
    @classmethod
    def search_by_difficulty(cls, difficulty: str) -> List[Attraction]:
        """Buscar atracciones por nivel de dificultad"""
        return [
            attr for attr in cls.ATTRACTIONS.values()
            if attr.difficulty.lower() == difficulty.lower()
        ]
    
    @classmethod
    def search_by_season(cls, season: str) -> List[Attraction]:
        """Buscar atracciones recomendadas para una temporada"""
        return [
            attr for attr in cls.ATTRACTIONS.values()
            if season.lower() in [m.lower() for m in attr.best_season]
        ]
    
    @classmethod
    def get_accommodations_by_budget(cls, budget: str) -> List[Dict[str, str]]:
        """Obtener alojamientos por presupuesto"""
        return cls.ACCOMMODATIONS.get(budget.lower(), [])
