if __name__ == "__main__":
    print ("Cristiano Ronaldo")
    print ("Interstellar")
    print ("Breaking Bad")
    print ("Bad Bunny")
    print ("Batman")
    print ("Aguascalientes")
    tema= input("Hola, ingresa el nombre del tema de tu interes: ")
    match tema:
        case "Cristiano Ronaldo":
            print ("Cristiano Ronaldo es un futbolista portugués considerado uno de los mejores jugadores de todos los tiempos. Ha ganado múltiples Balones de Oro y ha jugado en clubes como el Manchester United, Real Madrid y Juventus.")
        case "Interstellar":
            print ("Interestelar (Interstellar) es una película de ciencia ficción estrenada en 2014 y dirigida por Christopher Nolan. Está protagonizada por Matthew McConaughey, quien interpreta a Cooper, un expiloto que viaja al espacio para encontrar un planeta habitable y salvar a la humanidad de la escasez de alimentos y las condiciones ambientales de la Tierra. Durante su misión, enfrenta fenómenos como los agujeros negros, la relatividad del tiempo y los viajes espaciales. La película combina ciencia, aventura y emociones familiares, destacando el amor entre un padre y su hija como uno de sus temas principales.")
        case "Breaking Bad":
            print ("Breaking Bad es una serie de televisión creada por Vince Gilligan. La historia sigue a Walter White, un profesor de química que se convierte en fabricante de metanfetamina.")
        case "Bad Bunny":
            print ("Bad Bunny, cuyo nombre real es Benito Antonio Martínez Ocasio, nació el 10 de marzo de 1994 en Vega Baja, Puerto Rico. Es cantante, rapero y compositor, reconocido mundialmente por el reguetón y el trap latino. Comenzó su carrera en internet y alcanzó la fama internacional con canciones como «DÁKITI», «Tití Me Preguntó» y «Me Porto Bonito». Entre sus principales álbumes destacan X 100pre (2018), YHLQMDLG (2020), Un Verano Sin Ti (2022), Nadie Sabe Lo Que Va a Pasar Mañana (2023) y DeBÍ TiRAR MáS FOToS (2025). Su música combina ritmos urbanos con elementos de la cultura puertorriqueña, convirtiéndolo en uno de los artistas latinos más influyentes")
        case "Batman":
            print ("Batman es un superhéroe ficticio de DC Comics, creado por Bob Kane y Bill Finger, que apareció por primera vez en 1939. Su nombre real es Bruce Wayne, un millonario de Ciudad Gótica que combate el crimen después de presenciar el asesinato de sus padres cuando era niño. A diferencia de otros superhéroes, no tiene poderes sobrenaturales, sino que utiliza su inteligencia, entrenamiento, tecnología y habilidades de detective. Entre sus enemigos más conocidos están el Joker, el Pingüino y Dos Caras. Batman ha protagonizado cómics, películas, series y videojuegos, convirtiéndose en uno de los superhéroes más famosos del mundo.")
        case "Aguascalientes":
            print ("Aguascalientes es un estado ubicado en el centro de México, cuya capital lleva el mismo nombre. Fue fundado como estado en 1857 y su nombre proviene de sus numerosas aguas termales. Es conocido por la Feria Nacional de San Marcos, una de las celebraciones más importantes del país, así como por su tradición taurina, gastronomía y arquitectura histórica. Su economía destaca por la industria automotriz, el comercio y los servicios. Además, cuenta con lugares emblemáticos como el centro histórico y el Jardín de San Marcos, que reflejan su riqueza cultural y turística.")
        case _:
            print ("Lo siento, no tengo información sobre ese tema.")
            