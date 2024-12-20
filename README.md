## Ejecutando pruebas
Ejecutar suite de pruebas creada
```
PYTHONPATH=. python tests/test_suites.py
```

Si queremos ejecutar todas las pruebas de una clase
```
PYTHONPATH=. python -m unittest  tests.test_calculator.Calcul
atorTest
```
O una prueba específica de la clase
```
PYTHONPATH=. python -m unittest  tests.test_calculator.CalculatorTest.test_suma
```

## Mejores prácticas a seguir
### Formato
- Todos los test deben estar agrupados en clases y esta clase debe estar a la par con la clase de tu proyecto. Ejm BankAccoutTest deberá probar la clase BankAccout
- El nombre del archivo siempre debe iniciar con test_
- El nombre del método siempre debe iniciar con test_ y el nombre del método a probar debe coincidir con el método de la clase:
    - test_deposit deberá realizar la prueba del método deposito de la clase BankAccout
- Validar los escenarios: Si un método recibe un número como parámetro, se puede por ejemplo validar los distintos escenarios en diferentes métodos:
- Resultado esperado: Indicar el resultado esperado. Con todos estos puntos, el nombre del método quedaría de la siguiente manera:
```
test_deposit_positive_amount_increase_balance
test_deposit_negative_amount_increase_balance
``` 
### ¿Por qué es útil este formato?
- Permite a cualquier miembro del equipo entender el propósito de la prueba sin revisar el código completo.
- Facilita el mantenimiento del código y el soporte, ya que con solo leer el nombre, se entiende el objetivo de la prueba.
>Nombrar las pruebas de forma clara es muy útil para todo el equipo de desarrollo. Podremos entender el propósito de las pruebas únicamente leyendo los formatos sin necesidad de indagar a fondo el código fuente.


# Mocking de APIs externas
![Mockin](images/mockin.png)
Un Mock es una herramienta que nos permite simular comportamientos de funciones o servicios externos. En lugar de ejecutar una llamada real a una API, podemos definir una respuesta predefinida, lo que permite:

- Evitar depender de servicios externos en pruebas.
- Acelerar la ejecución de las pruebas.
- Controlar los resultados esperados.

# Side Effects en Mocking
![Side Effect](images/side_effect.png)

El “side effect” en Mock nos permite modificar el comportamiento de un método en distintas llamadas. Se define como una lista de comportamientos, donde cada elemento de la lista corresponde al resultado de una llamada específica. Esto permite:

- Simular fallos de manera controlada, como lanzar excepciones específicas en las pruebas.
- Probar el código bajo diferentes condiciones sin interactuar con los servicios externos.

```
python -m unittest tests.test_api_client.ApiClientTest.test_get_location_return_side_effect
```

# SubTest
![Subtest](images/subtests.png)
Nos ayuda a realizar validaciones con varios valores sin la necesidad de crear varios métodos. SubTest también es útil para identificar errores específicos. Si una prueba falla con un conjunto particular de parámetros, SubTest permitirá identificar fácilmente qué valores causaron el fallo. 

```
python -m unittest tests.test_bank_account.BankAccoutTest.test_deposit_multiple_amounts
```

# Doctest
![Doctest](images/doc_test.png)
Doctest es una librería que está incluida en Python y que permite crear pruebas en los comentarios del código.

# Faker
![Faker](images/faker.png)
```
pip install Faker
pip freeze | grep Kaker
```

# Coverage
```

coverage run --source src -m unittest
coverage report
```
![Coverage report](images/report.png)

Si queremos ver un reporte más detallado y dinámico sacamos el reporte en formato html.
```
coverage html
```
![Coverage html](images/report_html.png)
Podemos hacer clic en cada uno de los nombres donde se mostrará la cobertura de las pruebas. 
A modo de pruebas, al hacer clic en el archivo que está con 98% de convertura, se mostrará la parte no cubierta
![Report Detail](images/report_detail.png)

Si corregimos la parte que no tiene cobertura y ejecutamos nuevamente el comando ```coverage html``` cambiará el resultado.
![Coverage html full](images/report_html_full.png)

![Report Detail](images/report_detail_full.png)