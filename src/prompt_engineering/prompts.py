"""
Módulo de Prompt Engineering para el Chatbot Turístico
"""
from typing import List, Dict, Any
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate


class PromptManager:
    """Gestor centralizado de prompts"""
    
    @staticmethod
    def get_system_prompt() -> str:
        """Prompt del sistema para el asistente turístico"""
        return """Eres un asistente turístico experto especializado en Huaraz, Perú. 

Tu objetivo es:
1. Proporcionar información detallada sobre atracciones turísticas
2. Recomendar rutas y actividades según el perfil del turista
3. Dar consejos sobre alojamiento, gastronomía y transporte
4. Considerar el clima, temporada y nivel de actividad física
5. Ofrecer recomendaciones personalizadas

Información sobre Huaraz:
- Ubicación: Ancash, Perú a 3,052 metros sobre el nivel del mar
- Clima: Templado, frío en las noches, lluvias de noviembre a marzo
- Atracciones principales: Laguna Parón, Laguna Llanganuco, Nevado Pastoruri, Laguna 69
- Mejor época: Mayo a octubre (estación seca)

Siempre:
- Responde en español de manera amable y profesional
- Proporciona información práctica y útil
- Sugiere alternativas según el presupuesto y tiempo
- Advierte sobre riesgos de altitud (mal de montaña)
- Recomienda artículos esenciales para llevar
"""
    
    @staticmethod
    def get_tourism_question_prompt() -> ChatPromptTemplate:
        """Prompt para procesar preguntas turísticas"""
        system_message = SystemMessagePromptTemplate.from_template(
            PromptManager.get_system_prompt()
        )
        
        human_message = HumanMessagePromptTemplate.from_template(
            "{user_input}"
        )
        
        return ChatPromptTemplate.from_messages([
            system_message,
            human_message
        ])
    
    @staticmethod
    def get_routing_prompt() -> ChatPromptTemplate:
        """Prompt para enrutamiento de consultas"""
        system_template = """Analiza la siguiente consulta y clasifícala en una de estas categorías:
        
Categories:
1. ATTRACTIONS - Información sobre atracciones turísticas
2. ACCOMMODATIONS - Información sobre alojamiento
3. ACTIVITIES - Recomendaciones de actividades
4. ROUTES - Información sobre rutas y itinerarios
5. PRACTICAL_INFO - Información práctica (clima, documentos, etc.)
6. GENERAL - Preguntas generales

Responde SOLO con el nombre de la categoría."""
        
        human_template = "{query}"
        
        return ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(system_template),
            HumanMessagePromptTemplate.from_template(human_template)
        ])
    
    @staticmethod
    def get_attraction_details_prompt() -> ChatPromptTemplate:
        """Prompt para obtener detalles de atracción"""
        system_message = SystemMessagePromptTemplate.from_template(
            PromptManager.get_system_prompt() + 
            "\n\nProporciona detalles completos sobre la atracción solicitada."
        )
        
        human_message = HumanMessagePromptTemplate.from_template(
            "Cuéntame sobre: {attraction_name}"
        )
        
        return ChatPromptTemplate.from_messages([
            system_message,
            human_message
        ])
    
    @staticmethod
    def get_itinerary_prompt() -> ChatPromptTemplate:
        """Prompt para crear itinerarios"""
        system_template = PromptManager.get_system_prompt() + """

Cuando se te pida crear un itinerario:
1. Estructura día por día
2. Incluye horarios recomendados
3. Distancias y tiempos de viaje
4. Nivel de dificultad
5. Artículos a llevar
6. Costo estimado
7. Alternativas según presupuesto"""
        
        human_template = "{itinerary_request}"
        
        system_message = SystemMessagePromptTemplate.from_template(system_template)
        human_message = HumanMessagePromptTemplate.from_template(human_template)
        
        return ChatPromptTemplate.from_messages([
            system_message,
            human_message
        ])


class PromptEngineer:
    """Ingeniero de prompts para optimización"""
    
    @staticmethod
    def add_context_to_prompt(base_prompt: str, context: Dict[str, Any]) -> str:
        """Añade contexto adicional a un prompt"""
        context_str = "\n\nContexto adicional:\n"
        for key, value in context.items():
            context_str += f"- {key}: {value}\n"
        return base_prompt + context_str
    
    @staticmethod
    def create_few_shot_prompt(examples: List[Dict[str, str]], task: str) -> str:
        """Crear prompt con ejemplos few-shot"""
        prompt = f"Tarea: {task}\n\nEjemplos:\n"
        
        for i, example in enumerate(examples, 1):
            prompt += f"\nEjemplo {i}:\n"
            for key, value in example.items():
                prompt += f"  {key}: {value}\n"
        
        prompt += "\nAhora responde la siguiente consulta:"
        return prompt
