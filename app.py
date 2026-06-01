<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Práctica de Ecuaciones</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="container">

    <h1>📚 Ecuaciones de Primer Grado</h1>

    <div class="card">

        <h2 id="equation">2x + 3 = 7</h2>

        <input
            type="number"
            id="answer"
            placeholder="Ingresa x">

        <div class="buttons">
            <button onclick="checkAnswer()">
                Verificar
            </button>

            <button onclick="generateEquation()">
                Nueva pregunta
            </button>
        </div>

        <p id="message"></p>

        <h3>Aciertos: <span id="score">0</span></h3>

    </div>

</div>

<canvas id="confetti"></canvas>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>
<script src="script.js"></script>

</body>
</html>
