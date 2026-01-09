"""
Agente Turístico con capacidades AgentIC
"""
from typing import Optional, List, Dict, Any
from langgraph.prebuilt import create_react_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.memory import ConversationBufferMemory
from src.handlers.tools import (
    search_attractions,
    get_attraction_details,
    get_activity_recommendations,
    search_accommodations,
    get_best_season,
    get_altitude_advice,
    create_daily_itinerary
)
from src.prompt_engineering.prompts import PromptManager


class TouristicAgent:
    """Agente turístico con capacidades agénticas"""
    
    def __init__(self, llm: Any, max_iterations: int = 10):
        """
        Inicializar el agente turístico.
        
        Args:
            llm: Modelo de lenguaje a utilizar
            max_iterations: Máximo número de iteraciones del agente
        """
        self.llm = llm
        self.max_iterations = max_iterations
        self.tools = self._setup_tools()
        self.memory = ConversationBufferMemory(memory_key="chat_history")
        self.agent_executor = self._create_agent_executor()
    
    def _setup_tools(self) -> List:
        """Configurar las herramientas disponibles para el agente"""
        return [
            search_attractions,
            get_attraction_details,
            get_activity_recommendations,
            search_accommodations,
            get_best_season,
            get_altitude_advice,
            create_daily_itinerary
        ]
    
    def _create_agent_executor(self) -> Any:
        """Crear el ejecutor del agente"""
        # Crear agente reactivo con herramientas
        agent = create_react_agent(
            self.llm,
            self.tools,
            state_modifier=PromptManager.get_system_prompt()
        )
        
        return agent
    
    def process_query(self, user_input: str) -> Dict[str, Any]:
        """
        Procesar una consulta del usuario.
        
        Args:
            user_input: Pregunta del usuario
        
        Returns:
            Respuesta del agente
        """
        try:
            # Invocar el agente
            response = self.agent_executor.invoke({
                "input": user_input,
                "messages": []
            })
            
            # Extraer la respuesta
            output_text = ""
            if isinstance(response, dict) and "output" in response:
                output_text = response["output"]
            elif isinstance(response, str):
                output_text = response
            else:
                output_text = str(response)
            
            # Guardar en memoria
            self.memory.save_context(
                {"input": user_input},
                {"output": output_text}
            )
            
            return {
                "success": True,
                "response": output_text,
                "tool_calls": []
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "response": "Disculpa, ocurrió un error procesando tu consulta. Por favor, intenta de nuevo."
            }
    
    def get_conversation_history(self) -> str:
        """Obtener historial de conversación"""
        return self.memory.buffer
    
    def clear_memory(self) -> None:
        """Limpiar la memoria de conversación"""
        self.memory.clear()
    
    def set_user_context(self, context: Dict[str, Any]) -> None:
        """
        Establecer contexto del usuario (preferencias, restricciones, etc.).
        
        Args:
            context: Diccionario con información del usuario
                    Ejemplo: {"budget": "mid_range", "fitness_level": "medio", "interests": ["nature", "culture"]}
        """
        self.user_context = context
        context_msg = f"Contexto del usuario: {context}"
        self.memory.save_context(
            {"input": "Información del usuario"},
            {"output": context_msg}
        )


class AgentBuilder:
    """Constructor para crear agentes turísticos personalizados"""
    
    @staticmethod
    def create_agent(
        llm: Any,
        agent_type: str = "standard",
        max_iterations: int = 10
    ) -> TouristicAgent:
        """
        Crear un agente turístico personalizado.
        
        Args:
            llm: Modelo de lenguaje
            agent_type: Tipo de agente ("standard", "expert", "budget")
            max_iterations: Máximo de iteraciones
        
        Returns:
            Instancia del agente
        """
        agent = TouristicAgent(llm, max_iterations)
        
        if agent_type == "expert":
            # Para expertos: más iteraciones y herramientas avanzadas
            agent.max_iterations = 15
        elif agent_type == "budget":
            # Para presupuesto: enfoque en opciones económicas
            pass
        
        return agent
