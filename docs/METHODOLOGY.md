# Metodología y alcance de las demostraciones

## Experiencia profesional y evidencia pública

Los casos aplicados describen el enfoque de trabajo de Nicolás Alderete en supervisión de Customer Service, reporting y herramientas operativas. No se publican bases, clientes, identificadores, cifras internas ni código de producción de deRentas. La autoría se limita a la contribución descrita, dentro de un trabajo de equipo.

Las interfaces y el código de demostración fueron creados para este portfolio. No son capturas de sistemas internos ni prueban un despliegue productivo. No se atribuyen ahorros de tiempo, reducción de churn ni mejoras económicas que no hayan sido medidos.

## Bajas y retención

- Dataset: `assets/downloads/churn_demo.csv`. Sus 12 registros son completamente ficticios.
- Cada ID representa un caso de salida. El motivo y la antigüedad se crean únicamente para explicar la segmentación.
- Mediana: ordenar los días de antigüedad; tomar el valor central o la media de los dos centrales cuando la muestra es par.
- Casos con antigüedad menor a 90 días: comparación estricta `< 90`. Un caso de 90 días no pertenece a ese grupo.
- Todos: n=12, mediana=82,5 días; menores a 90 días=6/12.
- Motivos personales: n=4, mediana=90 días; menores a 90 días=2/4.
- Rentabilidad insuficiente: n=4, mediana=60 días; menores a 90 días=3/4.
- Decisión de la compañía: n=4, mediana=120 días; menores a 90 días=1/4.
- Estas proporciones describen la muestra de bajas seleccionada. No son una tasa de churn: no existe aquí un denominador de clientes activos o expuestos al riesgo.
- La demo no calcula LTV, rentabilidad, inferencia causal ni desempeño real de clientes.

## Agenda de revisiones

Recreación en JavaScript, independiente de la implementación interna en Google Apps Script.

- Reloj local del dispositivo para el mínimo de 48 horas entre la hora actual y el turno propuesto.
- Semana definida de lunes a domingo para la regla de una unidad por semana.
- Días disponibles en la demo: lunes a viernes.
- Horarios ficticios de ejemplo: 09:15, 09:30, 10:00 y 13:00. El horario 18:00 se incluye para probar un rechazo.
- Reserva de ejemplo: DEMO01, a las 10:00 del primer día hábil que cae al menos tres días de calendario después del día actual. Se crea solo en memoria del navegador.
- La validación devuelve el primer motivo de revisión encontrado, en orden: fecha, anticipación, día, horario, duplicado.
- No verifica capacidad real, permisos, colisiones concurrentes ni persistencia. No envía solicitudes ni almacena datos personales.

## Proyectos académicos

Los casos de Power BI y Tableau remiten a sus documentos públicos originales y sus revisiones técnicas. No se supone equivalencia de fuentes, filtros ni totales entre implementaciones. Los resultados reportados en informes no se presentan como cifras recalculadas.

## English summary

Applied cases describe professional contributions without publishing internal data or production code. All browser demonstrations were newly created for this portfolio, using entirely fictional records. The churn view describes the selected departure sample, not a churn rate. Scheduling checks use the device’s local clock and a Monday-to-Sunday week and do not create real bookings or validate real capacity. Academic BI projects retain their documented limitations; reported results are not presented as recalculated figures.
