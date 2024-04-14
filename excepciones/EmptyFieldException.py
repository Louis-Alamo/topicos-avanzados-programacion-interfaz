class EmptyFieldException(Exception):
    """
    Excepción para indicar que no se permiten campos vacíos al ingresar valores.

    Args:
        message (str, opcional): Mensaje personalizado de la excepción.
            Por defecto, el mensaje es "No se permiten campos vacíos.".
    """

    def __init__(self, message="No se permiten campos vacíos."):
        """
        Inicializa una nueva instancia de EntryVoidException.

        Args:
            message (str, opcional): Mensaje personalizado de la excepción.
                Por defecto, el mensaje es "No se permiten campos vacíos.".
        """
        super().__init__(message)
