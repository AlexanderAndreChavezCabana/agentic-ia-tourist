"""
Agente Turístico con capacidades AgentIC
"""
from typing import Optional, List, Dict, Any
from langgraph.prebuilt import create_react_agent
from langchain_core.prompts import ChatPromptTemplate
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
        self.conversation_history: List[Dict[str, str]] = []
        self.user_context: Dict[str, Any] = {}
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
        # create_react_agent solo acepta model y tools como argumentos principales
        agent = create_react_agent(
            self.llm,
            self.tools
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
            # Invocar el agente con formato correcto para LangGraph
            # create_react_agent espera: {"messages": [HumanMessage(content=...)]}
            from langchain_core.messages import HumanMessage
            
            response = self.agent_executor.invoke({
                "messages": [HumanMessage(content=user_input)]
            })
            
            # Extraer la respuesta del último mensaje
            output_text = ""
            if isinstance(response, dict) and "messages" in response:
                # Obtener el último mensaje que no sea del usuario
                messages = response["messages"]
                if messages:
                    last_message = messages[-1]
                    # Manejar diferentes formatos de contenido
                    if hasattr(last_message, 'content'):
                        content = last_message.content
                        # Si es una lista de dicts (formato de Google), extraer el texto
                        if isinstance(content, list) and len(content) > 0 and isinstance(content[0], dict):
                            output_text = content[0].get('text', str(content))
                        else:
                            output_text = str(content)
                    else:
                        output_text = str(last_message)
            elif isinstance(response, str):
                output_text = response
            else:
                output_text = str(response)
            
            # Guardar en historial de conversación
            self.conversation_history.append({
                "user": user_input,
                "assistant": output_text
            })
            
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
        history_text = ""
        for exchange in self.conversation_history:
            history_text += f"Usuario: {exchange['user']}\nAsistente: {exchange['assistant']}\n\n"
        return history_text
    
    def clear_memory(self) -> None:
        """Limpiar la memoria de conversación"""
        self.conversation_history = []
    
    def set_user_context(self, context: Dict[str, Any]) -> None:
        """
        Establecer contexto del usuario (preferencias, restricciones, etc.).
        
        Args:
            context: Diccionario con información del usuario
                    Ejemplo: {"budget": "mid_range", "fitness_level": "medio", "interests": ["nature", "culture"]}
        """
        self.user_context = context
        context_msg = f"Contexto del usuario: {context}"
        self.conversation_history.append({
            "user": "Información del usuario",
            "assistant": context_msg
        })


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
