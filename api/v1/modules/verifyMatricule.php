<?php

function verifyMatricule() {
    // Ajout des headers requis
    header('Access-Control-Allow-Origin: *');
    header("Content-Type: application/json");

    
    global $pdo;

    // La seule méthode autorisée est GET
    if ($_SERVER['REQUEST_METHOD'] !== 'GET') {
        http_response_code(405);
        echo json_encode(["error" => "Methode HTTP non autorisée"]);
        exit();
        }

    
    preg_match('/\/api\/v([0-9]+)\/([A-Za-z]+)\/([A-Za-z0-9]+)/', $_SERVER['REQUEST_URI'], $matches);

    // Vérification que la route contienne la version de l'API ($matches[1]) et un matricule ($matches[2]) 
    if (!isset($matches[1]) || !isset($matches[2]) || !isset($matches[3])) {
        http_response_code(400);
        echo json_encode(["error" => "Route invalide"]);
        exit();
    }
    
    // continuer...

}



?>