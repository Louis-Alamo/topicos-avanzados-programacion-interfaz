class NegativeNumberException(Exception):
    """
    Excepción para indicar que no se permiten cantidades negativas.

    Args:
        message (str, opcional): Mensaje personalizado de la excepción. 
            Por defecto, el mensaje es "No se permiten cantidades negativas".
    """

    def __init__(self, message="No se permiten cantidades negativas"):
        """
        Inicializa una nueva instancia de NegativeNumberException.

        Args:
            message (str, opcional): Mensaje personalizado de la excepción.
                Por defecto, el mensaje es "No se permiten cantidades negativas".
        """
        super().__init__(message)
