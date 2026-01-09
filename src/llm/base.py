"""
Módulo de clientes LLM - Integración con múltiples proveedores
"""
import os
from typing import Optional, Dict, Any
from abc import ABC, abstractmethod

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq
from langchain_core.language_model import BaseLanguageModel


class LLMClient(ABC):
    """Clase base para clientes LLM"""
    
    @abstractmethod
    def get_model(self) -> BaseLanguageModel:
        """Obtener instancia del modelo"""
        pass


class OpenAIClient(LLMClient):
    """Cliente para OpenAI"""
    
    def __init__(
        self,
        model_name: str = "gpt-4-turbo",
        temperature: float = 0.7,
        max_tokens: int = 2048,
        api_key: Optional[str] = None
    ):
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
    
    def get_model(self) -> BaseLanguageModel:
        return ChatOpenAI(
            model_name=self.model_name,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            api_key=self.api_key
        )


class AnthropicClient(LLMClient):
    """Cliente para Anthropic Claude"""
    
    def __init__(
        self,
        model_name: str = "claude-3-opus-20240229",
        temperature: float = 0.7,
        max_tokens: int = 2048,
        api_key: Optional[str] = None
    ):
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
    
    def get_model(self) -> BaseLanguageModel:
        return ChatAnthropic(
            model_name=self.model_name,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            api_key=self.api_key
        )


class GroqClient(LLMClient):
    """Cliente para Groq"""
    
    def __init__(
        self,
        model_name: str = "mixtral-8x7b-32768",
        temperature: float = 0.7,
        max_tokens: int = 2048,
        api_key: Optional[str] = None
    ):
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
    
    def get_model(self) -> BaseLanguageModel:
        return ChatGroq(
            model_name=self.model_name,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            api_key=self.api_key
        )


class LLMFactory:
    """Factory para crear clientes LLM"""
    
    _clients: Dict[str, LLMClient] = {
        "openai": OpenAIClient,
        "anthropic": AnthropicClient,
        "groq": GroqClient,
    }
    
    @classmethod
    def create_client(cls, provider: str, **kwargs) -> LLMClient:
        """Crear cliente LLM por proveedor"""
        if provider not in cls._clients:
            raise ValueError(f"Proveedor no soportado: {provider}")
        
        client_class = cls._clients[provider]
        return client_class(**kwargs)
    
    @classmethod
    def get_model(cls, provider: str, **kwargs) -> BaseLanguageModel:
        """Obtener modelo LLM directo"""
        client = cls.create_client(provider, **kwargs)
        return client.get_model()
