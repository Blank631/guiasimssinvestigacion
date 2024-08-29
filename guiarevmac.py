import tkinter as tk
from tkinter import simpledialog, messagebox

def mostrar_nota_inicial():
    # Mostrar una nota o mensaje de bienvenida
    messagebox.showinfo("Instrucciones", "Bienvenido a la aplicación de revisión, se realizarán 100 preguntas referentes al protocolo asignado. En esta versión no es posible regresar a las preguntas una vez contestadas u omitidas.")

def obtener_respuesta(pregunta):
    respuesta = simpledialog.askstring("Entrada", pregunta + " (Deja en blanco si no aplica):")
    if respuesta is None:  # Si el usuario presiona "Cancelar"
        root.quit()  # Cierra la aplicación
        exit()  # Termina el script
    return respuesta


variables = {
    "1. Título I.A.": "Es conciso, pero suficientemente informativo.",
    "2. Título I.B.": "Se ajusta a los límites teóricos y metodológicos del protocolo.",
    "3. Título I.C.": "Identifica la naturaleza del trabajo; Diseño, objetos de estudio, sujetos, y contexto.",
    "4. Título II.A.": "Permite identificar el estado basal (objetos de estudio) el desenlace o resultado (que se busca) y las maniobras o procedimientos (a través de que).",
    "5. Identificación de los Investigadores III.A.": "Nombre completo de cada uno de ellos.",
    "6. Identificación de los Investigadores III.B.": "Adscripción.",
    "7. Identificación de los Investigadores III.C.": "Área de trabajo.",
    "8. Identificación de los Investigadores III.D.": "Teléfono con extensión – Celular.",
    "9. Identificación de los Investigadores III.E.": "Correo electrónico.",
    "10. Resumen IV.A.": "Título del protocolo.",
    "11. Resumen IV.B.": "Antecedentes.",
    "12. Resumen IV.C": "Objetivo.",
    "13. Resumen IV.D": "Material y métodos.",
    "14. Resumen IV.E": "Recursos e infraestructura.",
    "15. Resumen IV.F": "Experiencia del grupo.",
    "16. Resumen IV.G": "Tiempo a desarrollarse.",
    "17. Resumen IV.H": "No incluir referencias.",
    "Gracias por tu colaboración, tu atención a los protocolos afecta directamente al proceso de la investigación": "(✿◠‿◠), los siguiente a valorar son los ANTECEDENTES CIENTÍFICOS",
    "18. Marco teórico V.A": "¿La información se relaciona en forma directa con el problema en estudio?",
    "19. Marco teórico V.A.1":" Presenta antecedentes concisos, resultantes de una búsqueda exhaustiva. ",
    "20. Marco teórico V.A.2":" Presenta antecedentes relevantes y actualizados (mínimo 80 % de los últimos 5 años).",
    "21. Marco teórico V.B.1":" Proporciona una visión clara del estado actual de los conocimientos sobre el problema a estudiar, presentando el estado del arte del conocimiento del o los objetos de estudio y de la relación entre los objetos de estudio en función del problema de estudio. ",
    "22. Marco teórico V.B.1.a":" Antecedentes a nivel instrumental.",
    "23. Marco teórico V.B.1.b":" Antecedentes a nivel descriptivo." ,
    "24. Marco teórico V.B.1.c":" Antecedentes a nivel analítico." ,
    "25. Marco teórico V.B.1.d":" Antecedentes a nivel experimental.",
    "26. Marco teórico V.C":" ¿Se fundamentan de manera adecuada, el planteamiento del problema, los objetivos y los métodos? ",
    "27. Marco teórico V.C.1 ":"Se presentan los conceptos implícitos en el planteamiento del problema.",
    "28. Marco teórico V.C.2":" Se presentan los conceptos implícitos en los objetivos. ",
    "29. Marco teórico V.C.3":" Se presentan los conceptos implícitos en los métodos. ? ",
    "30. Marco teórico V.C.4":" Se presentan las fuentes primaria o secundarias que fundamentes el diseño del estudio.", 
    "31. Marco teórico V.C.5":" Se incluye una teoría empleada para definir el problema ",
    "32. Marco teórico V.C.6":" La teoría empleada interpreta el o los fenómenos que el protocolo plantea explicar. ",
    "33. Marco teórico V.C.7":" Las referencias bibliográficas están bien señaladas utilizando solo un estilo en todas las referencias del protocolo? ",
    "34. Marco teórico V.C.8":"  Cada referencia bibliográfica concuerda con las afirmaciones que se le atribuyen?  ",
    "35. Marco teórico V.C.9":" Cada párrafo de los antecedentes científicos como del marco téorico tiene por lo menos una referencia bibliográfica?  ",
    "36. Marco teórico V.C.10":" El contenido de las referencias bibliográficas esta parafraseado o se redacta textualmente",
    "37. Justificación VI.A.1":"Se explica claramente la pertinencia (magnitud, trascendencia) del estudio en relación con los temas prioritarios de investigación institucionales. ",
    "38. Justificación VI.A.2":" Se explica claramente la necesidad del conocimiento y la información que se espera obtener con la investigación (contribución o beneficio))." ,
    "39. Justificación VI.A.3":"Se explica claramente la finalidad o propósito que se busca con el conocimiento que brindará el estudios.", 
    "40. Justificación VI.A.4":" Se explica claramente cuál es el resultado esperado  y como utilizarán en la práctica cotidiana en sus unidades de atención." , 
    "41. Justificación VI.A.5":" Se explica claramente quienes serán los beneficios o contribución para los participante, comunidad, IMSS con los resultados que brindará el estudios." , 
    "42. Planteamiento del problema VII.A1":"Se explica claramente cuál es el problema en el que se enmarca el estudio. Reflejando el estado del arte del conocimiento y el vacío del conocimiento, o las discrepancias o contradicciones en el estado del arte del conocimiento del objeto de estudio.",
    "43. Planteamiento del problema VII.A2":" Se plantea una pregunta de investigación, con la cual al responderse llenaría el vacío en el conocimiento o aclararía las discrepancia o contradicciones.",
    "44. Planteamiento del problema VII.B1 ":"Identifica claramente el problema y lo aísla de otros similares, fundamentando en forma sintetizada los antecedentes científicos pertinentes que reflejan el problema de investigación. ",
    "45. Planteamiento del problem VII.B2a ":" Se identifican las variables en estudio. La formulación del problema solo se limita al o los objetos de estudio y no incorpora objetos de estudio o sujetos ajenos al problema de investigación.",  
    "46. Planteamiento del problem VII.B2b ":" Se identifica la relación entre las variables de estudio, lo cual quedo bien fundamentada en el marco teórico. ",
    "Vamos bien":" los objetivos ahora tenemos que valorar ☜(ˆ▿ˆc)",
    "47. Objetivos VIII.A1":" Se incluye un objetivo general y los objetivos específicos que sean necesarios. Justificar la inclusión o eliminación de objetivos específicos.", 
    "48. Objetivos VIII.A2":"El objetivo general es congruente con el título del protocolo, hipótesis, objetivos específicos y métodos, fundamentando por que no son congruentes. ",
    "49. Objetivos VIII.A3":"Los objetivos específicos son congruentes con el objetivo general o con el y/o métodos propuestos para alcanzar cada uno de ellos, justificando por que no se alcanzarían.",
    "50. Objetivos VIII.A4":"Son pertinentes de acuerdo a las características específicas de cada estudio. Los objetivos y el diseño es congruente con la pregunta de investigación en caso que este bien formulada. ",
    "51. Objetivos VIII.B1":" Cada objetivo (general o específico) está planteado de manera que permita diseñar un estudio para su consecución. Estánformulados de manera lógica y sistemática. ",
    "52. Objetivos VIII.B2a":" Cada objetivo (general o específico) está adecuadamente operacionalizado. Se presenta una operacionalización fundamentada en el marco teórico.",
    "53. Objetivos VIII.B2b":" Cada objetivo (general o específico) está adecuadamente operacionalizado. Presenta la definición de los conceptos que emanan de los objetivos, así como las definiciones de sus dominios (si son pertinentes), sus dimensiones, la variabilidad de los conceptos, se definen los indicadores y sus escalas, los ítems son pertinentes y reflejan la concreción de los conceptos operacionalizados.",
    "54. Hipótesis de trabajo (en caso pertinente) IX.A1":"La hipótesis predice lógicamente la respuesta probable a la pregunta que se hizo en el planteamiento del problema. ",
    "55. Hipótesis de trabajo IX.A2":" La hipótesis es congruente con el objetivo principal.",
    "56. Hipótesis de trabajo IX.A3":" La hipótesis plantea de forma clara, breve y concisa cuál es el resultado esperado. ",
    "57. Hipótesis de trabajo IX.A4":" La hipótesis se plantea como una afirmación en términos cuantificables.  ",
    "58. Hipótesis de trabajo IX.A5":"La hipótesis permiten su evaluación con base a la teoría de probabilidad a través de una prueba de hipótesis (significancia, correlación, asociación, etc.). Ya que es una verdad provisional que será o no descartada por los resultados. ",
    "59. Hipótesis de trabajo IX.B1":"  Hay un objetivo (general o especifico) por cada hipótesis que se planteó. ",
    "60. Hipótesis de trabajo IX.B2":" Se identifica la dirección (es positiva o negativa, se acerca o se aleja del valor nulo de la hipótesis) de cada hipótesis.   ",
    "61. Hipótesis de trabajo IX.B3":"Se identifica el compromiso (probable magnitud) de cada hipótesis.  ",
    "Ahora vamos a ver como planea realizar su proyecto":"(⊙.⊙(☉̃ₒ☉)⊙.⊙)",
    "62. Material y Métodos A1":"Se incluyen todos los apartados que sean pertinentes (universo de trabajo, lugar donde se desarrollará el estudio, descripción general del estudio, procesamiento de datos y aspectos estadísticos), de acuerdo con el tipo de estudio que se propone, ¿Qué apartados hacen falta?",
    "63. Material y Métodos B2":" El universo de trabajo se encuentra bien caracterizado y adecuada para el estudio.",
    "64. Material y Métodos B3":" Se define el tipo de muestreo (si es pertinente) ",
    "65. Material y Métodos B4":" Se establece el tamaño de la muestra necesaria para el estudio, utilizando la ecuación pertinente al diseño de estudios. ",
    "66. Material y Métodos B5":"  Todos los parámetros para determinar el tamaño de la muestra están justificados.",
    "67. Material y Métodos C1":" Se describen los criterios de selección (inclusión, no inclusión y eliminación. ",
    "68. Material y Métodos C2":"  Los criterios de selección son adecuados para el estudio.",
    "69. Material y Métodos C3":"  Los criterios de selección introducen algún sesgo de selección. ",
    "70. Material y Métodos D1":"La definición de las variables, tanto conceptrual como operacional (cómo se medirán) es clara y adecuada. Presenta la definición de los conceptos de las variables que emanan de los objetivos, así como las definiciones de sus dominios (si son pertinentes), sus dimensiones, la variabilidad de los conceptos, se definen los indicadores y sus escalas, los ítems son pertinentes y reflejan la concreción de los conceptos operacionalizados. ",
    "71. Material y Métodos E1 ":"  La reproducibilidad y la validez de los métodos y los instrumentos de medición que se utilizan en el estudio están descritas y son adecuadas.  ",
    "72. Material y Métodos E2":"  Se establece la técnica para evaluar la confiablidad de los métodos y los instrumentos de medición que se utilizan en el estudio. ",
    "73. Material y Métodos E3":"  Se establece la técnica para evaluar la validez de los métodos y los instrumentos de medición que se utilizan en el estudio (validez aparente, de contenidos, constructo exploratorio, constructo confirmatorio, criterio). ",
    "74. Material y Métodos E4":" Se establece la técnica para evaluar el desempeño de una prueba diagnóstica o de tamizaje (sensibilidad, especificidad, VP+, VP-, etc.), si es pertinente se presenta una curva ROC. ",
    "75. Material y Métodos F1":"La descripción del estudio es clara y está suficientemente detallada. Estableciendo el tipo de estudio y el diseño pertinente con el objetivo del estudio. ",
    "76. Material y Métodos F2":" La descripción del estudio es clara y está suficientemente detallada. Describiendo la direccionalidad y la cronología del diseño propuesto.  ",
    "77. Material y Métodos G1":" La sistematización de la recolección de los datos es adecuada y está plasmada en un manual operacional.  ",
    "78. Material y Métodos H1":" La descripción de los procedimientos, tanto observacionales como experimentales es clara y está suficientemente detallada, estableciendo quien, cuando, donde y como se desarrollarán los procedimientos. ",
    "79. Material y Métodos I1":" El estudio incluye alguna forma de control de calidad, definiendo los procedimientos para estandarizar la recolección de datos  ",
    "80. Material y Métodos I2":" El estudio incluye alguna forma de control de calidad, valorando la reproducibilidad intra y entre observadores. ",
    "81. Material y Métodos I3":" El estudio incluye alguna forma de control de calidad en la captura de datos. ",
    "82. Material y Métodos J1":"Se describen los métodos para procesar los datos; Codificación de las variables a analizar, transformación de las variables, programa para captura de datos, programa para el análisis de datos y comandos a utilizar.  ",
    "83. Material y Métodos J2":" Se describen los métodos el análisis estadístico que planea utilizar. Supuestos del análisis estadístico a utilizar (univarido, bivariado o multivariado). Estadígrafos para describir las variables, pruebas de hipótesis para análisis bivariados, pruebas de hipótesis para análisis multivariado.",
    "84. Material y Métodos K11":" En el caso de ser pertinente el análisis estadístico, el que propone es acorde a la forma en la que se calculó el tamaño de la muestra. ",
    "85. Ahora veremos":" Aspectos Éticos ( ◡́.◡̀)(^◡^ ), este lo valora el Comité Local de Investigación en Salud Comité de Ética en Investigación , sin embargo, si se observa inconsistencias mayores favor de comentar ",
    "86. Congruencia XII.A1":" ¿Existe congruencia entre la pregunta, el diseño y la descripción del estudio? .",
    "87. Congruencia XII.A2":" -¿Los objetivos y la metodología permitirán contestar la pregunta planteada?  .",
    "88. Originalidad XIII.A1":"¿Aporta algo nuevo a nivel internacional o nacional?.",
    "89. Trascendecia XIV.A1":"¿El trabajo es importante en su campo de especialidad, de acuerdo con su aportación al avance del conocimiento, aplicabilidad, impacto potencial, consecuencias, etc.?.",
    "90. Subsidiarios XV.A1":"¿La sintaxis y la ortografía son correctas?", 
    "91. Subsidiarios XV.A2":"- ¿Otorga los créditos en forma adecuada?", 
    "92. Recursos, Financiamiento. Factibilidad":" XVI",
    "93. Cronograma de actividades XVII" :"La gráfica de Gantt presenta las fechas de inicio y conclusión de cada una de las actividades. ",
    "94. Referencias Bibliográficas XVIII.A1":"Se siguen los lineamientos internacionales de redacción del escrito médico, el estilo que aparece en las instrucciones para los autores en la revista Archives of Medical Research. ",
    "95. Referencias Bibliográficas XVIII.A2":"Las referencias bibliográficas se presentan de forma sistematizada utilizando un estilo único (Vancouver, APA, MLA, etc). ",
    "96. Referencias Bibliográficas XVIII.A3":" No se deben usar como referencia los datos de resúmenes, observaciones no publicadas y/o comunicaciones personales. ",
    "97. Anexos XV.A1":"Se presenta como anexo los instrumentos para la recolección de datos. ",
    "98. Anexos XV.A2":"Se presenta como anexo un manual operacional. ",
    "99. Anexos XV.A3":"Se presenta como anexo la operacionalización de conceptos. ",
    "100. Ya acabaste de revisar, Gracias ❤":" Comentarios finales sobre el protocolo (Felicitaciones, dudas importantes que no se encuentren en guía)",
}

respuestas = {}

def iniciar():
    mostrar_nota_inicial()  # Mostrar la nota al inicio
    for clave, descripcion in variables.items():
        recomendacion = obtener_respuesta(f"{clave} - {descripcion}\nRecomendaciones (Problema y Propuesta):")
        if recomendacion.strip() != "":
            respuestas[clave] = {"Recomendaciones": recomendacion}

    mostrar_resultados()

def mostrar_resultados():
    if not respuestas:
        messagebox.showinfo("Resultados", "No se han proporcionado respuestas.")
        return

    resultado = "\nRespuestas proporcionadas:"
    for clave, respuesta in respuestas.items():
        resultado += f"\n\n{clave} - {variables[clave]}"
        for campo, valor in respuesta.items():
            if valor:
                resultado += f"\n{campo}: {valor}"
    
    # Mostrar el resultado en una nueva ventana con un cuadro de texto para copiar
    result_window = tk.Toplevel(root)
    result_window.title("Resultados")

    text_box = tk.Text(result_window, wrap='word', height=20, width=80)
    text_box.insert('1.0', resultado)
    text_box.config(state='disabled')  # Hacer el texto no editable

    scroll_y = tk.Scrollbar(result_window, orient='vertical', command=text_box.yview)
    text_box.config(yscrollcommand=scroll_y.set)

    copy_button = tk.Button(result_window, text="Copiar al Portapapeles", command=lambda: copiar_al_portapapeles(text_box))
    copy_button.pack(pady=10)

    text_box.pack(side='left', fill='both', expand=True)
    scroll_y.pack(side='right', fill='y')

def copiar_al_portapapeles(text_box):
    result_window.clipboard_clear()  # Limpiar el portapapeles
    result_window.clipboard_append(text_box.get('1.0', 'end-1c'))  # Copiar el texto al portapapeles
    result_window.update()  # Actualizar la ventana

# Crear la ventana principal
root = tk.Tk()
root.withdraw()  # Oculta la ventana principal

# Iniciar el proceso de preguntas
iniciar()

root.mainloop()