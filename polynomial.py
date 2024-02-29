class Polynomial: # Creation of the class polynomial to save the number the grade and the var of the polynomial
    def __init__(self, component: int, grade: int, var) -> None:
        self.component = component
        self.grade = grade
        self.var = var

    def __str__(self) -> str: # This is to show in console as string the components of the polynomial
        if self.component >= 0:
            return str(f"+{self.component}{self.var}^{self.grade}")
        else:
            return str(f"{self.component}{self.var}^{self.grade}")