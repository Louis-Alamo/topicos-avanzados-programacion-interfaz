class InvalidRangeException(Exception):
    """
    Excepción para indicar que el límite inferior no puede ser mayor que el límite superior.

    Args:
        message (str, opcional): Mensaje personalizado de la excepción.
            Por defecto, el mensaje es "El límite inferior no puede ser mayor que el límite superior".
    """

    def __init__(self, message="El límite inferior no puede ser mayor que el límite superior"):
        """
        Inicializa una nueva instancia de InvalidRangeException.

        Args:
            message (str, opcional): Mensaje personalizado de la excepción.
                Por defecto, el mensaje es "El límite inferior no puede ser mayor que el límite superior".
        """
        super().__init__(message)
