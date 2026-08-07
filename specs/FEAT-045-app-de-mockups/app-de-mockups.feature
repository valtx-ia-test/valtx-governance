# language: es

@REQ-MOCK-001
Escenario: Generar mockup a partir de descripción en lenguaje natural
  Dado que el usuario proporciona una descripción "Crear un botón rojo con texto 'Enviar'"
  Cuando el sistema genera el mockup
  Entonces el sistema debe mostrar un mockup en HTML correspondiente

@REQ-MOCK-002
Escenario: Descargar mockup generado
  Dado que el usuario ha generado un mockup
  Cuando el usuario solicita descargar el mockup
  Entonces el sistema debe permitir la descarga del archivo HTML

@REQ-MOCK-003
Escenario: Compartir mockup generado
  Dado que el usuario ha generado un mockup
  Cuando el usuario solicita compartir el mockup
  Entonces el sistema debe proporcionar un enlace compartible
