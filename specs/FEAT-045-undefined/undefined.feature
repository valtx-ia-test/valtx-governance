# language: es

@REQ-UND-001
Escenario: Proporcionar respuesta al usuario
  Dado que el usuario solicita información
  Cuando el sistema procesa la solicitud
  Entonces el sistema debe proporcionar una respuesta en un tiempo razonable

@REQ-UND-002
Escenario: Validar datos del usuario
  Dado que el usuario envía datos
  Cuando el sistema valida la entrada
  Entonces el sistema debe confirmar que los datos cumplen con las reglas definidas
